import numpy as np

#Latihan masking dan kondisi
data = np.array([12,45,67,23,90,34,56,78])
#Tampilkan elemen yang lebih besar dari rata-rata DAN lebih kecil dari 80
data1 = (data > np.mean(data)) & (data< 80)
print(data[data1])
#Ganti semua elemen di bawah median menjadi nilai median-nya.
data1 = data < np.median(data)
data[data1] = np.median(data)
print(data)

#Latihan Random dan statistik
a = np.random.randint(10,100,(10,5))
print(a)
#Hitung rata-rata setiap kolom.
print(np.mean(a,axis=0))
#Hitung standar deviasi seluruh data
print(np.std(a))
#ganti elemen lebih besar dari 80 menjadi 999
a1 = a>80
a[a1] = 999
print(a)

#Latihan Broadcasting & Operasi Matematis
A = np.arange(1,10).reshape(3,3)
B = np.array([[2],[4],[6]])
#Hitung A + B dan A * B
tambah = A+B
kali = A*B
print(tambah, kali)
#Kalikan setiap elemen hasil perkalian dengan rata-rata seluruh elemen A
rata_elemen_A = np.mean(A)
print(kali * rata_elemen_A)

#Latihan Stacking & Manipulasi 3D
X = np.array([[1,2],[3,4]])
Y = np.array([[5,6],[7,8]])
Z = np.array([[9,10],[11,12]])

D = [X,Y,Z]
Array3d = np.stack(D)
#Ambil layer ke-3
print(Array3d[2])
#Hitung rata-rata tiap layer
print(np.mean(Array3d,axis=(1,2)))
#Hitung nilai maksimum di seluruh layer
print(np.max(Array3d))


#Latihan Linear Algebra & Korelasi
M = np.array([[4,5],[2,3]])
#Hitung determinan, invers, dan eigenvalue-nya.
print(f'hasil determinan = {np.linalg.det(M)}, hasil invers = {np.linalg.inv(M)}, hasil eigenvalue = {np.linalg.eig(M)}')
#Buat array acak N = np.random.randint(1,10,(2,2)) lalu hitung hasil M @ N.
N = np.random.randint(1,10,(2,2))
perkalian = M@N
print(perkalian)
#hitung korelasi antar kolom dari hasil perkalian M dan N
print(np.corrcoef(perkalian))