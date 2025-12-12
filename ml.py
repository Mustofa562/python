from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

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

#latihan training data

X = np.array([[1], [2], [3], [4], [5], [6], [7], [8]])
y = np.array([55, 60, 65, 70, 75, 80, 82, 90])

X_train, X_test, y_train, y_test =train_test_split(X,y, test_size=0.25, random_state=42)
model = LinearRegression()
model.fit(X_train,y_train)
y_pred = model.predict(X_test)
score = model.score(X_test,y_test)


print("Data testing:", X_test)
print("Prediksi:", y_pred)
print("Nilai sebenarnya:", y_test)
print("Score (R²):", score)