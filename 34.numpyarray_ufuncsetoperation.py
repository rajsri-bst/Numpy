# What is a Set
#A set in mathematics is a collection of unique elements.

#Sets are used for operations involving frequent intersection, union and difference operations.

# Create Sets in NumPy
#We can use NumPy's unique() method to find unique elements from any array. E.g. create a set array, but remember that the set arrays should only be 1-D arrays.

import numpy as np
x=np.array([1,1,1,2,3,2,3,34,7,8,4,5,7,8])
print(np.unique(x))

# Finding Union
#To find the unique values of two arrays, use the union1d() method.

import numpy as np
x=np.array([4,5,6])
y=np.array([1,2,3])
print(np.union1d(x,y))

# Finding Intersection
# To find only the values that are present in both arrays, use the intersect1d() method.

import numpy as np
x=np.array([4,5,1,2,6])
y=np.array([1,2,3])
print(np.intersect1d(x,y))


# Finding Difference
#To find only the values in the first set that is NOT present in the seconds set, use the setdiff1d() method.

import numpy as np
x=np.array([4,5,1,2,6])
y=np.array([1,2,3])
print(np.setdiff1d(x,y))


# Finding Symmetric Difference
#To find only the values that are NOT present in BOTH sets, use the setxor1d() method.

import numpy as np
x=np.array([4,5,1,2,6])
y=np.array([1,2,3])
print(np.setxor1d(x,y))
