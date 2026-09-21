
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


#  in slicing of arrayys in numpy u willl see the copy of list is cretaed but when you see in numpy it creates the view 
# when ever you are perforning the array slicing operatiosn it will also be created in the main array 

python_list = [10, 20, 30, 40, 50]
list_slice = python_list[1:4]  # Creates a NEW list [20, 30, 40]

list_slice[0] = 999  # Modify the slice

print(python_list)  # [10, 20, 30, 40, 50] (Original is UNCHANGED)
print(list_slice)    # [999, 30, 40]



import numpy as np

np_array = np.array([10, 20, 30, 40, 50])
arr_slice = np_array[1:4]  # Creates a VIEW pointing to index 1, 2, and 3

arr_slice[0] = 999  # Modify the slice

print(np_array)  # [ 10 999  30  40  50] (Original IS MODIFIED!)
print(arr_slice) # [999  30  40]



a = np.array([1, 2, 3, 4, 5])
b = a[1:4]

print(b.base is a)  # True -> 'b' is a view of 'a'

# what if you need a independent copy 
np_array = np.array([10, 20, 30, 40, 50])

# Force an actual copy in memory
independent_slice = np_array[1:4].copy()

independent_slice[0] = 999

print(np_array)           # [10, 20, 30, 40, 50] (Original remains unchanged)
print(independent_slice)  # [999, 30, 40]
print(independent_slice.base)  # None