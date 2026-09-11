import random
import numpy as np
from numpy import random

zeros = np.zeros((3,4))
print(zeros)

# range = arange
# if you need the squence in the array 
seq = np.arange(3,9.2)
print(seq)

# if you know the range and then you need to have these amount of values 
linespace = np.linspace(0,10,15)
print(linespace)

# to get the identitty matrix use np.eye
identity = np.eye(4)
print(identity)

x= random.randint(1,500)
print(x)

x = random.rand()
print(x)


"""
random.randint will create the random integer array you need to mention size and the range of values 
random.randint(<range like - 100 > , size=(<5>))
"""
x=random.randint(100, size=(5))

print("This one ",x)

# default_rng() is NumPy's recommended way to create a random number generator.
rng = np.random.default_rng()
print(rng.integers(1,15))

print(rng.integers(1,25,size = 5))

arr = rng.random((2,3))
print(arr)