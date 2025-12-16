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