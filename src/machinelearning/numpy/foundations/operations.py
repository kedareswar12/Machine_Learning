
import numpy as np 


# change the dimensions and the size of the array

array = [[1,2,4], [4,3,2]]
array_before_reshape = np.array(array)
print(array_before_reshape , array_before_reshape.shape)

array_after_reshape= array_before_reshape.reshape((3,2))
print(array_after_reshape , array_after_reshape.shape)


# toflatten the array that is to make the 2d array 

flattend_Array = array_before_reshape.flatten()
print(flattend_Array , flattend_Array.shape)

# indexing inside the array 

arr = np.array([1,2,3,4])
print(arr[3])
print(array_before_reshape[1][1])

# fancy indexing 
arr = np.array([1,2,3,4])
index = [0,2,1]
print(arr[index])
# output-> [1 3 2]