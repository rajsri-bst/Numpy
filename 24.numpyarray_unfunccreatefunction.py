# How To Create Your Own ufunc
#To create your own ufunc, you have to define a function, like you do with normal functions in Python, then you add it to your NumPy ufunc library with the frompyfunc() method.

#The frompyfunc() method takes the following arguments:

#function - the name of the function.
#inputs - the number of input arguments (arrays).
#outputs - the number of output arrays.

import numpy as np
def addnew(x,y):
    return x+y
addnew=np.frompyfunc(addnew,2,1)
print(addnew([1,2,3],[4,5,6]))

# Check if a Function is a ufunc
#Check the type of a function to check if it is a ufunc or not.

#A ufunc should return <class 'numpy.ufunc'>.

import numpy as np 
print(type(np.add))

# If it is not a ufunc, it will return another type, like this built-in NumPy function for joining two or more arrays:

import numpy as np
print(type(np.concatenate))

# If the function is not recognized at all, it will return an error:

'''import numpy as np
print(type(np.blahblah))
'''

#To test if the function is a ufunc in an if statement, use the numpy.ufunc value (or np.ufunc if you use np as an alias for numpy):

import numpy as np
if type(np.add)==np.ufunc:
    print('yes this function is ufunc')
else:
    print("No this function is not ufunc")    