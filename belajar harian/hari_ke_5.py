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

