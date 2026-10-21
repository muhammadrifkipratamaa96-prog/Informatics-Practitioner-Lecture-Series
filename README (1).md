# 1. Make Sense of Data with Analysis and AI
**Studi kasus:** Prediksi pelanggan toko online UMKM yang berisiko berhenti (churn).

## Alur
1. Membuat data pelanggan sintetis (lama langganan, transaksi, belanja, keluhan)
2. Membersihkan nilai kosong (diisi median)
3. Eksplorasi: bandingkan pelanggan yang churn dan yang tidak
4. Melatih model Random Forest
5. Menampilkan faktor paling berpengaruh dan daftar pelanggan berisiko tinggi

## Menjalankan
```bash
pip install numpy pandas scikit-learn matplotlib
python 01_analisis_data_ai.py
```
Output: laporan di terminal dan grafik `01_hasil.png`.

## Hasil contoh
Akurasi sekitar 83%. Recall untuk kelas churn masih rendah (~29%) karena kelasnya jarang. Ini bisa jadi bahan latihan (class weight, SMOTE).

## Pengembangan
Pakai dataset churn asli (misalnya dari Kaggle) dan tangani ketidakseimbangan kelas.
