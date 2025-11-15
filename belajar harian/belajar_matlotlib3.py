import matplotlib.pyplot as plt

#Latihan subplot
x = [1,2,3,4,5]
y1 = [2,4,6,8,10]
y2 = [5,3,6,2,7]
plt.subplot(1,2,1)
plt.plot(x,y1)
plt.title('garis y1')

plt.subplot(1,2,2)
plt.plot(x,y2)
plt.title('bar y2')
plt.show()

#latihan histogram sederhana
data = [12, 14, 15, 17, 17, 18, 19, 20, 21, 22,
        15, 17, 18, 19, 23, 24, 25, 17, 14, 13]

plt.hist(data)
plt.ylabel('sumbu')
plt.title('histogram sederhana')
plt.show()


#latihan grafik ke file png
angka = [1,2,3,4,5,6,7,8,9]
nilai = [3,5,2,6,8,9,10,7,4]

plt.plot(angka,nilai)
plt.savefig('grafik_nilai.png')
plt.show()

#Latihan catter + Garis Tren
a = [1,2,3,4,5,6]
b = [2,3,5,6,8,9]

plt.scatter(a,b)
plt.plot(a,b,label='data')
plt.title('cetter + garis tren')
plt.xlabel('nilai x')
plt.ylabel('nilai y')
plt.show()


#latihan Grafik dengan Warna Otomatis
x = [1,2,3,4,5]
a = [1,2,3,4,5]
b = [2,3,4,5,6]
c = [3,4,5,6,7]

plt.plot(x, a, label="A")
plt.plot(x, b, label='B')
plt.plot(x, c, label='C')
plt.legend()
plt.show()