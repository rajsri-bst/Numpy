# Products
#To find the product of the elements in an array, use the prod() function.

import numpy as np
arr=np.array([1,2,3,4])
print(np.prod(arr))

import numpy as np
arr=np.array([1,2,3,4])
arr1=np.array([5,6,7,8])
print(np.prod([arr,arr1]))

#Product Over an Axis
#If you specify axis=1, NumPy will return the product of each array.

import numpy as np
arr=np.array([1,2,3,4])
arr1=np.array([5,6,7,8])
print(np.prod([arr,arr1],axis=1))

# Cummulative Product
#Cummulative product means taking the product partially.

#E.g. The partial product of [1, 2, 3, 4] is [1, 1*2, 1*2*3, 1*2*3*4] = [1, 2, 6, 24]

#Perfom partial sum with the cumprod() function.

import numpy as np
arr=np.array([1,2,3,4])

print(np.cumprod(arr))
