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
5. Voice — tempel naskah final ke workflow 04 - Generate Persib Narration Audio; unduh artifact persib-narration-audio berisi WAV, teks, metadata, dan atribusi model. Dengarkan dan QC sebelum dipakai.
6. Visual & Render — gabungkan audio WAV dengan komposisi foto berizin, grafis taktik, dan presenter chibi.
7. Quality Control — cek fakta, visual, audio, hak penggunaan aset, dan durasi.
8. Publish — upload/penjadwalan hanya setelah persetujuan manual.

## Struktur awal
- config/: konfigurasi channel, sumber, dan produksi.
- audio/VOICE-AUDITION.md: jalur audisi TTS Bahasa Indonesia self-hosted yang ditargetkan full free, tanpa billing cloud.
- .github/workflows/03-generate-voice-audition.yml: workflow audisi awal Laras TTS.
- .github/workflows/04-generate-narration.yml: workflow manual untuk mengubah naskah final menjadi paket audio narasi WAV siap masuk tahap render; memakai Laras TTS CPU dan tanpa API TTS berbayar.
- audio/audition-script.txt: naskah default audisi suara Persib.
- audio/VOICE-AUDITION.md: catatan audisi dan persetujuan baseline suara Laras TTS.
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
Fondasi repository. News monitor mengelompokkan kandidat berdasarkan kata kunci judul, menghapus duplikasi judul lintas feed, menampilkan papan kandidat editorial dengan skor heuristik 1–5, dan membuat file inbox editorial otomatis. Skor bukan verifikasi atau penilaian kebenaran. Editor tetap memilih topik, angle, dan klaim secara manual. Script Builder v1 menyusun kerangka dan tabel klaim/sumber; ia tidak menambah fakta, memverifikasi sumber, atau mengizinkan publikasi otomatis. Workflow pembuat audio narasi sudah ditambahkan tetapi belum diuji melalui GitHub Actions. Master chibi tersedia di `assets/chibi/master-sheet.svg`. Workflow `Prepare Chibi Expression Assets` memisahkan enam pose menjadi aset SVG dan PNG transparan di `assets/chibi/expressions/`; workflow ini sudah disiapkan tetapi belum dijalankan untuk verifikasi. Renderer video chibi dan publisher masih tahap berikutnya.

## Render animasi Starting XI
Prototype renderer FFmpeg tersedia di `scripts/render_starting_xi.py`. Data contoh ada di `visual/demo-lineup.json`. Renderer membuat video MP4 vertikal 1080×1920 dengan reveal kartu pemain satu per satu, nomor/nama/posisi, dan penanda posisi di lapangan. Foto pemain dapat ditambahkan melalui properti `photo` pada tiap pemain jika file foto berizin tersedia di repository/runner.

Untuk mencoba:
1. Buka tab **Actions**.
2. Pilih **Render Starting XI Reveal**.
3. Jalankan workflow dengan input `visual/demo-lineup.json`.
4. Setelah selesai, unduh artifact `persib-starting-xi-reveal`.

Data contoh hanya placeholder, bukan susunan pemain Persib. Ganti dengan 11 pemain yang sudah diverifikasi sebelum dipakai. Foto pemain harus punya izin/lisensi yang sesuai. Workflow dan renderer baru ditambahkan; belum dianggap teruji sampai ada run Actions yang berhasil dan hasil MP4 diperiksa.
