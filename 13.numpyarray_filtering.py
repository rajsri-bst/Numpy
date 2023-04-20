#Filtering Arrays
# Getting some elements out of an existing array and creating a new array out of them is called filtering.

#In NumPy, you filter an array using a boolean index list.

#A boolean index list is a list of booleans corresponding to indexes in the array.

#If the value at an index is True that element is contained in the filtered array, if the value at that index is False that element is excluded from the filtered array.

import numpy as np
arr=np.array([41,42,43,44])
x=[True,False,True,False]
y=arr[x]
print(y)

# creating the filter array

import numpy as np
arr=np.array([41,42,43,44])
arr1=[]
for i in arr:
    if i>42:
        arr1.append(True)
    else:
        arr1.append(False)
arr2=arr[arr1]
print(arr2)  

# Create a filter array that will return only even elements from the original array:

import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7])
filter_arr = []
for element in arr:
    if element % 2 == 0:
       filter_arr.append(True)
    else:
       filter_arr.append(False)

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)


# Creating Filter Directly From Array

import numpy as np
arr=np.array([41,42,43,44])
arr1=arr>42
arr2=arr[arr1]
print(arr1)
print(arr2)

# create a filter array that will return only even elements from the original array:

import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7])
filter_arr = arr % 2 == 0
newarr = arr[filter_arr]
print(filter_arr)
print(newarr)
