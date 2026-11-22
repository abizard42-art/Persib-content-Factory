#!/usr/bin/env python3
"""Create pending editorial selection files from the latest Persib news digest."""
from pathlib import Path
import re
import unicodedata

DIGEST = Path("research/daily/latest.md")
OUT = Path("editorial/inbox")
MAX_PER_SECTION = 5
MAX_TOTAL = 25

def slugify(value):
    value = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode().lower()
    value = re.sub(r"[^a-z0-9]+", "-", value).strip("-")
    return value[:72].strip("-") or "kandidat-persib"

def extract_field(block, label):
    match = re.search(rf"^-\s*{re.escape(label)}\s*:\s*(.*)$", block, re.M | re.I)
    return match.group(1).strip() if match else ""

def main():
    if not DIGEST.exists():
        raise SystemExit(f"Digest tidak ditemukan: {DIGEST}")
    raw = DIGEST.read_text(encoding="utf-8")
    sections = re.split(r"(?m)^##\s+", raw)
    created = 0
    skipped = 0
    for section in sections[1:]:
        lines = section.splitlines()
        section_name = lines[0].strip()
        if section_name.lower().startswith("catatan editor"):
            continue
        blocks = re.split(r"(?m)(?=^###\s+\d+\.\s+)", section)
        count = 0
        for block in blocks[1:]:
            if created >= MAX_TOTAL or count >= MAX_PER_SECTION:
                break
            heading = re.search(r"(?m)^###\s+\d+\.\s+(.+)$", block)
            if not heading:
                continue
            title = heading.group(1).strip()
            link = extract_field(block, "Tautan artikel asli")
            source = extract_field(block, "Media/sumber tertera")
            published = extract_field(block, "Waktu publikasi (sesuai feed)")
            if not link:
                continue
            filename = slugify(title) + ".md"
            target = OUT / filename
            if target.exists():
                skipped += 1
                count += 1
                continue
            category = section_name.upper()
            content = f"""# Editorial Selection — {title}

> DIBUAT OTOMATIS DARI NEWS MONITOR. Kandidat belum diverifikasi dan belum disetujui untuk naskah.

## 1. Identitas topik
- Tanggal seleksi (WIB):
- Link kandidat dari `research/daily/latest.md`: {link}
- Judul kandidat: {title}
- Kategori: {category}
- Format yang dipertimbangkan: SHORT / VIDEO 4–8 MENIT / KEDUANYA

## 2. Pemeriksaan sumber
| Klaim yang ingin dipakai | Sumber asli (bukan hanya cuplikan RSS) | Tanggal sumber | Status |
|---|---|---|---|
| [Periksa klaim dari artikel] | {source} — {link} | {published} | BELUM DICEK |

Status yang boleh dipakai:
- TERKONFIRMASI RESMI — ada pengumuman/konfirmasi langsung dari pihak berwenang.
- DILAPORKAN MEDIA — diberitakan media; atribusikan kepada media tersebut.
- RUMOR/BELUM PASTI — belum ada konfirmasi; jangan ditulis sebagai kepastian.
- ANALISIS/OPINI — interpretasi editorial, bukan fakta.

## 3. Keputusan editor
- Keputusan: [PILIH LANJUT / TUNDA / TOLAK]
- Alasan:
- Angle utama:
- Hook pembuka:
- Apa yang membuat topik ini menarik bagi Bobotoh?
- Konteks/koreksi dari editor:

## 4. Klaim dan batasan naskah
| Klaim/fakta yang boleh disampaikan | Status bukti | Cara penyampaian yang aman |
|---|---|---|
| | | |

- Hal yang belum boleh diklaim:
- Sudut pandang yang harus dihindari:
- Nama pemain/tim/tanggal yang perlu dicek ulang:

## 5. Arah konten
- Pesan utama yang harus dibawa penonton:
- Poin pembahasan 1:
- Poin pembahasan 2:
- Poin pembahasan 3:
- Pertanyaan/pendapat editor yang ingin dimasukkan:
- CTA (opsional):

## 6. Kebutuhan visual
| Bagian narasi | Visual yang dibutuhkan | Sumber/izin/status |
|---|---|---|
| | | |

Checklist:
- [ ] Foto/video punya sumber dan dasar penggunaan yang jelas.
- [ ] Statistik punya sumber dan periode yang jelas.
- [ ] Prediksi starting XI diberi label prediksi, bukan susunan resmi.
- [ ] Diagram taktik diberi label sebagai ilustrasi analisis bila bukan data resmi.
- [ ] Chibi host memakai identitas visual channel yang konsisten.

## 7. Gerbang persetujuan
- [ ] Sumber utama sudah dibuka dan diperiksa.
- [ ] Fakta, laporan media, rumor, dan opini sudah dipisahkan.
- [ ] Angle dan hook disetujui editor.
- [ ] Konteks/koreksi editor sudah dimasukkan.
- [ ] Kebutuhan visual dan izin aset sudah diperiksa.

**Status akhir:** PENDING

- Disetujui oleh editor:
- Tanggal persetujuan (WIB):
- Catatan sebelum masuk tahap naskah:

---

**Aturan:** File ini hanya kandidat editorial. Tidak boleh masuk Script Builder sebelum editor mengubah keputusan menjadi LANJUT, mengisi semua pemeriksaan, mencentang checklist, dan menetapkan status APPROVED FOR SCRIPT.
"""
            OUT.mkdir(parents=True, exist_ok=True)
            target.write_text(content, encoding="utf-8")
            created += 1
            count += 1
    print(f"OK: {created} file kandidat dibuat; {skipped} sudah ada; folder: {OUT}")

if __name__ == "__main__":
    main()
