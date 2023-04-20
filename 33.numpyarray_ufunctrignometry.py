#Trigonometric Functions
#NumPy provides the ufuncs sin(), cos() and tan() that take values in radians and produce the corresponding sin, cos and tan values.

import numpy as np
x=np.sin(np.pi/2)
print(x)
y=np.cos(np.pi/4)
print(y)

# Find sine values for all of the values in arr:

import numpy as np
arr = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])
x = np.sin(arr)
print(x)


# Convert Degrees Into Radians
#By default all of the trigonometric functions take radians as parameters but we can convert radians to degrees and vice versa as well in NumPy.

import numpy as np
arr=np.array([45,60,90])
print(np.deg2rad(arr))

# Radians to Degrees

import numpy as np
arr = np.array([np.pi/2, np.pi, 1.5*np.pi, 2*np.pi])
x = np.rad2deg(arr)
print(x)

# Finding Angles
#Finding angles from values of sine, cos, tan. E.g. sin, cos and tan inverse (arcsin, arccos, arctan).

#NumPy provides ufuncs arcsin(), arccos() and arctan() that produce radian values for corresponding sin, cos and tan values given.

import numpy as np
x = np.arcsin(1.0)
print(x)

# Hypotenues
#Finding hypotenues using pythagoras theorem in NumPy.

#NumPy provides the hypot() function that takes the base and perpendicular values and produces hypotenues based on pythagoras theorem.
import numpy as np
x=3
y=4
arr=np.hypot(x,y)
print(arr)