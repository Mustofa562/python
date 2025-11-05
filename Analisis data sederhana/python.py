import numpy as np
import matplotlib.pyplot as plt

#nilai dariu 30 siswa secara acak
nilai = np.random.randint(50,101,size = 30)

print("Data nilai:",nilai)
print("Rata-rata:",np.mean(nilai))
print("Median:",np.median(nilai))
print("Stanmdar Deviasi:",np.std(nilai))
print("Nilai tertinggi", np.max(nilai))
print("Nilai Terendah",np.min(nilai))

#visual 
plt.hist(nilai, bins=10, edgecolor="black", color="skyblue")
plt.title("Nilai Ujian Siswa")
plt.xlabel("Rentang Nilai")
plt.ylabel("Jumlah siswa")
plt.show()

#visual
plt.boxplot(nilai, vert=False, patch_artist=True)
plt.title("Boxplot Nilai Ujian Siswa")
plt.xlabel("Nilai")
plt.show()