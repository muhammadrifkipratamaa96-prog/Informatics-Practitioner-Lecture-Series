# 4. Introduction to Machine Learning
**Studi kasus:** Memprediksi mahasiswa yang berisiko tidak lulus dari kehadiran, nilai tugas, dan jam belajar.

## Alur
1. Membuat 600 data mahasiswa sintetis
2. Membandingkan Logistic Regression, Decision Tree, dan Random Forest dengan 5-fold cross-validation
3. Menguji model terbaik pada data uji (confusion matrix)
4. Memprediksi satu mahasiswa baru

## Menjalankan
```bash
pip install numpy pandas scikit-learn matplotlib
python 04_machine_learning_dasar.py
```
Output: akurasi tiap model, model terbaik, dan grafik `04_hasil.png`.

## Konsep yang dipelajari
Supervised learning, pemisahan data latih/uji, cross-validation, confusion matrix.

## Pengembangan
Tambah tuning hyperparameter (`GridSearchCV`) dan metrik lain (precision, recall, F1).
