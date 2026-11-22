# Audisi Voice Persib — Jalur Full Free

Target: suara narasi Bahasa Indonesia tanpa API berbayar, tanpa billing cloud, dan tanpa langganan.

## Engine yang dipakai

**Laras TTS v0.2.1** — https://github.com/Urdemonlord/laras-tts

- Self-hosted, CPU-first, tersedia sebagai image Docker publik.
- Kode Laras berlisensi MIT atau Apache-2.0.
- Bobot Pocket TTS Indonesian oleh anak10thn berlisensi CC BY 4.0; atribusi wajib dipertahankan.
- Referensi suara bawaan workflow diambil dari Common Voice Indonesia dan dinyatakan CC0 oleh proyek Laras.
- Tidak memerlukan API key TTS berbayar atau akun billing.
- Workflow memakai GitHub Actions runner dan menyimpan hasil sebagai artifact selama 7 hari.

## Cara menjalankan audisi (workflow 03)

1. Buka tab **Actions** di repository Persib Content Factory.
2. Pilih **03 - Generate Persib Voice Audition**.
3. Tekan **Run workflow** pada branch `main`.
4. Biarkan kolom teks kosong untuk memakai naskah default, atau isi naskah sendiri (maksimal 3.000 karakter).
5. Setelah workflow selesai, buka hasil run dan unduh artifact **persib-voice-audition**.
6. Dengarkan file WAV di dalam ZIP.

Workflow memakai Laras TTS v0.2.1 yang dipin ke tag rilis, mengunduh model publik, memverifikasi SHA-256 setiap berkas, lalu membuat WAV. Audisi awal telah didengarkan dan disetujui editor sebagai baseline suara. Workflow produksi narasi terpisah tersedia di `.github/workflows/04-generate-narration.yml`; workflow produksi itu belum dianggap teruji sampai dijalankan dan hasil WAV diperiksa.

## Naskah uji default

> Bobotoh, tarik napas dulu! Persib bukan cuma soal siapa yang paling terkenal, tapi siapa yang paling siap bertarung di lapangan. Dalam sepak bola, satu keputusan kecil bisa mengubah jalannya pertandingan. Karena itu, kita nggak cukup cuma lihat nama di atas kertas. Kita cek kondisi pemain, baca kebutuhan taktik, lalu berani menyampaikan analisis dengan alasan yang jelas. Ini Persib, ini waktunya kita bahas dengan kepala dingin, tapi semangat tetap membara!

## Catatan suara

- Audisi pertama memakai rekaman referensi Common Voice CC0 yang disediakan proyek Laras. Karakter suara yang keluar akan mengikuti rekaman referensi itu; belum tentu cocok dengan target presenter pria yang kita inginkan.
- Kalau karakter suaranya belum cocok, langkah berikutnya adalah memakai rekaman referensi milik sendiri atau rekaman orang yang memberi izin jelas. Jangan mengkloning suara orang tanpa persetujuan.
- Workflow memakai satu take untuk pratinjau cepat. Kualitas pengucapan nama pemain dan istilah sepak bola tetap harus diperiksa.
- Engine dapat menghasilkan suara yang terdengar natural, tetapi model punya keterbatasan artikulasi pada beberapa gugus konsonan dan kosakata.

## Rubrik penilaian editor

Beri skor 1–5 setelah audio berhasil dibuat:

- [ ] Pengucapan Bahasa Indonesia jelas
- [ ] Nama pemain dan istilah sepak bola terdengar natural
- [ ] Energi terasa seperti presenter Bobotoh, bukan pembaca berita datar
- [ ] Jeda dan penekanan enak didengar
- [ ] Tidak terdengar berlebihan atau seperti berteriak terus
- [ ] Nyaman didengar untuk video 4–8 menit

**Pilihan editor:** APPROVED — baseline suara Laras TTS disetujui setelah didengarkan oleh editor.

**Catatan editor:** gunakan karakter suara hasil audisi sebagai baseline. Evaluasi ulang hanya jika ada masalah pengucapan atau editor meminta perubahan.

## Lisensi dan biaya

1. Sertakan atribusi: **“Pocket TTS Indonesian oleh anak10thn, CC-BY-4.0”** beserta tautan https://huggingface.co/anak10thn/pocket-tts-indonesian.
2. Lisensi kode Laras tidak menggantikan lisensi bobot model.
3. Tidak memakai layanan TTS cloud berbayar atau billing cloud.
4. GitHub Actions pada repo publik digunakan untuk proses audisi; artifact hasil audisi disimpan 7 hari lalu kedaluwarsa.
5. Jangan aktifkan layanan berbayar atau mengubah workflow ke provider berbayar tanpa persetujuan eksplisit editor.


## Produksi narasi untuk video

Gunakan workflow **04 - Generate Persib Narration Audio** untuk naskah final:
1. Buka repository → Actions → 04 - Generate Persib Narration Audio.
2. Pilih **Run workflow** pada branch `main`.
3. Tempel naskah final ke kolom `narration_text` (maksimal 10.000 karakter).
4. Setelah berhasil, unduh artifact `persib-narration-audio`.
5. Paket berisi `persib-narration.wav`, `narration.txt`, `metadata.json`, `credits.txt`, dan header respons TTS.
6. Dengarkan audio, cek nama pemain/istilah, jeda, volume, dan potongan kalimat sebelum dipakai dalam video.

Audio yang dihasilkan belum otomatis menjadi video dan bukan izin publikasi. Workflow ini belum diuji end-to-end di GitHub Actions. Artifact disimpan 7 hari; unduh dan simpan salinan sendiri.
