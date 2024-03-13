# Data types in python
# strings
# integers
# float
# boolean
# complex

# Data types in Numpy
#has some extra datatypes

# i - integer
# b - boolean
# u -unsigned Integer
# f - float
# c - complex float
# m - timedelta
# M - datetime
# O - objects
# S - string
# U - unicode string
# V - fixed chunck of memory for other type ( void )

import numpy as np

arr = np.array([1, 2, 3, 4, 5])
arr0 = np.array([1.1, 2.0, 3.6, 4.8, 5.01])
arr2 = np.array(['apple', 'banana', 'cherry'])

#checking the data type of an array
# Numpy array object has a property called dtype that returns the datatype of the array

print(arr.dtype)    # prints int32
print(arr2.dtype)    # prints U6

# dtype allows us to define expected datatypes os the array elements
# array() can take optional argument - in this case dtype

arr3 = np.array([1, 2, 3, 4], dtype='S')

print(arr3)
print(arr3.dtype)

# for i, u, f, S and U we can define size as well

arr4 = np.array([1,2,3,4], dtype='i4')

print(arr4)
print(arr4.dtype)

#################################################################################
#Converting Data Types on Existing arrays

# best way is to make copy of the array with astype() method.
#astype() function creats a copy of the array , and allows us to specify the datatype as parameter.

newarr = arr0.astype('i')
print(arr0.dtype)
print(newarr.dtype)
arr5 = np.array([1, 0, 3, 4])
newarr1 = arr5.astype('bool')
print(newarr1.dtype)
print(newarr1)














