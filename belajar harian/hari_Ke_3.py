import numpy as np


#Latihan array dan masking kombinasi
arr = np.arange(10,31,2)
#tampilkan semua elemen genap yg lebih besar dari rata rata
genap = (arr % 2 == 0) & (arr > np.mean(arr))
print(arr[genap])
#ubah elemen terkecil menjadi 0
arr[0] = 0
print(arr)
#tampilkan total elemen yang lebih besar dari median
arr1 = arr > np.median(arr)
print(np.sum(arr1))

#Latihan random dan fancy indexing
#buat array random 5x5 dari angka 50–150
a = np.random.randint(50,150,(5,5))
print(a)
# ambil elemen baris ke-2 dan ke-5
print(a[1,:],a[4,:])
# ubah elemen kolom ke-3 di semua baris jadi 0
a[:,2] = 0
# hitung nilai maksimum tiap kolom
print(np.max(a,axis=0))


#Latihan Reshape & Broadcasting
a = np.arange(1, 13)
# ubah menjadi array 3x4 
a = np.arange(1, 13).reshape(3,4)
# tambahkan array [[10], [20], [30]] ke dalamnya
b = np.array([[10],[20],[30]])
print(a + b)
# tampilkan hasil perkalian a * 2 dan rata-rata tiap baris
print(a*2)
print(np.mean(a,axis=1))

#Latihan Stacking Dinamis
A = np.array([[1, 2],
              [3, 4]])
B = np.array([[5, 6],
              [7, 8]])
C = np.array([[9, 10],
              [11, 12]])

# gabungkan semua array menjadi satu array besar 3D
D = [A,B,C]
arr3d = np.stack(D)
print(arr3d)
# ambil layer ke-2
print(arr3d[1])
# hitung rata-rata setiap layer
print(arr3d.mean(axis=(1,2)))

#Latihan Sorting & Linear Algebra
data = np.array([[4, 2],
                 [3, 5]])
# urutkan semua elemen dalam satu dimensi
print(np.sort(data.flatten()))
# hitung determinan dan inverse
print(np.linalg.det(data), np.linalg.inv(data))
# hitung hasil kali matrix data @ inverse-nya
inv = np.linalg.inv(data)
print(data @ inv)
# tampilkan eigenvalue-nya
print(np.linalg.eig(data))
