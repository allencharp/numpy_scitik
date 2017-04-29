import numpy as np

a = np.arange(12) ** 2 # the first 12 elements
i = np.array([1,2,3,4,5]) # len should < 12
print(a[i])
# [ 1  4  9 16 25]

j = np.array([[1,2],[3,4]])
print(a[j])
#[[ 1  4]
# [ 9 16]]

a = np.arange(12).reshape(3,4)
print(a)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]
i = np.array([[0,1],
              [1,2]])
j = np.array([[2,1],
              [3,3]])
print(a[i,j])
# [[ 2  5]
#  [ 7 11]]
print(a[i,2])
# [[ 2  6]
#  [ 6 10]]
print(a[:,j])
# [[[ 2  1]
#   [ 3  3]]
#
#  [[ 6  5]
#   [ 7  7]]
#
#  [[10  9]
#   [11 11]]]