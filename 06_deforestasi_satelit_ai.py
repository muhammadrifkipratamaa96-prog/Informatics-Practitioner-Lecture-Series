"""
STUDI KASUS 6 - Penyebab deforestasi dari citra satelit + AI
Kasus : Sistem peringatan dini menemukan area hutan hilang. Apa penyebabnya?
        Klasifikasikan tiap peringatan: perkebunan, pertambangan, pertanian kecil,
        kebakaran, atau pembangunan jalan.
Fitur : diambil dari citra satelit (di sini disimulasikan):
        dNDVI (perubahan kehijauan), dNBR (indikator terbakar), luas, kekompakan
        bentuk, jarak ke jalan.
Upgrade nyata: ganti fitur ini dengan potongan citra Sentinel-2 + CNN (PyTorch).
"""
import numpy as np, pandas as pd
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, ConfusionMatrixDisplay

rng = np.random.default_rng(11)
# kelas: (dNDVI, dNBR, luas_ha, kekompakan, jarak_jalan_km)
profil = {
    "perkebunan":       (-0.45, 0.10, 60, 0.85, 3.0),
    "pertambangan":     (-0.60, 0.05, 25, 0.60, 5.0),
    "pertanian_kecil":  (-0.30, 0.08, 3,  0.70, 1.5),
    "kebakaran":        (-0.40, 0.55, 40, 0.30, 4.0),
    "jalan":            (-0.35, 0.06, 6,  0.10, 0.2),
}
rows = []
for nama, (dn, db, lh, kk, jj) in profil.items():
    for _ in range(300):
        rows.append([rng.normal(dn, 0.08), rng.normal(db, 0.06),
                     abs(rng.normal(lh, lh*0.4)), np.clip(rng.normal(kk, 0.1), 0, 1),
                     abs(rng.normal(jj, jj*0.4+0.1)), nama])
df = pd.DataFrame(rows, columns=["dNDVI", "dNBR", "luas_ha", "kekompakan", "jarak_jalan_km", "penyebab"])

X, y = df.drop(columns="penyebab"), df["penyebab"]
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.25, random_state=0, stratify=y)
m = RandomForestClassifier(n_estimators=300, random_state=0).fit(Xtr, ytr)
print(classification_report(yte, m.predict(Xte)))

ConfusionMatrixDisplay.from_estimator(m, Xte, yte, xticks_rotation=30, colorbar=False)
plt.tight_layout(); plt.savefig("06_hasil.png", dpi=120)

baru = pd.DataFrame([[-0.42, 0.52, 35, 0.28, 3.5]], columns=X.columns)
print("Peringatan baru ->", m.predict(baru)[0], "| peluang:",
      dict(zip(m.classes_, m.predict_proba(baru)[0].round(2))))
