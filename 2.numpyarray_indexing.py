import numpy as np
arr=np.array([1,2,3,4])
print(arr[0])

arr1=np.array([[1,2,3],[4,5,6]])
print(arr1[0,2])

arr2=np.array([[[1,2,3],[4,5,6]],[[6,7,8],[8,9,2]]])
print(arr2[1,1,2])

# we can also do a negative indexing
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('Last element from 2nd dim: ', arr[0, -2])
