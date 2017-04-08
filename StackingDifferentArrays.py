import numpy as np

a = np.floor(10 * np.random.random((2,2)))
print(a)

b = np.floor(10*np.random.random((2,2)))
print(b)

c = np.vstack((a,b))
print(np.vstack((a,b)))
print(np.hstack((a,b)))
print(c)

d = np.array([1,2,3])
e = np.array([3,4,5])
print(np.column_stack((d,e)))
# [[1 3]
#  [2 4]
#  [3 5]]
f = np.r_[1:4, 0,1,8,9, 4]
print(f)
# [1 2 3 0 1 8 9 4]