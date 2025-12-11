import numpy as np

#LATIHAN BATCH 2

#Latihan fancy indexing
arr = np.array([100,200,300,400,500])
#ambil elemen ke 2,4 dan 5
arr1 = [1,3,4]
print(arr[arr1])
#ubah elemen 1 dan 3 menjadi 999
arr1 = [0,2]
arr[arr1] = 999
print(arr)

#Latihan masking
data = np.array([5, 12, 18, 25, 7, 30])
#ambil elemen lebih kecil dari rata-rata
data1 = data<np.mean(data)
print(data[data1])
#ganti elemen lebih besar dari 20 menjadi 0
data1 = data > 20
print(np.where(data1,0,data))

#Latihan Broadcasting
x = np.array([[2, 4, 6],
              [8, 10, 12]])
y = np.array([[1],
              [3]])
#operasi penjumlahan dan perkalian
print(x+y)
print(x*y)

#Latihan Random Operation
rand = np.random.randint(10, 100, (3, 3))
#nilai max di setiap kolom
print(np.max(rand,axis=0))
#nilai max di setiap baris
print(np.max(rand,axis=1))
#rata-rata seluruh elemen
print(np.mean(rand))

#Latihan staxking
A = np.array([[1, 2],
              [3, 4]])
B = np.array([[5, 6],
              [7, 8]])
C = np.array([[9, 10],
              [11, 12]])
#menggabungkan matrix di list
D = [A,B,C]
#gabung secara vertikal
print(np.vstack(D))
#gabung secara horizontal
print(np.hstack(D))

#Latihan Sorting dan Argsort
nilai = np.array([45, 80, 60, 75, 90])
#urut dari kecil ke besar
urut = np.sort(nilai)
print(urut)
#urutan indec
print(np.argsort(urut))

#Latihan Algebra
M = np.array([[4, 2],
              [1, 3]])
#hitung determinan
print(np.linalg.det(M))
#hitung invers
print(np.linalg.inv(M))
#hitung eigenvalue dan egienvector
print(np.linalg.eig(M))


#LATIHAN BATCH 3

#fancy index dan masking
arr = np.arange(5, 26, 2)
#ambil elemen 2,5 dan 7
arr1 = [1,4,6]
print(arr[arr1])
#ubah elemen 4 dan 8 jadi 0
arr2= [3,7]
arr[arr2] = 0
print(arr)
#ambil semua elemen lebih besar dari rata rata
rata = arr>np.mean(arr)
print(arr[rata])

#random dan reshape
#buat array random 4x4 dari angka 10-99
a = np.random.randint(10,99,(4,4))
print(a)
#ubah menjadi array 2X8
print(a.reshape(2,8))
#hitung max baris dan rata rata seluruh elemen
print(np.max(a,axis=1))
print(np.mean(a))

#broadcasting
x = np.array([[2, 4, 6],
              [8, 10, 12],
              [14, 16, 18]])
y = np.array([[1], [3], [5]])
#operasi penjumlahan
print(-x+y)
#operasi pengurangan
print(-x-y)
#operasi perkalian
print(-x*y)

#stacking dinamis
a = np.array([[1, 2],
              [3, 4]])
b = np.array([[5, 6],
              [7, 8]])
c = np.array([[9, 10],
              [11, 12]])
#gabungkan array
d = [a,b,c]
#gabung menjadi vertikal dan horizontal
e = np.vstack(d)
print(e)
print(np.hstack(d))
#ambil elemen ke 5 dari gabungan vertikal
print(e[4])

#Sorting dan Argsort
nilai = np.array([75, 60, 90, 80, 55])
#urut dari kecil ke besar
print(np.sort(nilai))
#urutan index sebelum di urutkan
print(np.argsort(nilai))
#nilai max dan min
print(np.max(nilai))
print(np.min(nilai))

#Linear algebra
M = np.array([[4, 2],
              [1, 3]])
#hitung determinan
print(np.linalg.det(M))
#hitung inverse
inv = np.linalg.inv(M)
print(inv)
#hitung perkalian matrix m @ inverse
print(M@inv)
#tampilkan eignvalue dan eigenvactor
print(np.linalg.eig(M))