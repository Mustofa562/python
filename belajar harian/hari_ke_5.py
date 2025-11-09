import numpy as np

        ## Projek kecil Analisis data penjualan batch 1 

harga_produk = ([15000,25000,12000,18000,22000])
penjualan = np.random.randint(5,50,(7,5))
print("Data penjualan per hari (7x5):\n", penjualan)

total_per_hari = penjualan * harga_produk
print("Total penjualan per hari:", total_per_hari)

hari_tertinggi = np.max(total_per_hari)
hari_terendah = np.min(total_per_hari)
print("Hari tertinggi:", hari_tertinggi)
print("Hari terendah:", hari_terendah)

rata_per_produk = np.mean(total_per_hari,axis=0)
std_per_produk = np.std(total_per_hari,axis=0)
print("Rata-rata per produk:", rata_per_produk)
print("Standar deviasi per produk:", std_per_produk)

rata_global = np.mean(penjualan)
penjualan_baru = np.where(penjualan < rata_global, 0, penjualan)
print("Penjualan baru (nilai < rata-rata diganti 0):\n", penjualan_baru)

gabung = np.stack([[harga_produk,rata_per_produk]])
print("Data gabungan (harga & rata-rata penjualan):\n", gabung)

M = np.array([[np.sum(total_per_hari[:3]), np.sum(total_per_hari[3:5])],
              [np.sum(total_per_hari[5:]), np.mean(total_per_hari)]])
print("Matrix M:\n", M)
print("Determinant =", np.linalg.det(M))
print("Inverse =\n", np.linalg.inv(M))

    ## Projek kecil Analisis data penjualan batch 1 
import numpy as np

# ====== DATA PENJUALAN ======
harga_produk = np.array([15000, 25000, 12000, 18000, 22000])
penjualan = np.random.randint(10, 100, (10, 5))  # 10 hari x 5 produk
print("Data Penjualan (10x5):\n", penjualan)

# ====== TOTAL PENJUALAN PER HARI ======
total_harian = penjualan * harga_produk
print("\nTotal Penjualan per Hari (Rupiah):\n", total_harian)

# ====== STATISTIK PER PRODUK ======
rata_per_produk = np.mean(total_harian, axis=0)
max_per_produk = np.max(total_harian, axis=0)
min_per_produk = np.min(total_harian, axis=0)
print("\nRata-rata per Produk:", rata_per_produk)
print("Nilai Tertinggi per Produk:", max_per_produk)
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
