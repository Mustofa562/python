import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

#Data (luas rumah, jumlah kamar)
X = np.array([
    [50,2],
    [70,3],
    [90,3],
    [120,4],
    [150,4],
    [200,5]
])

# Harga rumah (dlam juta)
y = np.array([300,420,520,650,800,950])

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.4, random_state=1)

print("Train data:", X_train)
print("Test data :", X_test)

model = LinearRegression()
model.fit(X_train,y_train)

print("Model selesai training")

predict = model.predict(X_test)
print("Prediksi :", predict)
print("Asli     :", y_test)

print(model.predict([[100,3]]))  # data baru total


score = r2_score(y_test,predict)
print("R² Score:", score)

#prediksi rumah baru
rumah_baru = [[180,4]] #luas rumah 180, kamar 4
hasil = model.predict(rumah_baru)
print('prediksi harga rumah baru:', hasil)