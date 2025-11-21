import matplotlib.pyplot as plt
import numpy as np

# Stacked area chart
tahun = [2018,2019,2020,2021,2022]
laptop = [30,40,35,50,60]
hp     = [20,25,30,35,40]
tablet = [10,20,15,22,30]
plt.stackplot(tahun,laptop,hp,tablet, labels=['Laptop','Hp','Tablet'])
plt.legend()
plt.show()

#Grouped bar chart
buah = ['Apel','Jeruk','Pisang','Mangga']
y = [40,25,35,30]
z = [45,30,38,34]
x = np.arange(len(buah))
width = 0.35

plt.bar(x-width/2,y,width, label='Tahun 2023')
plt.bar(x+width/2,z, width,label='Tahun 2024')
plt.xticks(x,buah)
plt.legend()
plt.title('Grouped bar chart')
plt.show()

#polar plot
a = np.linspace(0,2*np.pi)
print(a)