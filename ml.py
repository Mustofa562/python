from sklearn.linear_model import LinearRegression
import numpy as np

#data
x = np.array([[30], [50], [70], [90], [110]])  # luas rumah
y = np.array([300, 500, 700, 900, 1100])       # harga (juta)

model = LinearRegression()

model.fit(x,y)

pred = model.predict([[65]])

print("Prediksi harga untuk 65 m2", pred[0])