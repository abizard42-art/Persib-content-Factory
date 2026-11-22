# Persib Content Factory

Workflow produksi konten Persib Bandung berbasis riset, keputusan editorial manusia, dan render hemat biaya.

## Prinsip utama
- AI membantu mengumpulkan dan merangkum informasi; keputusan editorial tetap di tangan pemilik channel.
- Fakta, laporan media, rumor, dan analisis dipisahkan dengan jelas.
- Tidak ada produksi final atau publikasi tanpa persetujuan editorial.
- Gunakan foto/video hanya sesuai izin, lisensi, atau ketentuan penggunaan yang berlaku.
- Workflow proyek ini terpisah dari AI Content Factory, Peta Sunyi, dan Sejarah Dunia.

## Alur produksi
1. Research — News Monitor mengumpulkan tautan dan membuat digest otomatis.
2. Editorial inbox — setiap jadwal monitor, sistem membuat file kandidat PENDING di editorial/inbox/ (maksimal 5 kandidat per kategori dan 25 total per run; kandidat yang sudah ada dilewati).
3. Editorial — topik berita/transfer melalui seleksi editor; prediksi Starting XI memakai jalur riset cepat oleh asisten sesuai editorial/STARTING-XI-PLAYBOOK.md.
4. Content — 02 - Build Script Draft hanya berjalan untuk file editorial berstatus APPROVED FOR SCRIPT; sistem menyusun kerangka draf dari bahan editor.
5. Visual & Render — komposisi foto berizin, grafis taktik, dan presenter chibi.
6. Quality Control — cek fakta, visual, audio, hak penggunaan aset, dan durasi.
7. Publish — upload/penjadwalan hanya setelah persetujuan manual.

## Struktur awal
- config/: konfigurasi channel, sumber, dan produksi.
- audio/VOICE-AUDITION.md: naskah identik dan rubrik untuk membandingkan kandidat suara; belum ada audio yang dibuat.
- research/inbox/: brief riset yang baru dibuat.
- editorial/inbox/: kandidat berita yang dibuat otomatis dan masih berstatus PENDING.
- editorial/pending/: bahan yang sedang diperiksa editor.
- editorial/approved/: keputusan editorial yang disetujui.
- editorial/STARTING-XI-PLAYBOOK.md: standar riset dan format prediksi starting XI.
- scripts/drafts/: kerangka draf yang dihasilkan dari keputusan editorial.
- assets/: aset dengan catatan sumber dan izin.
- .github/workflows/: workflow otomatis dan manual.

## Mulai
Buka tab Actions, pilih 00 - Auto News Monitor untuk menjalankan pengumpulan berita manual, atau tunggu jadwal otomatis. Prediksi Starting XI diminta langsung kepada asisten agar status pemain dan jadwal dapat diperiksa dari sumber terbaru.

## Status
Fondasi repository. News monitor mengelompokkan kandidat berdasarkan kata kunci judul, menghapus duplikasi judul lintas feed, menampilkan papan kandidat editorial dengan skor heuristik 1–5, dan membuat file inbox editorial otomatis. Skor bukan verifikasi atau penilaian kebenaran. Editor tetap memilih topik, angle, dan klaim secara manual. Script Builder v1 menyusun kerangka dan tabel klaim/sumber; ia tidak menambah fakta, memverifikasi sumber, atau mengizinkan publikasi otomatis. Renderer dan publisher akan dibangun bertahap.
