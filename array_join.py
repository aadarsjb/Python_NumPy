# puutting content of two or more arrays in a single array
#  we join arrays by axes

# pass a sequence of arra to the concatenate() function, along with the axis

import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

print("Concatenating")
arr = np.concatenate((arr1, arr2))

print(arr)

print("")

print("Join two 2-D arrays along row (axis = 1):")

arr3 = np.array([[1, 2, 3], [4, 5, 6]])
arr4 = np.array([[11, 22, 33], [44, 55, 66]])

print("Concatenating")
arr5 = np.concatenate((arr3, arr4), axis = 1)
print(arr5)


print("Join two 2-D arrays along row (axis = 0):")
print("Concatenating")
arr5 = np.concatenate((arr3, arr4), axis = 0)


print(arr5)
print(arr5.ndim)
print(arr5.dtype)

for idx, item in np.ndenumerate(arr5):
    print(idx, item)

print("Iterating through array")
for idx, item in np.ndenumerate(arr5[0:2, ::-1]):
    print(idx, item)

for idx, item in np.ndenumerate(arr5[2:3, ::-1]):
    print(idx, item)


print("Joining arrays using stack function")

arr6 = np.stack((arr1, arr2), axis = 1)
print(arr6)

print("Joining arrays using hstack function\nIt stack along rows")
arr7 = np.hstack((arr1, arr2))
print(arr7)

print("Joining arrays using vstack function\nIt stack along columns")
arr8 = np.vstack((arr1, arr2))
print(arr8)

print("Stacking along Height(depth) using dstack function\nIt stack along height")
arr9 = np.vstack((arr1, arr2))
print(arr9)





























