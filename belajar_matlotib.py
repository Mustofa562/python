import numpy as np
import matplotlib.pyplot as plt


#membuat data
x = np.array((1,2,3,4,5))
y = np.array((2,4,6,8,10))

#membuat plot
plt.plot(x,y)

#membuat judul
plt.title('data hari')
plt.xlabel('penjualan')
plt.ylabel('hari ke')

#ubah warna dan bentuk garis
plt.plot(x,y, color='blue',linestyle='--',marker='o')

#menampilkan plot
plt.show()

#data baru
buah = ['Apel', 'Jeruk', 'Mangga', 'Pisang']
jumlah = [10, 7, 5, 12]

#membuat grafik cart
plt.bar(buah,jumlah)
plt.title('grafik batang buah')
plt.xlabel('jenis buah')
plt.ylabel('jumlah buah')
plt.bar(buah,jumlah,color='green')
plt.show()

#data baru
label = ['Coklat', 'Karamel', 'Permen Buah']
jumlah = [10, 5, 8]

#membuat grafik lingkaran
plt.pie(jumlah, labels=label, autopct='%1.1f%%')
plt.title('jenis permen faforit')
plt.show()

#data baru
umur = [5, 10, 15, 20, 25]
tinggi = [100, 130, 150, 160, 170]

#membuat grafik titik
plt.scatter(umur,tinggi)
plt.scatter(umur,tinggi,color='blue')
plt.ylabel('tinggi')
plt.xlabel('umur')
plt.show()

