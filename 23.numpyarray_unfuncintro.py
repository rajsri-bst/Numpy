# ufuncs stands for 'universal function' and they are numpy function that operates on ndarray object.

#Why use ufuncs?
# ufuncs are used to implement vectorization in NumPy which is way faster than iterating over elements.

# They also provide broadcasting and additional methods like reduce, accumulate   etc. that are very helpful for computation.

# ufuncs also take additional arguments, like:

#where -boolean array or condition defining where the operations should take place.

#dtype -defining the return type of elements.

#out -output array where the return value should be copied.

#Without ufunc, we can use Python's built-in zip() method:

x=[1,2,3,4]
y=[5,6,7,8]
z=[]
for i,j in zip(x,y):
    z.append(i+j)
print(z)    

# What is Vectorization?
# Converting iterative statements into a vector based operation is called vectorization.

# It is faster as modern CPUs are optimized for such operations.

# with ufunc we use add() function

import numpy as np
x=[1,2,3,4]
y=[5,6,7,8]
z=np.add(x,y)
print(z)