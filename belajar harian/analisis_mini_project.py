import numpy as np

# ====== DATA PENJUALAN ======
harga_produk = np.array([15000, 25000, 12000, 18000, 22000])
penjualan = np.random.randint(2, 50, (6,5))  # 5 hari x 5 produk
print("Data Penjualan (5x5):\n", penjualan)

# ====== TOTAL PENJUALAN PER HARI ======

total_harian = penjualan * harga_produk
total_perbulan = np.sum(total_harian,axis=1)
print("\nTotal Penjualan per Hari (Rupiah):\n", total_harian)
print("\nTotal Penjualan per Bulan (Rupiah):\n", total_perbulan)

# ====== STATISTIK PER PRODUK ======
rata_per_produk = np.mean(total_harian, axis=1)
max_per_produk = np.max(total_harian, axis=1)
min_per_produk = np.min(total_harian, axis=0)
print("\nRata-rata per hari:", rata_per_produk)
print("Nilai Tertinggi per hari:", max_per_produk)
print("Nilai Terendah per Produk:", min_per_produk)

# ====== PRODUK TERLARIS DAN TERENDAH ======
ranking = np.argsort(rata_per_produk)[::-1]  # Urut dari tertinggi ke terendah
print("\nRanking Produk (index dari terbesar ke terkecil):", ranking)
print("Produk Terlaris =", ranking[0], "| Produk Penjualan Terendah =", ranking[-1])

# ====== NORMALISASI DATA PENJUALAN ======
# Normalisasi agar skala antar produk bisa dibandingkan (0 - 1)
norm_penjualan = (total_harian - np.min(total_harian)) / (np.max(total_harian) - np.min(total_harian))
print("\nData Penjualan Ternormalisasi:\n", np.round(norm_penjualan, 2))

# ====== KORELASI ANTAR PRODUK ======
corr = np.corrcoef(penjualan.T)
print("\nKorelasi antar Produk:\n", np.round(corr, 2))

# ====== MATRIX ANALISIS (Linear Algebra) ======
A = np.array([[np.sum(total_harian[:,0]), np.sum(total_harian[:,1])],
              [np.sum(total_harian[:,2]), np.sum(total_harian[:,3])]])
print("\nMatrix A:\n", A)
print("Determinan A =", np.linalg.det(A))
print("Inverse A =\n", np.linalg.inv(A))

# ====== PRODUK DI ATAS RATA-RATA ======
rata_global = np.mean(total_harian)
print("\nProduk dengan rata-rata penjualan di atas rata-rata global:")
print(rata_per_produk[rata_per_produk > rata_global])
