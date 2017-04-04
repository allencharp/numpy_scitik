import numpy as np

a = np.arange(12).reshape(3, 4)
print(a)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]
print(a.shape)
# (3, 4)
print(a.ravel())
# [ 0  1  2  3  4  5  6  7  8  9 10 11]
print(a.reshape(6,2))
# [[ 0  1]
#  [ 2  3]
#  [ 4  5]
#  [ 6  7]
#  [ 8  9]
#  [10 11]]
print(a.T)
# [[ 0  4  8]
#  [ 1  5  9]
#  [ 2  6 10]
#  [ 3  7 11]]
print(a.reshape(1,-1))
# If a dimension is given as -1 in a reshaping operation, the other dimensions are automatically calculated:
# [[ 0  1  2  3  4  5  6  7  8  9 10 11]]