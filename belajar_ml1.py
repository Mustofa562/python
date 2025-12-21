import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

X = np.array([[1], [2], [3], [4], [5]])
y = np.array([10, 20, 30, 40, 50])

poly = PolynomialFeatures(degree=4)
X_poly = poly.fit_transform(X)

model = LinearRegression()
model.fit(X_poly, y)

pred = model.predict(X_poly)

print("R2:", r2_score(y, pred))

# data baru (belum pernah dilihat model)
X_new = np.array([[6], [7]])
X_new_poly = poly.transform(X_new)

print("Prediksi data baru:", model.predict(X_new_poly))

