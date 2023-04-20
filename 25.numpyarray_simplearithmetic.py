# Simple Arithmetic
#You could use arithmetic operators + - * / directly between NumPy arrays, but this section discusses an extension of the same where we have functions that can take any array-like objects e.g. lists, tuples etc. and perform arithmetic conditionally.

#Arithmetic Conditionally: means that we can define conditions where the arithmetic operation should happen

# Addition
# The add() function sums the content of two arrays, and return the results in a new array.

import numpy as np
x=np.array([1,2,3,4])
y=np.array([5,6,7,8])
print(np.add(x,y))

# Subtraction
# The subtract() function subtracts the values from one array with the values from another array, and return the results in a new array.

import numpy as np
x=np.array([4,5,6,7])
y=np.array([1,2,3,1])
print(np.subtract(x,y))

# Multiplication
# The multiply() function multiplies the values from one array with the values from another array, and return the results in a new array.

import numpy as np
x=np.array([4,5,6,7])
y=np.array([1,2,3,1])
print(np.multiply(x,y))

# Division
# The divide() function divides the values from one array with the values from another array, and return the results in a new array.

import numpy as np
x=np.array([4,5,6,7])
y=np.array([1,2,3,1])
print(np.divide(x,y))

# Power
#The power() function rises the values from the first array to the power of the values of the second array, and return the results in a new array.

import numpy as np
x=np.array([4,5,6,7])
y=np.array([1,2,3,1])
print(np.power(x,y))

# Remainder
#Both the mod() and the remainder() functions return the remainder of the values in the first array corresponding to the values in the second array, and return the results in a new array.

import numpy as np
x=np.array([4,5,6,7])
y=np.array([1,2,3,1])
print(np.mod(x,y))

import numpy as np
x=np.array([4,5,6,7])
y=np.array([1,2,3,1])
print(np.remainder(x,y))

# Quotient and Mod
#The divmod() function return both the quotient and the the mod. The return value is two arrays, the first array contains the quotient and second array contains the mod.

import numpy as np
x=np.array([4,5,6,7])
y=np.array([1,2,3,1])
print(np.divmod(x,y))

# Absolute Values
# Both the absolute() and the abs() functions do the same absolute operation element-wise but we should use absolute() to avoid confusion with python's inbuilt math.abs()

import numpy as np
x=np.array([-1,2,-4,5,6])
print(np.absolute(x))