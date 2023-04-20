# There are primarily five ways of rounding off decimals in NumPy:

#truncation
#fix
#rounding
#floor
#ceil

# Truncation
#Remove the decimals, and return the float number closest to zero. Use the trunc() and fix() functions.

import numpy as np
arr = np.trunc([-3.56,25.6667])
print(arr)

import numpy as np
arr = np.fix([-3.1666, 3.6667])
print(arr)

#Rounding
#The around() function increments preceding digit or decimal by 1 if >=5 else do nothing.

import numpy as np
arr=np.around(3.166,1)
print(arr)

#Floor
# The floor() function rounds off decimal to nearest lower integer.
import numpy as np
arr=np.floor([-3.1666, 3.6667])
print(arr)

#Ceil
#The ceil() function rounds off decimal to nearest upper integer.

import numpy as np
arr=np.ceil([-3.1666, 3.6667])
print(arr)