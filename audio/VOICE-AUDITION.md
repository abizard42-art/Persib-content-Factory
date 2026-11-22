# Audisi Voice Persib — Jalur Full Free

Target: suara narasi Bahasa Indonesia tanpa API berbayar, tanpa billing cloud, dan tanpa langganan.

## Engine kandidat

**Laras TTS** — https://github.com/Urdemonlord/laras-tts

- Engine self-hosted, CPU-first, kode berlisensi Apache-2.0.
- Model kandidat: `anak10thn/pocket-tts-indonesian`, model 6-layer student.
- Bobot model berlisensi CC BY 4.0; atribusi wajib dipertahankan.
- Proyek Laras mendokumentasikan contoh referensi suara Common Voice Indonesia berlisensi CC0.
- Tidak perlu API key TTS berbayar atau akun billing.
- Status: kandidat riset; belum diintegrasikan ke repo Persib dan belum diuji di GitHub Actions.

## Naskah uji

> Bobotoh, tarik napas dulu! Persib bukan cuma soal siapa yang paling terkenal, tapi siapa yang paling siap bertarung di lapangan. Dalam sepak bola, satu keputusan kecil bisa mengubah jalannya pertandingan. Karena itu, kita nggak cukup cuma lihat nama di atas kertas. Kita cek kondisi pemain, baca kebutuhan taktik, lalu berani menyampaikan analisis dengan alasan yang jelas. Ini Persib, ini waktunya kita bahas dengan kepala dingin… tapi semangat tetap membara!

## Rubrik penilaian editor

Beri skor 1–5 setelah audio berhasil dibuat:

- [ ] Pengucapan Bahasa Indonesia jelas
- [ ] Nama pemain dan istilah sepak bola terdengar natural
- [ ] Energi terasa seperti presenter Bobotoh, bukan pembaca berita datar
- [ ] Jeda dan penekanan enak didengar
- [ ] Tidak terdengar berlebihan atau seperti berteriak terus
- [ ] Nyaman didengar untuk video 4–8 menit

**Pilihan editor:** PENDING

**Catatan editor:** belum diisi.

## Catatan lisensi dan biaya

1. Lisensi kode engine dan lisensi bobot model adalah dua hal berbeda. Cantumkan atribusi CC BY 4.0 untuk model.
2. Gunakan hanya rekaman referensi suara yang lisensinya jelas; jangan memakai suara orang tanpa izin.
3. Repo TTS Indonesia Gratis lain yang ditemukan menyatakan “DO NOT USE FOR COMMERCIAL PURPOSES”, jadi tidak dipilih untuk channel yang berpotensi dimonetisasi.
4. Jalur ini tidak memakai layanan TTS cloud berbayar. Tetap periksa batas penggunaan GitHub Actions dan penyimpanan artefak; jangan mengaktifkan layanan berbayar.
5. Belum ada audio yang dihasilkan dan belum ada klaim kualitas sebelum tes nyata.
