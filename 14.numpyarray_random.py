# What is a Random Number?
#Random number does NOT mean a different number every time. Random means something that can not be predicted logically.

# NumPy offers the random module to work with random numbers.

# Now we generate a random number from 0 to 1

from numpy import random 
x=random.randint(100)
print(x)

# we can also generate a random float number via using rand() from 0 to 1
from numpy import random 
x=random.rand()
print(x)

# you can also generate random array
# we will generate a 1-D array containing a 5 random int from 0 to 100
# The randint() method takes a size parameter where you can specify the shape of an array.

from numpy import random
x=random.randint(100,size=(5))
print(x)

# Generate a 2-D array with 3 rows, each row containing 5 random integers from 0 to 100:

from numpy import random
x=random.randint(100,size=(3,5))
print(x)

# The rand() method also allows you to specify the shape of the array.
# we will generate a 1- D array containing a 5 random float.

from numpy import random
x=random.rand(5)
print(x)

# Generate a 2-D array with 3 rows, each row containing 5 random numbers:

from numpy import random
x = random.rand(3, 5)
print(x)

# Generate Random Number From Array
#The choice() method allows you to generate a random value based on an array of values.

#The choice() method takes an array as a parameter and randomly returns one of the values.

from numpy import random 
x=random .choice([4,3,2,7,8])
print(x)

# Generate a 2-D array that consists of the values in the array parameter (3, 5, 7, and 9):

from numpy import random
x = random.choice([3, 5, 7, 9,2,6,4,3], size=(3, 4))
print(x)