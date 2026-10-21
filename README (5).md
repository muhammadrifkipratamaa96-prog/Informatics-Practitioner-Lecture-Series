# 5. Human-Computer Interaction & Data Visualization
**Studi kasus:** Uji kegunaan (usability) aplikasi KRS online, Desain A (lama) vs Desain B (baru), pada 20 mahasiswa.

## Alur
1. Mensimulasikan jawaban kuesioner SUS (10 pertanyaan, skala 1-5)
2. Menghitung skor SUS tiap responden
3. Uji-t antar desain
4. Dasbor boxplot: skor SUS, waktu menyelesaikan tugas, jumlah kesalahan

## Menjalankan
```bash
pip install numpy matplotlib scipy
python 05_hci_visualisasi_data.py
```
Output: ringkasan statistik di terminal dan dasbor `05_hasil.png`.

## Acuan
Skor SUS di atas 68 dianggap di atas rata-rata.

## Pengembangan
Ganti data sintetis dengan hasil survei nyata dan tambahkan visualisasi interaktif (Plotly).
