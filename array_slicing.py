#taking elements from one given index to another given index
# we pass slice instead of index like this ---> [1:4]
# [start:end]
#can also define step --> [start:end:step]

import numpy as np 

arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

print(arr[1:5])
print(arr[1:])
print(arr[:5])
print(arr[::2])
print(arr[::-1])
print(arr[-2:-6:-1])
print(arr[-6:-2])
print(arr[-6:-2:2])
print(arr[-2:-6:-2])


#############################################################################

# SlICING 2-D ARRAY
print("2-D Array Slicing")
arr2 = np.array([[0,1,2,3,4,5], [6,7,8,9,10,11]])

#prints values from second array 
print(arr2[1, 1:5]) #not including 5
print(arr2[1, ::-1])
print(arr2[0, ::-1])
print(arr2[0, ::2])

# From both elements, return index 2
print(arr2[0:2, 2])
print(arr2[0:2, 2:5])


# for 3-D array

arr3 = np.array([[[1,2,3],[4,5,6]], [[11,22,33], [44,55,66]]])
print(arr3[1, 1, 1:])
#prints [55 66]
print(arr3[1, 0, ::-1])
#prints [33 22 11]
print(arr3.ndim)







