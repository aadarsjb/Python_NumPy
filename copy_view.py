# Numpy Copy vs View

# copy is new arrauy
# view is just a view of the oiriginal array

#The copy owns the data and any changes made to the copy will not affect original
# array, and any changes made to the original array will not affect the copy.

#The view does not own the data and any changes made to the view will affect the
# original array, and any changes made to the original array will affect the view.


import numpy as np

arr = np.array([1, 2, 3, 4, 5])

x = arr.copy()
y = arr.view()

arr[0] = 42

print(arr)
print(x)
print(y)


































