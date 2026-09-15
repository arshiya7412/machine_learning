import numpy as np
a = np.array([1, 2, 3, 4])
print(a)
print(type(a))
print(a.shape)
b = np.array([[1, 2, 3],
             [4, 5, 6]])
print(b)
print(b.shape)
x = np.array([1, 2, 3])
y = np.array([10, 20, 30])

print(x + y)
print(np.mean(x))   # average
print(np.sum(x))    # sum
print(np.max(x))    # max value
