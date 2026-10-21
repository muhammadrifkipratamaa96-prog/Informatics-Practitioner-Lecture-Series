"""
STUDI KASUS 5 - HCI & Data Visualization
Kasus : Uji kegunaan (usability) dua desain aplikasi KRS online: Desain A (lama)
        vs Desain B (baru), pada 20 mahasiswa.
Metrik: skor SUS, waktu menyelesaikan tugas, jumlah kesalahan.
Alur  : hitung SUS -> uji statistik -> dasbor visual yang mudah dibaca.
"""
import numpy as np
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy import stats

rng = np.random.default_rng(3)
N = 20

def sus_score(jawaban):
    """jawaban: array (N,10) skala 1-5. Item ganjil: (x-1), genap: (5-x). Total x2.5"""
    j = np.asarray(jawaban)
    ganjil, genap = j[:, 0::2] - 1, 5 - j[:, 1::2]
    return (ganjil.sum(1) + genap.sum(1)) * 2.5

def survei(bagus):
    base = np.array([4, 2, 4, 2, 4, 2, 4, 2, 4, 2]) if bagus else np.array([3, 3, 3, 3, 3, 3, 3, 3, 3, 3])
    return np.clip(base + rng.integers(-1, 2, (N, 10)), 1, 5)

sus_a, sus_b = sus_score(survei(False)), sus_score(survei(True))
waktu_a, waktu_b = rng.normal(95, 15, N), rng.normal(65, 12, N)      # detik
salah_a, salah_b = rng.poisson(2.5, N), rng.poisson(0.9, N)

t, p = stats.ttest_ind(sus_b, sus_a)
print(f"SUS A = {sus_a.mean():.1f} | SUS B = {sus_b.mean():.1f} (>68 dianggap di atas rata-rata)")
print(f"Uji-t: t={t:.2f}, p={p:.4f} -> {'berbeda nyata' if p < .05 else 'tidak berbeda nyata'}")

fig, ax = plt.subplots(1, 3, figsize=(13, 4))
for a, (jud, da, db, yl) in zip(ax, [("Skor SUS", sus_a, sus_b, "Skor (0-100)"),
                                     ("Waktu tugas", waktu_a, waktu_b, "Detik"),
                                     ("Jumlah kesalahan", salah_a, salah_b, "Kesalahan")]):
    bp = a.boxplot([da, db], tick_labels=["Desain A", "Desain B"], patch_artist=True)
    for patch, c in zip(bp["boxes"], ["#d9534f", "#5cb85c"]):
        patch.set_facecolor(c)
    a.set_title(jud); a.set_ylabel(yl)
ax[0].axhline(68, ls="--", color="gray"); ax[0].text(1.55, 69, "rata-rata 68", fontsize=8)
fig.suptitle("Perbandingan usability KRS online: Desain A vs B"); plt.tight_layout()
plt.savefig("05_hasil.png", dpi=120)
