"""
STUDI KASUS 1 - Make Sense of Data with Analysis and AI
Kasus : Toko online UMKM ingin tahu pelanggan mana yang berisiko berhenti (churn).
Alur  : buat data -> bersihkan -> eksplorasi -> model AI -> interpretasi.
"""
import numpy as np, pandas as pd
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

rng = np.random.default_rng(42)
n = 1500
df = pd.DataFrame({
    "lama_langganan_bulan": rng.integers(1, 48, n),
    "transaksi_per_bulan": rng.poisson(4, n),
    "rata_belanja_rp": rng.normal(150_000, 50_000, n).clip(20_000),
    "keluhan": rng.poisson(0.7, n),
})
logit = (-0.3 + 0.9*df.keluhan - 0.05*df.lama_langganan_bulan
         - 0.25*df.transaksi_per_bulan + rng.normal(0, 0.8, n))
df["churn"] = (rng.random(n) < 1/(1+np.exp(-logit))).astype(int)
df.loc[rng.choice(n, 60, replace=False), "rata_belanja_rp"] = np.nan  # data kotor

# 1) Pembersihan
df["rata_belanja_rp"] = df["rata_belanja_rp"].fillna(df["rata_belanja_rp"].median())

# 2) Eksplorasi
print("Tingkat churn:", round(df.churn.mean()*100, 1), "%")
print(df.groupby("churn").mean().round(1), "\n")

# 3) Model AI
X, y = df.drop(columns="churn"), df["churn"]
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.25, random_state=0, stratify=y)
model = RandomForestClassifier(n_estimators=200, random_state=0).fit(Xtr, ytr)
print(classification_report(yte, model.predict(Xte)))

# 4) Interpretasi: fitur apa yang paling berpengaruh?
imp = pd.Series(model.feature_importances_, index=X.columns).sort_values()
imp.plot.barh(title="Faktor paling berpengaruh pada churn")
plt.tight_layout(); plt.savefig("01_hasil.png", dpi=120)

# 5) Aksi: daftar pelanggan berisiko tinggi untuk diberi promo
df["risiko"] = model.predict_proba(X)[:, 1]
print(df.sort_values("risiko", ascending=False).head(5)[["lama_langganan_bulan", "keluhan", "risiko"]])
