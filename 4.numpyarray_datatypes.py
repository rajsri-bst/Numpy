# data types in numpy
"""
i - integer
b - boolean
u - unsigned integer
f - float
c - complex float
m - timedelta
M - datetime
O - object
S - string
U - unicode string
V - fixed chunk of memory for other type ( void )

"""

# dtype -it return the data types of an array

import numpy as np
arr=np.array([1,2,3,4])
print(arr.dtype)

import numpy as np
arr1=np.array(["a","b","c"])
print(arr1.dtype)

# Creating array with a defined data types

# array() function is used to create an array this function takes an optional argument dtype() that allows us to define the expected data type of the array elements

import numpy as np
arr1=np.array([1,2,3],dtype="f")
print(arr1)

import numpy as np
arr1=np.array(['a','b','c'],dtype='O')
print(arr1)
print(arr1.dtype)

# For i, u, f, S and U we can define size as well.

import numpy as np
arr1=np.array([1,2,3],dtype='i4')
print(arr1)
print(arr1.dtype)

import numpy as np
arr1=np.array([1,2,3],dtype='f2')
print(arr1)
print(arr1.dtype)


# if a type is given in which elements can't be casted then NumPy will raise a ValueError.

# ValueError: In Python ValueError is raised when the type of passed argument to a function is unexpected/incorrect.

"""import numpy as np

arr = np.array(['a', '2', '3'], dtype='i')
print(arr)
"""


#The best way to change the data type of an existing array, is to make a copy of the array with the astype() method.

# The astype() function creates a copy of the array, and allows you to specify the data type as a parameter.

import numpy as np
arr=np.array([0.0,1.0,2.3,4.5])
arr1=arr.astype('i')
print(arr1)


import numpy as np
arr=np.array([0.0,1.0,2.3,4.5])
arr1=arr.astype(int)
print(arr1)

import numpy as np
arr = np.array([1, 0, 3])
newarr = arr.astype(bool)
print(newarr)
print(newarr.dtype)