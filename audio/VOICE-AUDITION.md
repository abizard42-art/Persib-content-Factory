# Paket Audisi Voice Persib

Tujuan: membandingkan suara Orus, Algieba, dan Puck dengan **teks, bahasa, dan konteks yang sama**. Jangan tetapkan voice final sebelum editor mendengarkan hasilnya.

## Naskah uji identik

> Bobotoh, tarik napas dulu! Persib bukan cuma soal siapa yang paling terkenal, tapi siapa yang paling siap bertarung di lapangan. Dalam sepak bola, satu keputusan kecil bisa mengubah jalannya pertandingan. Karena itu, kita nggak cukup cuma lihat nama di atas kertas. Kita cek kondisi pemain, baca kebutuhan taktik, lalu berani menyampaikan analisis dengan alasan yang jelas. Ini Persib, ini waktunya kita bahas dengan kepala dingin… tapi semangat tetap membara!

## Kandidat yang dibandingkan

| Urutan | Voice ID | Fokus penilaian |
|---|---|---|
| 1 | `id-ID-Chirp3-HD-Orus` | Tegas, berwibawa, ekspresif |
| 2 | `id-ID-Chirp3-HD-Algieba` | Tegas, artikulasi, ritme |
| 3 | `id-ID-Chirp3-HD-Puck` | Lincah, natural, conversational |

WaveNet B tetap menjadi opsi cadangan, bukan bagian dari audisi pertama.

## Rubrik penilaian editor

Beri skor 1–5 untuk setiap suara:

- [ ] Pengucapan Bahasa Indonesia jelas
- [ ] Nama dan istilah sepak bola terdengar natural
- [ ] Energi terasa seperti presenter Bobotoh, bukan pembaca berita datar
- [ ] Jeda dan penekanan enak didengar
- [ ] Tidak terdengar berlebihan atau seperti berteriak terus
- [ ] Paling nyaman didengar untuk video 4–8 menit

**Pilihan editor:** PENDING

**Catatan editor:** belum diisi.

## Status teknis dan biaya

- Belum ada audio yang dibuat.
- Belum ada kredensial Google Cloud yang disimpan.
- Google Cloud Text-to-Speech mensyaratkan billing aktif. Kuota gratis bulanan bukan berarti API dapat dipakai tanpa billing; penggunaan di atas kuota dapat ditagihkan.
- Jangan aktifkan billing, menambahkan metode pembayaran, atau menjalankan request TTS berbayar tanpa persetujuan eksplisit editor.
- Setelah akses dan batas biaya disetujui, buat tiga MP3 dari naskah identik, simpan sebagai artefak audisi, lalu minta editor memilih satu suara.
