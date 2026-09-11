# dtype:a fixed-width box, and a rule for what the bits inside it mean.

"""
int8        -> 1 byte  -> -128......127
int16       -> 2 bytes -> -32.......767
int32       -> 4 bytes -> 
int64       -> 8 bytes

dropping the sign of the int8 results to unit8  and this has a range -> 0-255

"""

import numpy as np 

# print(np.array[127])

print(np.array([127], dtype=np.int8))
print(np.array([127], dtype=np.int8)+1)



"""
float16     ~3  significant digits      2 bytes
float32     ~7 digits                   4 bytes
float64     ~16 digits                  8 bytes (the default)

significant digits means - general values 

float16
np.float32(12345678.9)  ~7 -> can store 7 digits only 

but incase of 0.1
Decimal: 0.1
Binary: 0.000110011001100110011... 
                         ↑
                    repeats forever

0.1 + 0.2 == 0.3 → False
np.isclose(0.1 + 0.2, 0.3) → True


| Operation           | Result dtype | Why                        |
| ------------------- | ------------ | -------------------------- |
| `int8 + int64`      | `int64`      | **Widen to fit**           |
| `int32 + float32`   | `float64`    | **Needs range + decimals** |
| `int64 + float64`   | `float64`    | **Floats win**             |
| `float32 + float32` | `float32`    | **No change needed**       |

Smaller → bigger → integer → float

int8 → int32 → int64 → float32 → float64

"""


# .astype() converts explicitly — and always copies. Going the narrow way truncates rather than rounds

print(np.array([[1.2,4.5]]).astype(int)) # -> [1,4]  -> truncated, not rounded
print(np.round([[1.2 , 6.7]]).astype(int))


print(np.iinfo(np.int8)  ,    
np.iinfo(np.uint8)   , 
np.finfo(np.float32)   )

small = np.array([250] , dtype=np.uint8)
print("250 + 10  =  " ,small+10 )
# wraps silently without any error 

