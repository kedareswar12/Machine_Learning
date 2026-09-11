# With strides: one number per axis saying how many bytes to jump to move one step along it. Here that's (32, 8) — 8 bytes to the next column, 32 to the next row.

from re import T
from traceback import print_tb
import numpy as np 

a = np.array([[0,1,2,3],
        [4,5,6,7],
        [8,9,10,11]])

# a[2, 1] = 2×32 + 1×8 = byte 72
# a[2, 1] lives at 2 × 32 + 1 × 8 = 72 bytes in. No searching, no pointers — one multiply-add. That's the whole reason indexing an array is fast and indexing a list of lists isn't.
# memory — never changes · transpose didn't touch a byte
# Now the trick. a.T doesn't move a single byte — it just swaps the strides to (8, 32). Stepping along the new axis 0 now jumps 8 bytes instead of 32. Same memory, different walk, instant no matter how big the array.

# print(a.transpose())

print(a.strides)

print("a[2,1] at byte", 2 * a.strides[0] + 1 * a.strides[1], "->", a[2, 1])

print(a.flags)

"""
flags

 C_CONTIGUOUS : True
  F_CONTIGUOUS : False
  OWNDATA : True
  WRITEABLE : True
  ALIGNED : True
  WRITEBACKIFCOPY : False

"""


# Some operations need a genuine flat C-ordered run of bytes. If your array isn't laid out that way, NumPy has to make one:
print(a.ravel())
print(a.T)
print(a.T.ravel()) 
print(np.ascontiguousarray(a))


# Checking whether two arrays share memory
b= a.base
print(np.shares_memory(a, b))
print(np.may_share_memory(a, b) )


# normal

print(a.T.strides)
print(a.flags["C_CONTIGUOUS"]) #True
print(a.T.flags["C_CONTIGUOUS"])
print(a)
print(np.ascontiguousarray(a))