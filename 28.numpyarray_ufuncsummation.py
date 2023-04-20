# Summations
#What is the difference between summation and addition?

#Addition is done between two arguments whereas summation happens over n elements

import numpy as np
x=np.array([1,2,3,4])
y=np.array([5,6,7,8])
arr=np.sum([x,y])
print(arr)

# Summation Over an Axis
#If you specify axis=1, NumPy will sum the numbers in each array.

import numpy as np
x=np.array([1,2,3,4])
y=np.array([5,6,7,8])
arr=np.sum([x,y],axis=1)
print(arr)

# Cummulative Sum
#Cummulative sum means partially adding the elements in array.

#E.g. The partial sum of [1, 2, 3, 4] would be [1, 1+2, 1+2+3, 1+2+3+4] = [1, 3, 6, 10].

#Perfom partial sum with the cumsum() function.

import numpy as np
x=np.array([1,2,3,4])
arr=np.cumsum(x)
print(arr)

