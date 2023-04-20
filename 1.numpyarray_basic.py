
# now we create numpy array object
# the array object in numpy is called ndarray
# array()
import numpy as np
arr=np.array([1,2,3,4])
print(np.__version__)
print(arr)
print(type(arr))

# we can also pass a list,tuple or any array like object with array().and it converted into ndarray

import numpy as np
arr=np.array((1,2,3))
print(arr)
print(type(arr))


# dimension in array- a dimension in arrays is one level of array depth(nested array)

# 0-D Arrays - scalars are the element in an array,each value in an array is a 0-D array.

# Now we will create 0-D array 

import numpy as np
x=np.array(42)
print(x)

 # 1-D array -An array that has 0-D arrays as its elements is called uni-dimensional or 1-D array.

import numpy as np
x=np.array([1,2,3,4,5])
print(x)

# create a 2-D array containing 2 array as it values

import numpy as np
x=np.array([[1,2,3],[4,5,6]])
print(x)


# Now we will create a 3-D array with two 2-D array

import numpy as np

x=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(x)

# ndim attribute that return an integer value which tell how many dimension of array it have

import numpy as np

a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

# when there is need to create any number of dimension of an array then we use ndmin attribute
# we can also check how many dimension of array it have by using variable_name.ndim
import numpy as np
x=np.array([1,2,3,4],ndmin=5)  
print(x)
print("Number of dimension:",x.ndim)