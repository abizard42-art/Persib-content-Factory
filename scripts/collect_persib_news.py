#!/usr/bin/env python3
"""Collect and organize Persib news discovery feeds.

This is an indexing and triage aid, not a fact-checker or editorial decision-maker.
"""
from datetime import datetime
from email.utils import parsedate_to_datetime
from zoneinfo import ZoneInfo
from urllib.parse import urlencode
from urllib.request import Request, urlopen
from xml.etree import ElementTree as ET
from html import unescape
from html.parser import HTMLParser
from pathlib import Path
import os
import re
import unicodedata

TZ = ZoneInfo("Asia/Jakarta")
OUT = Path("research/daily")
BASE = "https://news.google.com/rss/search?"
QUERIES = [
    ("Berita umum Persib", "Persib Bandung"),
    ("Transfer dan rumor", 'Persib Bandung (transfer OR rumor OR rekrutmen)'),
    ("Kondisi pemain", 'Persib Bandung (cedera OR absen OR kebugaran OR latihan)'),
    ("Pertandingan dan taktik", 'Persib Bandung (jadwal OR preview OR analisis OR starting XI)'),
]
CATEGORIES = {
    "TRANSFER": ("transfer", "rumor", "rekrut", "kontrak", "pinjam", "permanen", "negosiasi", "gabung", "direkrut"),
    "KONDISI PEMAIN": ("cedera", "absen", "pulih", "fit", "kebugaran", "latihan", "sanksi", "skors", "kembali"),
    "MATCH & JADWAL": ("jadwal", "lawan", "vs", "pertandingan", "bali united", "persija", "persik", "persis", "liga"),
    "TAKTIK & STARTING XI": ("starting xi", "susunan pemain", "formasi", "taktik", "strategi", "rotasi", "skema", "preview", "analisis"),
}
RUMOR_TERMS = ("rumor", "rumor", "dikabarkan", "disebut", "berpeluang", "negosiasi", "minat", "incar")
OFFICIAL_SOURCES = ("persib.co.id", "persib official", "liga indonesia baru", "pssi")

class StripHTML(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts = []
    def handle_data(self, data):
        self.parts.append(data)

def clean_html(value):
    parser = StripHTML()
    parser.feed(unescape(value or ""))
    return re.sub(r"\s+", " ", " ".join(parser.parts)).strip()

def normalize_title(value):
    value = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode().lower()
    value = re.sub(r"\s+-\s+[^-]+$", "", value)
    return re.sub(r"[^a-z0-9]+", " ", value).strip()

def classify(title):
    text = title.lower()
    for category, terms in CATEGORIES.items():
        if any(term in text for term in terms):
            return category
    return "UPDATE UMUM"

def source_kind(source):
    s = source.lower()
    if any(term in s for term in OFFICIAL_SOURCES):
        return "KANAL RESMI (tetap buka sumber asli)"
    return "MEDIA / AGREGATOR (perlu cek artikel asli)"

def priority(item):
    title = item["title"].lower()
    score = 1
    if "persib" in title or "maung bandung" in title:
        score += 2
    if item["category"] != "UPDATE UMUM":
        score += 1
    if item["source_kind"].startswith("KANAL RESMI"):
        score += 1
    return min(score, 5)

def published_sort(item):
    try:
        dt = parsedate_to_datetime(item["published"])
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=TZ)
        return dt.timestamp()
    except Exception:
        return 0

def fetch(query):
    params = urlencode({"q": query, "hl": "id", "gl": "ID", "ceid": "ID:id"})
    req = Request(BASE + params, headers={"User-Agent": "Mozilla/5.0 PersibContentFactory/1.1"})
    with urlopen(req, timeout=25) as response:
        root = ET.fromstring(response.read())
    items = []
    for item in root.findall("./channel/item"):
        source = item.find("source")
        items.append({
            "title": (item.findtext("title") or "").strip(),
            "link": (item.findtext("link") or "").strip(),
            "published": (item.findtext("pubDate") or "").strip(),
            "source": (source.text or "").strip() if source is not None else "Sumber tidak terdeteksi",
            "description": clean_html(item.findtext("description") or ""),
        })
    return items

def render_board(items):
    ranked = sorted(items, key=lambda x: (priority(x), published_sort(x)), reverse=True)
    lines = [
        "## Papan kandidat editorial",
        "",
        "> Pengelompokan dan skor dibuat otomatis dari judul/sumber feed. Ini alat penyaringan, bukan verifikasi, penilaian kualitas jurnalistik, atau keputusan topik.",
        "",
        "**Skor prioritas 1–5** hanya mengukur kecocokan kata kunci dan jenis sumber; bukan tingkat kebenaran berita.",
        "",
    ]
    if not ranked:
        return "\n".join(lines + ["_Belum ada kandidat dari feed yang berhasil diambil._", ""])
    for category in ("TRANSFER", "KONDISI PEMAIN", "MATCH & JADWAL", "TAKTIK & STARTING XI", "UPDATE UMUM"):
        group = [x for x in ranked if x["category"] == category][:8]
        if not group:
            continue
        lines.extend([f"### {category}", ""])
        for item in group:
            rumor = " | **Ada kata bernuansa rumor/laporan belum pasti**" if any(t in item["title"].lower() for t in RUMOR_TERMS) else ""
            lines.extend([
                f"- **[{priority(item)}/5] {item['title']}**",
                f"  - Sumber: {item['source']} — {item['source_kind']}{rumor}",
                f"  - Publikasi feed: {item['published'] or 'Tidak tersedia'}",
                f"  - [Buka tautan hasil feed]({item['link']})",
            ])
        lines.append("")
    lines.extend([
        "### Keputusan editor",
        "",
        "- Topik yang dipilih: _belum dipilih_",
        "- Angle yang disetujui: _menunggu editor_",
        "- Konteks/koreksi dari editor: _menunggu editor_",
        "- Status: **PENDING — tidak ada naskah atau publikasi otomatis**",
        "",
    ])
    return "\n".join(lines)

def main():
    now = datetime.now(TZ)
    OUT.mkdir(parents=True, exist_ok=True)
    custom = os.getenv("CUSTOM_QUERY", "").strip()
    queries = list(QUERIES)
    if custom:
        queries.insert(0, ("Topik tambahan dari editor", custom))

    by_title = {}
    sections = []
    for label, query in queries:
        try:
            found = fetch(query)
        except Exception as exc:
            sections.append(f"## {label}\n\n_Pengambilan feed gagal: {type(exc).__name__}: {exc}_\n")
            continue
        rows = []
        for item in found:
            fingerprint = normalize_title(item["title"])
            if not fingerprint:
                continue
            item["category"] = classify(item["title"])
            item["source_kind"] = source_kind(item["source"])
            # Keep the first copy of a near-identical title across RSS queries.
            if fingerprint in by_title:
                continue
            by_title[fingerprint] = item
            desc = item["description"][:500] if item["description"] else "Tidak ada ringkasan dari feed."
            rows.append(
                f"### {len(rows)+1}. {item['title']}\n"
                f"- Media/sumber tertera: {item['source']}\n"
                f"- Waktu publikasi (sesuai feed): {item['published'] or 'Tidak tersedia'}\n"
                f"- Tautan hasil feed: {item['link']}\n"
                f"- Cuplikan: {desc}\n"
                f"- Kategori otomatis: {item['category']}\n"
                f"- Status: **HASIL INDEKS — BELUM DIVERIFIKASI**\n"
            )
        sections.append(f"## {label}\n\n" + ("\n".join(rows) if rows else "_Tidak ada hasil baru setelah deduplikasi judul._") + "\n")

    items = list(by_title.values())
    content = (
        f"# Persib News Monitor — {now:%d %B %Y, %H:%M WIB}\n\n"
        f"- Dibuat otomatis: {now.isoformat(timespec='minutes')}\n"
        f"- Jumlah kandidat unik berdasarkan normalisasi judul: {len(items)}\n"
        "- Status keseluruhan: **BAHAN RISET, BUKAN FAKTA TERVERIFIKASI**\n"
        "- Google News RSS dipakai untuk penemuan artikel; buka artikel/pengumuman asli sebelum memakai klaim.\n"
        "- Label kategori dan skor prioritas bersifat heuristik berdasarkan judul/sumber feed.\n"
        "- Jangan mengubah rumor menjadi kepastian. Kondisi pemain, sanksi, dan ketersediaan perlu konfirmasi kuat.\n"
        "- Foto/video tidak otomatis boleh digunakan hanya karena muncul di artikel atau media sosial.\n\n"
        + render_board(items)
        + "\n".join(sections)
        + "\n## Catatan editor\n"
        "- Angle yang dipilih: _menunggu keputusan editor_\n"
        "- Koreksi/konteks tambahan: _menunggu editor_\n"
        "- Status editorial: **PENDING**\n"
    )
    stamp = now.strftime("%Y-%m-%d-%H00")
    (OUT / f"{stamp}.md").write_text(content, encoding="utf-8")
    (OUT / "latest.md").write_text(content, encoding="utf-8")
    print(f"Saved research/daily/{stamp}.md with {len(items)} title-deduplicated candidates")

if __name__ == "__main__":
    main()
