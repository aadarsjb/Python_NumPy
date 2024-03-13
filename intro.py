# pip install numpy
import numpy as np

# 0-D array
a = np.array(42)
# 1-D array                        
b = np.array([1, 2, 3, 4, 5])
# 2-D array
c = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
# 3-D array
d = np.array([[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]], [[1, 2, 3, 4, 6], [2, 8, 5, 7, 9]]])

print(a)
print(b)
print(c)
print(d)

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

arr = np.array([1,2,3,4,5], ndmin=5)
print(arr)
print('no. of dimensions', arr.ndim)

#accessing elements of array
#for 0-D array
print(a)
#for 1-D array
print(b[3])
print(b[4])
# for 2-D array
print(c[0, 1])
print(c[1, 1])
# for 3-D array
print(d[0, 1, 0])
print(d[1, 1, 0])