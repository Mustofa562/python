import numpy as np
import matplotlib.pyplot as plt


#Latihan Grafik garis 2 variabel
bulan = [1, 2, 3, 4, 5, 6]
penjualan_a = [10, 12, 9, 15, 17, 20]
penjualan_b = [8, 11, 13, 14, 16, 18]

#plt.plot(bulan,penjualan_a,label='Data A', color='red')
#plt.plot(bulan,penjualan_b,label='Data B', color='blue')
#plt.title('penjualan perbulan')
#plt.xlabel('bulan')
#plt.ylabel('jumlah penjualan per bulan')
#plt.legend()
#plt.show()

#Latihan mengubah ukuran gambar
x = [1,2,3,4,5]
y = [5,3,6,2,7]
#plt.figure(figsize=(10,4))
#plt.plot(x,y,color='red',marker='^')
#plt.show()

#Latihan menambah Grid
tahun = [2019, 2020, 2021, 2022, 2023]
pendapatan = [50, 55, 60, 58, 65]
plt.plot(tahun,pendapatan, color = 'blue', marker='o')
plt.grid(True)
plt.title('pendapatan per tahun')
plt.show()

#Latihan bar Chart horiazontal
kota = ["Jakarta", "Bandung", "Surabaya", "Medan"]
penduduk = [10, 4, 3, 2]
plt.barh(kota,penduduk, color='purple')
plt.title('jumlah penduduk')
plt.show()

#Latihan Pie Chart dg Highlight
kategori = ['Makanan', 'Transportasi', 'Hiburan', 'Lainnya']
pengeluaran = [500, 300, 150, 50]
explode = [0.1, 0, 0, 0]
plt.pie(pengeluaran, labels=kategori, autopct='%1.1f%%', explode=explode)
plt.title("Pengeluaran Bulanan")
plt.axis('equal')
plt.show()
