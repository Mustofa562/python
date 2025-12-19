from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import numpy as np
from sklearn.linear_model import LinearRegression

# Data
X = [
    [150, 7],
    [170, 8],
    [140, 6],
    [300, 10],
    [320, 11],
    [280, 10]
]

y = ["apel", "apel", "apel", "jeruk", "jeruk", "jeruk"]

# 1. Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.33, random_state=1
)

# 2. Scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 3. Model
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train_scaled, y_train)

# 4. Predict data test
y_pred = model.predict(X_test_scaled)

# 5. Accuracy
acc = accuracy_score(y_test, y_pred)
print("Accuracy:", acc)


# Data
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([10, 20, 30, 40, 50])

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=1
)

# Model
model = LinearRegression()

# Training
model.fit(X_train, y_train)

# Predict
prediksi = model.predict(X_test)

print("Prediksi:", prediksi)
print("Jawaban asli:", y_test)

#latihan lagi 
import numpy as np
from sklearn.linear_model import LinearRegression

# Data
X = np.array([[1], [2], [3], [4]])
y = np.array([10, 20, 30, 40])

# Model
model = LinearRegression()

# Train
model.fit(X, y)

# Predict
print(model.predict([[8]]))

#
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

X = np.array([[1], [2], [3], [4], [5]])
y = np.array([10, 20, 30, 40, 50])

# Bagi data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.4, random_state=1
)

model = LinearRegression()
model.fit(X_train, y_train)

print("X_test:", X_test)
print("Prediksi:", model.predict(X_test))
print("Asli:", y_test)

from sklearn.metrics import r2_score

r2 = r2_score(y_test, model.predict(X_test))
print("R2 score:", r2)

import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

X = np.array([[1], [2], [3], [4], [5]])
y = np.array([12, 19, 33, 38, 55])  # data agak acak

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.4, random_state=1
)

model = LinearRegression()
model.fit(X_train, y_train)

pred = model.predict(X_test)

print("X_test:", X_test)
print("Prediksi:", pred)
print("Asli:", y_test)
print("R2:", r2_score(y_test, pred))

