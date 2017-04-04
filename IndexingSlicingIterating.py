import numpy as np

a = np.arange(10) ** 3
print(a)
# [  0   1   8  27  64 125 216 343 512 729]
print(a[2])
# 8
print(a[2:5])
# [ 8 27 64]
a[:6:2] = 100
print(a)
# [100   1 100  27 100 125 216 343 512 729]
print(a[::-1])
# [729 512 343 216 125 100  27 100   1 100]


def f(x, y):
    return 10 * x + y

b = np.fromfunction(f, (5,4),dtype=int)
print(b)
# [[ 0  1  2  3]
#  [10 11 12 13]
#  [20 21 22 23]
#  [30 31 32 33]
#  [40 41 42 43]]
print(b[2,3])
# 23
print(b[0:5, 1])
# [ 1 11 21 31 41]
print(b[:,1]) # == print(b[0:5, 1])
# [ 1 11 21 31 41]
print(b[1:3:])
# [[10 11 12 13]
#  [20 21 22 23]]
print(b[-1]) # == print(b[-1,::])
#[40 41 42 43]