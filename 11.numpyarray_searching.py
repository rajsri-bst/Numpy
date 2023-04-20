# searching array-you can search an array for a certain value and return that indexes that get match by using where()

import numpy as np
arr=np.array([1,2,3,4,5,4,7,4,8])
x=np.where(arr==4)
print(x)

# now we will find a indexes where the element is even

import numpy as np
arr=np.array([1,2,3,4,5,6,7,8,9])
x=np.where(arr%2==0)
print(x)

# now we will find a indexes where the element is odd

import numpy as np
arr=np.array([1,2,3,4,5,6,7,8,9])
x=np.where(arr%2==1)
print(x)
for i in x:
    print(i)


# Search Sorted
# There is a method called searchsorted() which performs a binary search in the array, and returns the index where the specified value would be inserted to maintain the search order.

# The searchsorted() method is assumed to be used on sorted arrays.    
# The method starts the search from the left and returns the first index where the number 3 is no longer larger than the next value
import numpy as np

arr=np.array([1,2,4,6])
x=np.searchsorted(arr,3)
print(x)

# Search From the Right Side
# By default the left most index is returned, but we can give side='right' to return the right most index instead
# The method starts the search from the right and returns the first index where the number 5 is no longer less than the next value.
import numpy as np
arr=np.array([1,2,4,6])
x=np.searchsorted(arr,5,side='right')
print(x)

#Multiple Values
# To search for more than one value, use an array with the specified values.
import numpy as np
arr=np.array([1,2,4,6,8,10])
x=np.searchsorted(arr,[3,5,7,9])
print(x)