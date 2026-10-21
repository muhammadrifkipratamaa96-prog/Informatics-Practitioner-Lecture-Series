# 2. Bridging Global Infrastructure to Address Local Challenge with HPC
**Studi kasus:** Simulasi Monte Carlo risiko banjir di satu DAS (curah hujan x kejenuhan tanah).

## Alur
1. Membagi 40 juta simulasi menjadi 20 potongan
2. Menjalankan secara serial, lalu paralel (`multiprocessing.Pool`)
3. Membandingkan waktu dan memastikan hasil keduanya identik

## Menjalankan
```bash
pip install numpy
python 02_hpc_paralel.py
```
Output: probabilitas banjir harian, waktu serial vs paralel, dan speedup.

## Catatan
- Speedup hanya terlihat di mesin multi-core. Pada uji dengan 1 core hasilnya 0,91x.
- Ambang banjir (120 mm) adalah angka ilustrasi.

## Pengembangan
Di klaster HPC sungguhan, ganti `Pool` dengan `mpi4py` atau SLURM job array, lalu ukur speedup di 1, 2, 4, 8, ... core.
