import numpy as np

x = np.array([1, 2, 3, 4, 5, 6])
y = np.array([3, 6, 7, 10, 11, 14])
m = 0.0
b = 0.0
lr = 0.001
n = len(x)

for i in range(100):
  y_hat = m * x + b


  dm = (-2/n) * np.sum(x * (y - y_hat))
  db = (-2/n) * np.sum(y - y_hat)

  m = m - lr * dm
  b = b - lr * db

print("Slope:", m)
print("Intercept:", b)
