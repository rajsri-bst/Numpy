# permutation refers to arrangement of element list [3,2,1] is permutation of [1,2,3] and vice versa

# the numpy random module provide 2 methods - shuffle() and permutation()

# shuffle method makes changes to an original array

from numpy import random
import numpy as np
x=np.array([1,2,3,4,5])
random.shuffle(x)
print(x)

# the permutation method leaves the original array unchanged
# we can create a copy of original array and then permutation 

from numpy import random 
import numpy as np
x=np.array([1,4,5,6,7])
y=random.permutation(x)
print(y)