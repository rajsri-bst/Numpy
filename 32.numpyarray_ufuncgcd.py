# Finding GCD (Greatest Common Denominator)
#The GCD (Greatest Common Denominator), also known as HCF (Highest Common Factor) is the biggest number that is a common factor of both of the numbers.

import numpy as np
x=4
y=8
print(np.gcd(x,y))

# Finding GCD in Arrays
#To find the Highest Common Factor of all values in an array, you can use the reduce() method.

#The reduce() method will use the ufunc, in this case the gcd() function, on each element, and reduce the array by one dimension.

import numpy as np
x=np.array([4,5,6,7])
arr=np.gcd.reduce(x)
print(arr)