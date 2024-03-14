# going through each element of the array
import numpy as np

print("Iterating 1-D array")

arr = np.array([1, 2, 3])

for item in arr:
    print(item)


print("Iterating 2-D array")
arr1 = np.array( [[1, 2, 3], [4, 5, 6]] )
# In 2-D array it will go through all the rows
for item in arr1:
    print(item)

for item in arr1:
    for i in item:
        print(i)

print("For 3-D array")

arr2 = np.array( [[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]] )

for i in arr2:
    for j in i:
        for item in j:
            print(item)
            
for i in arr2:
    print(i)



































