import numpy as np


##latihan fancy indexing
a = np.array([10, 20, 30, 40, 50])

#list index
indx = [0,2,3]
print('ambil elemen ke 1, 3 dan 4', a[indx])
#list index
indx = [1,4]
a[indx] = 999
print('ubah elemen ke 2 dan 5 menjadi 999 =', a)

##latihan masking
b = np.array([5, 10, 15, 20, 25, 30])

#variable dg fungsi memilih array lebih besar dari rata-rata array
lebih_besar = b>np.mean(b)
print('ambil elemen lebih besar dari rata rata array', b[lebih_besar])
#variable dengan fungsi kurang 15
kurang = b<15
print('ganti semua nilai kurang dari 15 menjadi 0', np.where(kurang,0,b))

##latihan broadcasting multidimensi
x = np.array([[1, 2, 3],
              [4, 5, 6]])
y = np.array([[10],
              [20]])

print('ini adalah bagaimana operasi penjumlahan dg bentuk matrix yg berbeda',x+y)

##Latihan operasi random

#buat array 4x4 dg angka 1 - 100
a = np.random.randint(1,100, (4,4))
print('hasil array random 4x4',a)
#nilai maxsimum di setiap baris
print('max setiap baris', np.max(a,axis=1))
#rata - rata seluruh elemen
print('rata rata seluruh elemen',np.mean(a))

##Latihan stacking dinamis
arr1 = np.array([[1, 2],
                 [3, 4]])
arr2 = np.array([[5, 6],
                 [7, 8]])
arr3 = np.array([[9, 10],
                 [11, 12]])

#variable untuk menampung semua array
arr = [arr1,arr2,arr3]
#menggabungkan semua array menjadi array besar vertikal
print(np.vstack(arr))
#menggabungkan semua array menjadi array besar horizontal
print(np.hstack(arr))

##Latihan sorting dan Argsort
data = np.array([40, 10, 50, 30, 20])
#mengurutkan array secara menaik
data_1 = np.sort(data)
print(data_1)
#menampilkan urutan index dari hasil pengurutan
print(np.argsort(data_1))

##Latihan linear algebra
A = np.array([[2, 3],
              [1, 4]])
#menghitung determinan
print(np.linalg.det(A))
#menghitung invers
print(np.linalg.inv(A))
#menhitung eigenvalue dan eigenvector
print(np.linalg.eig(A))