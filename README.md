# Persib Content Factory

Workflow produksi konten Persib Bandung berbasis riset, keputusan editorial manusia, dan render hemat biaya.

## Prinsip utama
- AI membantu mengumpulkan dan merangkum informasi; keputusan editorial tetap di tangan pemilik channel.
- Fakta, laporan media, rumor, dan analisis dipisahkan dengan jelas.
- Tidak ada produksi final atau publikasi tanpa persetujuan editorial.
- Gunakan foto/video hanya sesuai izin, lisensi, atau ketentuan penggunaan yang berlaku.
- Workflow proyek ini terpisah dari AI Content Factory, Peta Sunyi, dan Sejarah Dunia.

## Alur produksi
1. **Research** — buat brief pertandingan/topik dari sumber yang dicatat.
2. **Editorial** — pemilik channel mengoreksi dan menyetujui angle, prediksi, dan klaim.
3. **Content** — jalankan `02 - Build Script Draft` hanya untuk file editorial berstatus `APPROVED FOR SCRIPT`; sistem menyusun kerangka draf dari bahan editor.
4. **Visual & Render** — komposisi foto berizin, grafis taktik, dan presenter chibi.
5. **Quality Control** — cek fakta, visual, audio, hak penggunaan aset, dan durasi.
6. **Publish** — upload/penjadwalan hanya setelah persetujuan manual.

## Struktur awal
- `config/`: konfigurasi channel, sumber, dan produksi.
- `research/inbox/`: brief riset yang baru dibuat.
- `editorial/pending/`: bahan yang menunggu keputusan.
- `editorial/approved/`: keputusan editorial yang disetujui.
- `scripts/drafts/`: kerangka draf yang dihasilkan dari keputusan editorial.
- `assets/`: aset dengan catatan sumber dan izin.
- `.github/workflows/`: workflow manual.

## Mulai
Buka tab **Actions**, pilih **01 - Create Research Brief**, lalu tekan **Run workflow**. Workflow ini hanya membuat kerangka brief; belum melakukan scraping atau menyimpulkan berita otomatis.

## Status
Fondasi repository. News monitor mengelompokkan kandidat berdasarkan kata kunci judul, menghapus duplikasi judul lintas feed, dan menampilkan papan kandidat editorial dengan skor heuristik 1–5. Skor bukan verifikasi atau penilaian kebenaran. Editor tetap memilih topik, angle, dan klaim secara manual. Script Builder v1 menyusun kerangka dan tabel klaim/sumber; ia tidak menambah fakta, memverifikasi sumber, atau mengizinkan publikasi otomatis. Renderer dan publisher akan dibangun bertahap.
