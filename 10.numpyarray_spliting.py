# spliting of array - it is reverse of joining,breaking the array

# spliting of an array into 3 parts

import numpy as np
arr=np.array([1,2,3,4,5,6])
arr1=np.array_split(arr,3)
print(arr1)


# spliting of array into 4 parts

import numpy as np
arr=np.array([1,2,3,4,5,6])
arr1=np.array_split(arr,4)
print(arr1)

# split of array with index
import numpy as np
arr=np.array([1,2,3,4,5,6])
arr1=np.array_split(arr,4)
print(arr1[0])
print(arr1[1])
print(arr1[2])
print(arr1[3])

# Split the 2-D array into three 2-D arrays.

import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newarr = np.array_split(arr, 3)
print(newarr)

# Split the 2-D array into three 2-D arrays along rows.

import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newarr = np.array_split(arr, 3, axis=1)
print(newarr)

# Use the hsplit() method to split the 2-D array into three 2-D arrays along rows.

import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newarr = np.hsplit(arr, 3)
print(newarr)
