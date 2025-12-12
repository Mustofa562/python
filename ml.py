from sklearn.linear_model import LinearRegression
import numpy as np

#data
x = np.array([[30], [50], [70], [90], [110]])  # luas rumah
y = np.array([300, 500, 700, 900, 1100])       # harga (juta)

model = LinearRegression()

model.fit(x,y)

pred = model.predict([[65]])

print("Prediksi harga untuk 65 m2", pred[0])

#latihan lagi
#Latihan a
X = np.array([[10], [11], [12], [13], [14]])
y = np.array([130, 138, 145, 150, 158]) # tinggi badan anak (cm)

mdl = LinearRegression()
mdl.fit(X,y)
pred = mdl.predict([[15]])
print('prediksi tinggi anak', pred)
#latihan b

X = np.array([[1], [2], [3], [4], [5]])  # jumlah jam belajar
y = np.array([55, 60, 65, 70, 80])       # nilai ujian

model = LinearRegression()
model.fit(X,y)
pred = model.predict([[6]])
print("prediksi nilai siswa yang belajar 6 jam", pred)
