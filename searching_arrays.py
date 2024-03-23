# use the where() method

import numpy as np

arr = np.array([1, 2 ,3, 4, 5, 4, 4])

x = np.where(arr == 4)

# returns a tuple: (array([3, 5, 6],) --> Index of the value 4
print(x)

print("finding indexes where the values are even")

arr2 = np.array(range(1, 12))

x = np.where(arr2 % 2 == 0)

print(x)

print()

print(" search sorted")

# performs binary search in the array
# returns where the specified value would be sorted
#assumed to be used on sorted arrays

y = np.searchsorted(arr2, 7)

print(y)


print("Searching from right side")

z = np.searchsorted(arr2, 7, side = "right")
print(arr2)

print(z)









































