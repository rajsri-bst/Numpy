# The main difference between a copy and a view of an array is that the copy is a new array, and the view is just a view of the original array.

#The copy owns the data and any changes made to the copy will not affect original array, and any changes made to the original array will not affect the copy.

#The view does not own the data and any changes made to the view will affect the original array, and any changes made to the original array will affect the view.

import numpy as np
arr=np.array([1,2,3,4])
    
arr1=arr.copy()
arr1[0]=45
print(arr1)
print(arr)

import numpy as np
arr=np.array([1,2,3,4])
arr[0]=45
arr1=arr.copy()

print(arr1)
print(arr)

import numpy as np
x=np.array([1,2,3,4,56])
y=x.view()
y[0]=45
print(y)
print(x)

import numpy as np
x=np.array([1,2,3,4,56])
x[0]=45
y=x.view()

print(y)
print(x)

# check if arrays owns its data

# Every NumPy array has the attribute base that returns None if the array owns the data.

#Otherwise, the base  attribute refers to the original object.

import numpy as np

arr = np.array([1, 2, 3, 4, 5])

x = arr.copy()
y = arr.view()

print(x.base)
print(y.base)