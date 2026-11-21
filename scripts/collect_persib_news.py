#!/usr/bin/env python3
"""Collect a lightweight Persib news digest from Google News RSS.

This is a discovery feed, not a fact-checker. Every item must be opened and
checked against its original publisher before being used as a factual claim.
"""
from datetime import datetime
from zoneinfo import ZoneInfo
from urllib.parse import urlencode
from urllib.request import Request, urlopen
from xml.etree import ElementTree as ET
from html import unescape
from html.parser import HTMLParser
from pathlib import Path
import os
import re

TZ = ZoneInfo("Asia/Jakarta")
OUT = Path("research/daily")
BASE = "https://news.google.com/rss/search?"
QUERIES = [
    ("Berita umum Persib", "Persib Bandung"),
    ("Transfer dan rumor", 'Persib Bandung (transfer OR rumor OR rekrutmen)'),
    ("Kondisi pemain", 'Persib Bandung (cedera OR absen OR kebugaran OR latihan)'),
    ("Pertandingan dan taktik", 'Persib Bandung (jadwal OR preview OR analisis OR starting XI)'),
]

class StripHTML(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts = []
    def handle_data(self, data):
        self.parts.append(data)

def clean_html(value):
    parser = StripHTML()
    parser.feed(unescape(value or ""))
    return re.sub(r"\\s+", " ", " ".join(parser.parts)).strip()

def fetch(query):
    params = urlencode({"q": query, "hl": "id", "gl": "ID", "ceid": "ID:id"})
    req = Request(BASE + params, headers={"User-Agent": "Mozilla/5.0 PersibContentFactory/1.0"})
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

def main():
    now = datetime.now(TZ)
    OUT.mkdir(parents=True, exist_ok=True)
    custom = os.getenv("CUSTOM_QUERY", "").strip()
    queries = list(QUERIES)
    if custom:
        queries.insert(0, ("Topik tambahan dari editor", custom))

    seen = set()
    sections = []
    total = 0
    for label, query in queries:
        try:
            found = fetch(query)
        except Exception as exc:
            sections.append(f"## {label}\\n\\n_Pengambilan feed gagal: {type(exc).__name__}: {exc}_\\n")
            continue
        rows = []
        for item in found:
            key = item["link"] or item["title"]
            if not key or key in seen:
                continue
            seen.add(key)
            total += 1
            desc = item["description"][:500] if item["description"] else "Tidak ada ringkasan dari feed."
            rows.append(
                f"### {len(rows)+1}. {item['title']}\\n"
                f"- Media/sumber tertera: {item['source']}\\n"
                f"- Waktu publikasi (sesuai feed): {item['published'] or 'Tidak tersedia'}\\n"
                f"- Tautan artikel asli: {item['link']}\\n"
                f"- Cuplikan: {desc}\\n"
                f"- Status: **HASIL INDEKS — BELUM DIVERIFIKASI**\\n"
            )
        sections.append(f"## {label}\\n\\n" + ("\\n".join(rows) if rows else "_Belum ada hasil pada feed ini._") + "\\n")

    content = (
        f"# Persib News Monitor — {now:%d %B %Y, %H:%M WIB}\\n\\n"
        f"- Dibuat otomatis: {now.isoformat(timespec='minutes')}\\n"
        f"- Jumlah tautan unik: {total}\\n"
        "- Status keseluruhan: **BAHAN RISET, BUKAN FAKTA TERVERIFIKASI**\\n"
        "- Pengumpul memakai Google News RSS untuk menemukan artikel; verifikasi wajib dilakukan pada artikel/pengumuman asli.\\n"
        "- Jangan mengubah rumor menjadi kepastian. Informasi cedera, sanksi, dan ketersediaan pemain perlu konfirmasi kuat.\\n"
        "- Foto/video tidak otomatis boleh digunakan hanya karena muncul di artikel atau media sosial.\\n\\n"
        + "\\n".join(sections)
        + "\\n## Catatan editor\\n"
        "- Angle yang dipilih: _menunggu keputusan editor_\\n"
        "- Koreksi/konteks tambahan: _menunggu editor_\\n"
        "- Status editorial: **PENDING**\\n"
    )
    stamp = now.strftime("%Y-%m-%d-%H00")
    (OUT / f"{stamp}.md").write_text(content, encoding="utf-8")
    (OUT / "latest.md").write_text(content, encoding="utf-8")
    print(f"Saved research/daily/{stamp}.md with {total} unique links")

if __name__ == "__main__":
    main()
