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

print("Using nditer() for iteration")

for item in np.nditer(arr2):
    print(item)



# using op_dtypes argument to change datatypes while iterating
    
for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
    print(x)

print("Iterating with different step size")
print("")

arr3 = np.array([[1,2,3,4], [5, 6, 7, 8], [9, 10, 11, 12]])

for item in np.nditer(arr3[:, ::2]):
    print(item)

for item in np.nditer(arr3[:2, ::-1]):
    print(item)

print("Printing last element")
for item in np.nditer(arr3[:3, -1]):
    print(item)

print("Printing last OF 3RD ROW element")
for item in np.nditer(arr3[2:3, -1]):
    print(item)



print("")
print("Using denumerate() : ")

for idx, item in np.ndenumerate(arr3):
    print(idx, item)


























