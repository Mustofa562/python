import matplotlib.pyplot as plt
import random

x = [1,2,3,4,5,6,7,8]
y = [5,6,4,7,8,9,3,4]

#Garis sederhana
plt.subplot(2,2,1)
plt.plot(x,y, label='garis')
plt.title('garis sederhana')

plt.subplot(2,2,2)
plt.scatter(x,y)
plt.plot(x,y,label='scatter')
plt.title('scatter')

plt.subplot(2,2,3)
plt.bar(x,y, label='chart')
plt.title('bar chart')

plt.subplot(2,2,4)
plt.hist(x)
plt.title('historigm')

plt.show()

#historigm dg 10 bins
data = [random.randint(10, 50) for _ in range(100)]
plt.hist(data,bins=10,edgecolor='black',alpha=0.7)
plt.title('historigm')
plt.xlabel('sumbu x')
plt.ylabel('sumbu y')
plt.show()

#grafik dengan costum marker
tahun = [2018, 2019, 2020, 2021, 2022]
penjualan = [120, 150, 100, 180, 200]
plt.plot(tahun,penjualan, marker='o',label='titik tertinggi', markersize=12, linestyle='--')
plt.xlabel('tahun')
plt.ylabel('penjualan')
plt.legend()
plt.show()

#scatter plot dg ukuran titik berbeda
x = [1,2,3,4,5,6]
y = [4,5,3,6,7,8]
ukuran = [50, 100, 200, 300, 400, 500]
plt.scatter(x,y,s=ukuran)
plt.title('scatter plot')
plt.xlabel('sumbu x')
plt.ylabel('sumbu y')
plt.show()

#save figure dlm 3 format
tahun = [2018, 2019, 2020, 2021, 2022]
penjualan = [120, 150, 100, 180, 200]
plt.plot(tahun, penjualan)
plt.savefig('grafik_latihan.png')
plt.savefig('grafik_latihan.pdf')
plt.savefig('grafik_latihan.jpg')
plt.show()

#Plot Multi-Line Dengan Warna Manual
x = [1,2,3,4,5]
a = [1,4,2,5,3]
b = [2,5,3,6,4]
c = [3,6,4,7,5]

plt.plot(x,a,label='line a',color='red', marker='o')
plt.plot(x,b,label='line b',color='green',marker='^')
plt.plot(x,c,label='line c',color='blue',marker='*')
plt.legend()
plt.show()

#Membuat Figure Lebar
x = [1,2,3,4,5]
a = [1,4,2,5,3]
plt.figure(figsize=(12,4))
plt.plot(x,a)
plt.show()

#Subplot Share Axis
b = [2,5,3,6,4]
c = [3,6,4,7,5]
fig, ax = plt.subplots(1, 2, figsize=(10,4), sharex=True)

# subplot kiri
ax[0].plot(b, c, label='line', color='blue')
ax[0].set_title('Line')

# subplot kanan
ax[1].scatter(b, c, label='scatter', color='red')
ax[1].set_title('Scatter')

plt.tight_layout()
plt.show()