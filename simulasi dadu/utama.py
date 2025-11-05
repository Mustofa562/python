
import numpy as np
import matplotlib.pyplot as plt

#lempar 1000 kali
roll = np.random.randint(1,7, size=1000)


#frekuensi
plt.hist(roll, bins= np.arange(1, 8 ) - 0.5, edgecolor = "black", rwidth=0.8)

#judul dan lebel
plt.title("Simulasi lempar dadu")
plt.xlabel("Angka Dadu")
plt.ylabel("Frekuensi")

#Tampilan
plt.show()