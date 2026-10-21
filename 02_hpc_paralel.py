"""
STUDI KASUS 2 - HPC untuk masalah lokal
Kasus : Simulasi Monte Carlo risiko banjir (curah hujan x kejenuhan tanah)
        untuk sebuah DAS. Semakin banyak simulasi, semakin akurat -> butuh komputasi paralel.
Alur  : jalankan serial vs paralel (multiprocessing), bandingkan speedup.
Di klaster HPC sungguhan: ganti Pool dengan mpi4py / SLURM job array.
"""
import time, numpy as np
from multiprocessing import Pool, cpu_count

AMBANG_BANJIR = 120.0   # mm limpasan (angka ilustrasi)

def simulasi(args):
    seed, n = args
    rng = np.random.default_rng(seed)
    hujan = rng.gamma(shape=2.0, scale=60.0, size=n)   # mm/hari
    jenuh = rng.uniform(0.3, 1.0, size=n)              # kejenuhan tanah
    return int(((hujan * jenuh) > AMBANG_BANJIR).sum())

if __name__ == "__main__":
    TOTAL, CHUNK = 40_000_000, 2_000_000
    tugas = [(i, CHUNK) for i in range(TOTAL // CHUNK)]

    t0 = time.perf_counter()
    serial = sum(simulasi(t) for t in tugas)
    t_serial = time.perf_counter() - t0

    t0 = time.perf_counter()
    with Pool(cpu_count()) as p:
        paralel = sum(p.map(simulasi, tugas))
    t_par = time.perf_counter() - t0

    print(f"Probabilitas banjir harian : {serial/TOTAL*100:.2f} %")
    print(f"Hasil sama (serial==paralel): {serial == paralel}")
    print(f"Serial {t_serial:.2f}s | Paralel {t_par:.2f}s ({cpu_count()} core) "
          f"| Speedup {t_serial/t_par:.2f}x")
