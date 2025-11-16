import matplotlib.pyplot as plt

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