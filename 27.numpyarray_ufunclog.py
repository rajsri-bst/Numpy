#Logs
#NumPy provides functions to perform log at the base 2, e and 10.

#We will also explore how we can take log for any base by creating a custom ufunc.

#All of the log functions will place -inf or inf in the elements if the log can not be computed.

# Log at Base 2
#Use the log2() function to perform log at the base 2.

import numpy as np
x=np.arange(1,10)
print(np.log2(x))

#Log at Base 10
# Use the log10() function to perform log at the base 10.
import numpy as np
x=np.arange(1,10)
print(np.log10(x))

# Natural Log, or Log at Base e
#Use the log() function to perform log at the base e.

import numpy as np
x=np.arange(1,10)
print(np.log(x))

