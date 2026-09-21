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


# numpy array 
# pass the list in the numpy array function

numpy_array = np.array([1,2,3,4,5])
print(numpy_array , type(numpy_array))
# 1D Array ->  (Vector)

# 2D Array (Matrix)
matrix_list = [[1, 2, 3], [4, 5, 6]]
numpy_list2d = np.array(matrix_list)
print(numpy_list2d)


# passing the type inside the array fxn 
float_arr = np.array([1, 2, 3], dtype=float)

print(float_arr , type(float_arr))

# Specify 32-bit integers
int32_arr = np.array([10, 20, 30], dtype=np.int32)
print(int32_arr.dtype)


"""
notes 
------------

* Standard Python lists that can store mixed types
* NumPy arrays require all elements to be of the same type
* If you pass mixed types, NumPy will automatically upcast everything to a common type


"""

# create a 2d array matrix

arr2d = np.array([[1,2,3] ,[4,5,6] ,[7,8,9]])
print(arr2d.shape)


print(arr2d.itemsize)
# to get the complete size of the array 
print(arr2d.nbytes)