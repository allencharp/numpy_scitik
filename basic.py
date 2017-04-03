import numpy as np
from numpy import pi

# start
a = np.arange(15).reshape(3, 5)
print(a)
print(a.shape)
print(a.ndim)
print(a.itemsize)
print(a.size)

b = np.array([1.2, 3.5, 4.6])
print(b.dtype)

print(b)

c = np.array([[1, 2], [3, 4]], dtype=complex)
print(c)

d = np.arange(0, 2, 0.3)
print(d)

e = np.arange(0,10)
print(e[0:6,2])

#basic operator
a = np.array([20, 30, 40, 50])
b = np.arange(4)
print(b)
print(a - b)

A = np.array([[1, 1],
              [2, 3]])
B = np.array([[2, 0],
              [3, 2]])
print(A * B)

b = np.linspace(0, pi, 3)
print(b)

