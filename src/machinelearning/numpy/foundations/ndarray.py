import random
import numpy as np
import time 

# creating the np array 
arr_1d = np.array([1,2,3,4,5])
print("1d_array" , end = "\n\n")
print(arr_1d)

arr_2d = np.array([[1,2,3,4] , [4,6,6,7]])
print("2d_array" , end = "\n\n")
print(arr_2d)

# list vs numpy 

py_list = [1,2,3,4]
print("Pyhton list multiplication" , py_list*2)
# Pyhton list multiplication [1, 2, 3, 4, 1, 2, 3, 4]

np_array = np.array([1,2,3])
print("Pyhton numpy multiplication" ,np_array*2)
# Pyhton numpy multiplication [2 4 6]

start = time.time()
py_list = [i*2 for i in range(100000)]
print("\nList operation time : " , time.time() - start)

start = time.time()
np_array = np.arange(100000) *2
print("\nnumpy operation time : " , time.time() - start)

# creating array from scratch 

zeros = np.zeros((3,4))
print(zeros)
print()

ones = np.ones((2,3))
print(ones)
print()

full = np.full((3,3) , 7)
print(full)



# random in numppy 
random  = np.random.random((2,3))
print(random)

sequence  = np.arange(0,10,2)
print(sequence)


# vector , Matrix , tensor 

vector = np.array([1,2,3,4])
print("Vector:" , vector)


matrix = np.array([[1,2,3,4],
                    [9,7,6,5]])
print(matrix)

tensor = np.array([[[1,2],[3,4]],
                    [[5,6], [7,8]]])
print(tensor)  

# Array Properties 

define_np_arraay = np.array([[1,2,3],
                            [4,5,6]])

print(define_np_arraay.shape)
print("Dimensions",define_np_arraay.ndim)
print("Size" , define_np_arraay.size)
print("Dtype", define_np_arraay.dtype)

print("itmeize" , define_np_arraay.itemsize)
# how many bytes one element of a NumPy array occupies in memory.