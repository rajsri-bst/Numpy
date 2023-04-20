# Shape of an array=the number of element each dimension have
# it give output in tuple

import numpy as np
x=np.array([1,2,3,4])
print(x.shape) 

import numpy as np
y=np.array([[1,2,3,4],[5,6,7,8]])
print(y.shape)

import numpy as np
z=np.array([1,2,3,4],ndmin=5)
print(z.shape)