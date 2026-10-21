# 3. Career and Competition in Industrial Era with GIS
**Studi kasus:** Memilih lokasi gudang terbaik dari 8 kandidat.

## Alur
1. Membuat 60 desa (koordinat dan jumlah penduduk) dan 8 kandidat lokasi
2. Menghitung jarak dengan rumus Haversine
3. Menjumlahkan penduduk dalam radius 15 km
4. Skor = 70% cakupan penduduk + 30% kedekatan ke jalan utama
5. Peringkat kandidat dan peta lokasi terpilih

## Menjalankan
```bash
pip install numpy pandas matplotlib
python 03_gis_pemilihan_lokasi.py
```
Output: tabel peringkat di terminal dan peta `03_hasil.png`.

## Pengembangan
Gunakan data nyata dengan `geopandas.read_file("desa.shp")`, operasi `buffer` dan `sjoin`, serta jarak tempuh jaringan jalan (bukan jarak lurus).
