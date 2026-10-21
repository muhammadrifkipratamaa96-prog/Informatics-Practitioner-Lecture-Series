"""
STUDI KASUS 4 - Introduction to Machine Learning
Kasus : Memprediksi mahasiswa berisiko tidak lulus mata kuliah dari kehadiran,
        nilai tugas, dan jam belajar (supervised learning - klasifikasi).
Alur  : bandingkan 3 algoritma dengan cross-validation -> evaluasi model terbaik.
"""
import numpy as np, pandas as pd
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import ConfusionMatrixDisplay, accuracy_score

rng = np.random.default_rng(1)
n = 600
df = pd.DataFrame({"kehadiran_pct": rng.uniform(40, 100, n),
                   "nilai_tugas": rng.normal(70, 12, n).clip(0, 100),
                   "jam_belajar_minggu": rng.gamma(3, 2.5, n)})
skor = 0.04*df.kehadiran_pct + 0.05*df.nilai_tugas + 0.12*df.jam_belajar_minggu + rng.normal(0, 0.8, n)
df["lulus"] = (skor > np.median(skor) - 0.3).astype(int)

X, y = df.drop(columns="lulus"), df["lulus"]
kandidat = {
    "Logistic Regression": make_pipeline(StandardScaler(), LogisticRegression()),
    "Decision Tree": DecisionTreeClassifier(max_depth=4, random_state=0),
    "Random Forest": RandomForestClassifier(n_estimators=200, random_state=0),
}
hasil = {}
for nama, m in kandidat.items():
    s = cross_val_score(m, X, y, cv=5)
    hasil[nama] = s.mean()
    print(f"{nama:20s} akurasi CV: {s.mean():.3f} (+/- {s.std():.3f})")

terbaik = max(hasil, key=hasil.get)
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.25, random_state=0)
m = kandidat[terbaik].fit(Xtr, ytr)
print(f"\nModel terbaik: {terbaik} | akurasi uji: {accuracy_score(yte, m.predict(Xte)):.3f}")
ConfusionMatrixDisplay.from_estimator(m, Xte, yte, display_labels=["Tidak lulus", "Lulus"])
plt.title(terbaik); plt.savefig("04_hasil.png", dpi=120)

mhs_baru = pd.DataFrame([[55, 60, 3]], columns=X.columns)
print("Prediksi mahasiswa baru (hadir 55%, tugas 60, belajar 3 jam):",
      "Lulus" if m.predict(mhs_baru)[0] else "Berisiko tidak lulus")
