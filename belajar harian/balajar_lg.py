
import matplotlib.pyplot as plt
import numpy as np



#Latihan fill between dan style matplotlib
X = np.array([1,2,3,4,5,6,7,8,9,10])
Y = np.random.randint(5,15,size=10)
plt.style.use('ggplot')
plt.plot(X,Y, marker='o')
plt.grid(True)
plt.fill_between(X,Y,color='red',alpha=0.2)
plt.title('contoh style')
plt.show()


#dual axis/twinx
data = [1,2,3,4,5]
data1 = [30,31,29,28,32]
data2 = [50,80,60,30,100]

fig, ax1 = plt.subplots()
#grafik pertama
ax1.plot(data,data1,color='red', label = 'suhu')
ax1.set_ylabel('Suhu', color='black')

#grafik kedua
ax2 = ax1.twinx()
ax2.plot(data,data2,color='green', label='penjualan')
ax2.set_ylabel('Penjualan', color='purple')
plt.title('Dua sumbu Y')
plt.show()

#Erro bar chart
x = ['A','B','C','D']
nilai = [10, 15, 7, 12]
error = [1.5, 2, 1, 1.8]
plt.errorbar(x,nilai,yerr=error,fmt='-o',capsize=5, color='blue')
plt.show()