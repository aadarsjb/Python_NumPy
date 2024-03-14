# the number of elements in each  dimensions

# Numpy array have an attribute called shape
#returns a tuple with each index having the number of corresponding elements

import numpy as np

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

print(arr.shape)
# output = (2, 4) ---> tuple

arr0 = np.array([1,2,3,4], ndmin = 5)

print(arr0)
print(f'shape of array : {arr0.shape}')
# output  = (1, 1, 1, 1, 4)

###########################################################

# Numpy Array Reshaping

# changing shape of the array

# by reshaping we can add or remove dimensions or change number of element in each dimensions

arr1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

print(arr1)

print("1-D to 2-D Array")
newarr = arr1.reshape(4, 3)

newarr3 = arr1.reshape(6,2)
print(newarr3)

print(newarr)


print("1-D to 3-D Array")
newarr0 = arr1.reshape(2, 2, 3)
print(newarr0)
print(f"dimension of new arry is : {newarr0.ndim}")

newarr1 = arr1.reshape(2, 3, 2)
print(newarr1)
print(f"dimension of new arry is : {newarr1.ndim}")

newarr2 = arr1.reshape(3, 2, 2)
print(newarr2)
print(f"dimension of new arry is : {newarr2.ndim}")

print(f"3- D array to 2-D array :\n {newarr2.reshape(6,2)}")

print("Accessing elements form an array")

print(newarr3[5, 0])
print(newarr2[2, 0, 0])
print(newarr1[1, 2, 1])

































