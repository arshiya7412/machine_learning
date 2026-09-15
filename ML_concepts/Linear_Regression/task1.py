import numpy as np

# Data
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 5, 4, 5])

# Initialize parameters
m = 0.0
b = 0.0
lr = 0.1
n = len(x)

# Gradient Descent
for i in range(100):
    y_hat = m * x + b

    dm = (-2/n) * np.sum(x * (y - y_hat))
    db = (-2/n) * np.sum(y - y_hat)

    m = m - lr * dm
    b = b - lr * db

print("Slope (m):", m)
print("Intercept (b):", b)
