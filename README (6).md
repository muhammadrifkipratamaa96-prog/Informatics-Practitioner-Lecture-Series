# 6. Attributing Direct Drivers to Deforestation Alerts with Satellite Imagery and AI
**Studi kasus:** Peringatan dini menunjukkan di mana hutan hilang, tetapi tidak penyebabnya. Klasifikasikan penyebabnya.

## Kelas penyebab
Perkebunan, pertambangan, pertanian kecil, kebakaran, pembangunan jalan.

## Fitur (disimulasikan dari citra satelit)
- `dNDVI`: perubahan kehijauan vegetasi
- `dNBR`: indikator area terbakar
- `luas_ha`, `kekompakan` (bentuk area), `jarak_jalan_km`

## Menjalankan
```bash
pip install numpy pandas scikit-learn matplotlib
python 06_deforestasi_satelit_ai.py
```
Output: laporan klasifikasi, confusion matrix `06_hasil.png`, dan prediksi satu peringatan baru.

## Peringatan
Akurasi ~99% karena data sintetis mudah dipisahkan. Pada data satelit nyata hasilnya hampir pasti lebih rendah.

## Pengembangan
Ganti fitur dengan potongan citra Sentinel-2 dan model CNN (PyTorch/TensorFlow), dengan label dari data Global Forest Watch.
