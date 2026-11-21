#!/usr/bin/env python3
"""Build a reviewable script scaffold from an approved editorial markdown file."""
from pathlib import Path
import argparse
import re
import sys

APPROVAL = re.compile(r"\*\*Status akhir:\*\*\s*APPROVED FOR SCRIPT", re.I)

def field(text, label):
    match = re.search(rf"^\s*-\s*{re.escape(label)}\s*:\s*(.*?)\s*$", text, re.I | re.M)
    return match.group(1).strip() if match else ""

def section(text, heading):
    match = re.search(rf"^##\s+{re.escape(heading)}\s*$([\s\S]*?)(?=^##\s+|\Z)", text, re.M | re.I)
    return match.group(1).strip() if match else ""

def table_rows(block):
    rows = []
    for line in block.splitlines():
        line = line.strip()
        if line.startswith("|") and not re.search(r"\|[\s:-]{3,}\|", line):
            rows.append([cell.strip() for cell in line.strip("|").split("|")])
    return rows[1:] if rows else []

def checked(text, phrase):
    return bool(re.search(rf"^\s*-\s*\[x\]\s*{re.escape(phrase)}", text, re.I | re.M))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output-dir", default="scripts/drafts")
    args = parser.parse_args()

    source = Path(args.input)
    if not source.exists() or source.suffix.lower() != ".md":
        sys.exit(f"ERROR: File editorial tidak ditemukan atau bukan .md: {source}")
    if "editorial" not in source.resolve().parts:
        sys.exit("ERROR: Input harus berada di dalam folder editorial/.")
    raw = source.read_text(encoding="utf-8")

    if not APPROVAL.search(raw):
        sys.exit("BLOCKED: Status akhir belum APPROVED FOR SCRIPT.")
    if field(raw, "Keputusan").upper() != "LANJUT":
        sys.exit("BLOCKED: Keputusan editor harus LANJUT.")
    if not field(raw, "Angle utama") or not field(raw, "Hook pembuka"):
        sys.exit("BLOCKED: Angle utama dan Hook pembuka wajib diisi.")
    if not field(raw, "Disetujui oleh editor"):
        sys.exit("BLOCKED: Persetujuan editor belum diisi.")

    required_checks = [
        "Sumber utama sudah dibuka dan diperiksa.",
        "Fakta, laporan media, rumor, dan opini sudah dipisahkan.",
        "Angle dan hook disetujui editor.",
        "Konteks/koreksi editor sudah dimasukkan.",
        "Kebutuhan visual dan izin aset sudah diperiksa.",
    ]
    missing = [item for item in required_checks if not checked(raw, item)]
    if missing:
        sys.exit("BLOCKED: Checklist persetujuan belum lengkap: " + "; ".join(missing))

    sources = [r for r in table_rows(section(raw, "2. Pemeriksaan sumber")) if len(r) >= 4 and all(c.strip() for c in r[:4])]
    claims = [r for r in table_rows(section(raw, "4. Klaim dan batasan naskah")) if len(r) >= 3 and all(c.strip() for c in r[:3])]
    if not sources:
        sys.exit("BLOCKED: Isi semua kolom pada minimal satu baris tabel Pemeriksaan sumber.")
    if not claims:
        sys.exit("BLOCKED: Isi semua kolom pada minimal satu baris tabel Klaim dan batasan naskah.")

    topic = field(raw, "Judul kandidat") or source.stem
    safe = re.sub(r"[^a-zA-Z0-9_-]+", "-", source.stem).strip("-").lower()
    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    output = out_dir / f"{safe}-script-draft.md"
    fmt = field(raw, "Format yang dipertimbangkan").upper()
    lines = [
        f"# Draf Naskah — {topic}", "",
        "> DRAF KERJA. Bukan naskah terverifikasi atau izin publikasi. Sistem ini hanya menyusun bahan yang dimasukkan editor.", "",
        "## Brief editorial", "",
        f"- Kategori: {field(raw, 'Kategori')}",
        f"- Format: {fmt}",
        f"- Angle disetujui: {field(raw, 'Angle utama')}",
        f"- Hook editor: {field(raw, 'Hook pembuka')}",
        f"- Pesan utama: {field(raw, 'Pesan utama yang harus dibawa penonton')}",
        f"- Disetujui oleh: {field(raw, 'Disetujui oleh editor')}",
        "", "## Klaim dan sumber", "",
        "| Klaim | Sumber asli | Tanggal | Status |", "|---|---|---|---|",
    ]
    for row in sources:
        lines.append("| " + " | ".join((row + [""] * 4)[:4]) + " |")
    lines += ["", "## Klaim yang boleh disampaikan", "",
              "| Klaim | Status bukti | Cara penyampaian aman |", "|---|---|---|"]
    for row in claims:
        lines.append("| " + " | ".join((row + [""] * 3)[:3]) + " |")
    lines += [
        "", f"- Jangan klaim: {field(raw, 'Hal yang belum boleh diklaim')}",
        f"- Hindari sudut pandang: {field(raw, 'Sudut pandang yang harus dihindari')}",
        f"- Konteks/koreksi editor: {field(raw, 'Konteks/koreksi dari editor')}",
        "", "## Struktur narasi", "",
        f"**Hook:** {field(raw, 'Hook pembuka')}", "",
        f"**Konteks:** {field(raw, 'Apa yang membuat topik ini menarik bagi Bobotoh?') or '[Kembangkan dari sumber dan konteks editor.]'}", "",
        f"**Poin 1:** {field(raw, 'Poin pembahasan 1') or '[Isi dari klaim aman.]'}", "",
        f"**Poin 2:** {field(raw, 'Poin pembahasan 2') or '[Isi dari klaim aman.]'}", "",
        f"**Poin 3:** {field(raw, 'Poin pembahasan 3') or '[Isi dari klaim aman.]'}", "",
        f"**Pertanyaan/penutup:** {field(raw, 'Pertanyaan/pendapat editor yang ingin dimasukkan') or '[Simpulan sesuai bukti.]'}",
        f"**CTA:** {field(raw, 'CTA (opsional)') or '[Opsional]'}", "",
    ]
    if "SHORT" in fmt or "KEDUANYA" in fmt:
        lines += [
            "## Kerangka Shorts — 30–60 detik", "",
            "| Segmen | Durasi | Arahan |", "|---|---:|---|",
            "| Hook | 0–3 dtk | Hook editor, tanpa klaim tambahan. |",
            "| Konteks | 3–12 dtk | Mengapa isu ini penting bagi Bobotoh. |",
            "| Inti | 12–45 dtk | Poin terkuat; atribusikan laporan media/rumor. |",
            "| Penutup | 45–60 dtk | Simpulan terbatas pada bukti + CTA. |",
            "", "**Naskah narasi:**", "", "[Tulis dan periksa naskah final di sini.]", "",
        ]
    if "VIDEO" in fmt or "KEDUANYA" in fmt:
        lines += [
            "## Kerangka video panjang — 4–8 menit", "",
            "1. Hook dan pertanyaan utama (0:00–0:20)",
            "2. Konteks/kronologi bersumber (0:20–1:30)",
            "3. Pembahasan bukti dan poin utama (1:30–4:30)",
            "4. Analisis yang diberi label opini (4:30–6:30)",
            "5. Kesimpulan dan pertanyaan untuk Bobotoh (6:30–8:00)",
            "", "**Naskah narasi:**", "", "[Tulis dan periksa naskah final di sini.]", "",
        ]
    lines += [
        "## Visual", "", "| Bagian narasi | Visual | Sumber/izin |", "|---|---|---|",
    ]
    for row in table_rows(section(raw, "6. Kebutuhan visual")):
        lines.append("| " + " | ".join((row + [""] * 3)[:3]) + " |")
    lines += [
        "", "## QC sebelum render", "",
        "- [ ] Semua klaim dicocokkan dengan sumber asli dan tanggal.",
        "- [ ] Rumor, laporan media, dan opini diberi label/atribusi.",
        "- [ ] Kondisi pemain dan ketersediaan tidak diasumsikan.",
        "- [ ] Prediksi XI ditandai sebagai prediksi.",
        "- [ ] Statistik mencantumkan sumber dan periode.",
        "- [ ] Foto/video punya dasar penggunaan yang jelas.",
        "- [ ] Editor menyetujui naskah final sebelum render.",
        "", "**Status:** NEEDS SCRIPT WRITING & FACT CHECK — belum siap render/publikasi.", "",
    ]
    output.write_text("\n".join(lines), encoding="utf-8")
    print(f"OK: Draft scaffold dibuat: {output}")

if __name__ == "__main__":
    main()
