import numpy as np

# Splitting is reverse of joining
# breaking a single array into multiple array
arr = np.array([1, 2, 3, 4, 5, 6])

# We use array_split() for splitting arrays
# we pass it the array we want to split and number of split
newarr = np.array_split(arr, 3)

print(newarr)


# If array has less elements than required
# It will adjust from the end accordingly

newarr1 = np.array_split(arr, 4)

print(newarr1)

# Return value of the array_split() method is an array
# we can access it as an array

print(newarr1[0])
print(newarr1[1])
print(newarr1[2])
print(newarr1[3])

print("-----------------------------------Splitting 2-D array---------------------------------------------")


arr1 = np.array([[1,2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])

newarr2 = np.array_split(arr1, 3)
newarr3 = np.array_split(arr1, 6)

print(newarr2)
print(newarr3)

print("------------------------------------------------------------------------------")

arr2 = np.arange(9)

print(np.array_split(arr2, 4))

print(np.hsplit(arr1, 1))
print(np.hsplit(arr2, 1))































