# reshape- the adding or removing of element or dimension

# reshaping from 1-D to 2-D

import numpy as np
arr=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(arr.reshape(4,3))

import numpy as np
arr=np.array([1,2,3,4,5,6,7,8])
print(arr.reshape(4,2))

# reshaping from 1-D to 3-D

import numpy as np
arr=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(arr.reshape(2,3,2))

# to check copy or a view
# if it return None then it is copy
# if it return original array then it is view

import numpy as np
arr=np.array([1,2,3,4,5,6,7,8])
print(arr.reshape(2,4).base)

# Flattening the arrays- it means that we convert multidimensional array into 1-D arrays
# we can use reshape(-1) to do this
import numpy as np
arr=np.array([[1, 2, 3], [4, 5, 6]])
print(arr.reshape(-1))