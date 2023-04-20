# iterate the element in 1-D

import numpy as np 
arr=np.array([1,2,3,4])
for i in (arr):
    print(i,end=" ")

# iterate  2-D

import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6]])
for x in arr:
  print(x)


# iterate each element in 2-D


import numpy as np
arr=np.array([[1,2,3],[4,5,6]]) 
for i in arr:
    for j in i:
        print(j,end=" ")   

# iterate  3- D

import numpy as np
arr=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[9,10,11]]])
for i in arr:
    print(i)

# iterate each element in 3- D

import numpy as np
arr=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[9,10,11]]])
for i in arr:
    for j in i:
        for k in j:
           print(k)    

# nditer function- this function is used when we don't know hoe many dimension it have and we have to iterate each element            

import numpy as np
arr=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[9,10,11]]])
for i in np.nditer(arr):
    print(i)

# now we will iterate with different step sizes

import numpy as np
arr=np.array([[1,2,3,4],[5,6,7,8]])
for i in np.nditer(arr[:,::3]):
    print(i,end=" ")    

# Enumerated Iteration Using ndenumerate()
# Enumeration means mentioning sequence number of somethings one by one.

# Sometimes we require corresponding index of the element while iterating, the ndenumerate() method can be used for those usecases.    

import numpy as np
arr=np.array([[1,2,3,4],[5,6,7,8]])
for i,j in np.ndenumerate(arr):
    print(i,j)

import numpy as np
arr=np.array([1,2,3,4])
for i,j in np.ndenumerate(arr):
    print(i,j)    