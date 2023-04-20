# Finding LCM (Lowest Common Multiple)
#The Lowest Common Multiple is the smallest number that is a common multiple of two numbers.

import numpy as np
x=4
y=6
arr=np.lcm(x,y)
print(arr)

# Finding LCM in Arrays
#To find the Lowest Common Multiple of all values in an array, you can use the reduce() method.

#The reduce() method will use the ufunc, in this case the lcm() function, on each element, and reduce the array by one dimension.

import numpy as np
x=np.array([2,3,4,5])
arr=np.lcm.reduce(x)
print(arr)

# Find the LCM of all values of an array where the array contains all integers from 1 to 10:

import numpy as np
x=np.arange(1,10)
arr=np.lcm.reduce(x)
print(arr)