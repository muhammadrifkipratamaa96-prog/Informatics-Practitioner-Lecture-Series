"""
STUDI KASUS 3 - GIS di dunia industri / karier
Kasus : Perusahaan logistik memilih lokasi gudang terbaik dari 8 kandidat.
Kriteria (analisis spasial): jumlah penduduk terlayani dalam radius 15 km
        + kedekatan ke jalan utama.
Data sintetis. Untuk data nyata: geopandas.read_file("desa.shp"), lalu sjoin/buffer.
"""
import numpy as np, pandas as pd
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt

def haversine(lat1, lon1, lat2, lon2):
    R = 6371.0
    p1, p2 = np.radians(lat1), np.radians(lat2)
    a = np.sin((p2-p1)/2)**2 + np.cos(p1)*np.cos(p2)*np.sin(np.radians(lon2-lon1)/2)**2
    return 2*R*np.arcsin(np.sqrt(a))

rng = np.random.default_rng(7)
desa = pd.DataFrame({"lat": rng.uniform(-3.5, -3.0, 60),
                     "lon": rng.uniform(102.0, 102.6, 60),
                     "penduduk": rng.integers(500, 8000, 60)})
kand = pd.DataFrame({"lat": rng.uniform(-3.5, -3.0, 8),
                     "lon": rng.uniform(102.0, 102.6, 8),
                     "jarak_jalan_km": rng.uniform(0.2, 12, 8)})

RADIUS = 15
kand["terlayani"] = [desa.penduduk[haversine(r.lat, r.lon, desa.lat, desa.lon) <= RADIUS].sum()
                     for r in kand.itertuples()]
# skor 0-1, bobot 70% cakupan penduduk, 30% akses jalan
kand["skor"] = (0.7*kand.terlayani/kand.terlayani.max()
                + 0.3*(1 - kand.jarak_jalan_km/kand.jarak_jalan_km.max()))
kand = kand.sort_values("skor", ascending=False).reset_index(drop=True)
print(kand.round(2))

best = kand.iloc[0]
fig, ax = plt.subplots(figsize=(7, 6))
ax.scatter(desa.lon, desa.lat, s=desa.penduduk/40, alpha=.4, label="Desa (ukuran = penduduk)")
ax.scatter(kand.lon, kand.lat, marker="s", c="gray", label="Kandidat gudang")
ax.scatter(best.lon, best.lat, marker="*", s=300, c="red", label="Terpilih")
ax.add_patch(plt.Circle((best.lon, best.lat), RADIUS/111, fill=False, color="red", ls="--"))
ax.set_aspect("equal"); ax.legend(); ax.set_title("Pemilihan lokasi gudang")
plt.savefig("03_hasil.png", dpi=120)
