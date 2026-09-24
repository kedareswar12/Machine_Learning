# dtype:a fixed-width box, and a rule for what the bits inside it mean.

"""
int8        -> 1 byte  -> -128......127
int16       -> 2 bytes -> -32.......767
int32       -> 4 bytes -> 
int64       -> 8 bytes


int8        -> 1 byte  -> -128 to 127
int16       -> 2 bytes -> -32,768 to 32,767
int32       -> 4 bytes -> -2,147,483,648 to 2,147,483,647
int64       -> 8 bytes -> -9,223,372,036,854,775,808 to 9,223,372,036,854,775,807

uint8       -> 1 byte  -> 0 to 255
uint16      -> 2 bytes -> 0 to 65,535
uint32      -> 4 bytes -> 0 to 4,294,967,295
uint64      -> 8 bytes -> 0 to 18,446,744,073,709,551,615


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

# print(np.array([129] , dtype=np.int8))

small = np.array([250], dtype=np.uint8)
print("250 + 10 =", small + 10)          # wraps, silently
"""
small = np.array([250], dtype=np.uint8)
print("250 + 10 =", small + 10)          # wraps, silently


np.array([250], dtype=np.uint8) -> ranges from 0 to 255 
if we directly write this this will raise the error 
but use the above case this will wrap you easily 


"""

# adding the floating values in the python numpy is very hard beacuse they required the precision but to get the arrrox results or else the results that is similar that is if we add 2 float values like  (e.g., $0.1 + 0.2 = 0.30000000000000004) like this you need to have the presicion but if you use the `isclose()` function you will not be requied to have this amount of the precision
a = np.array([1.0, 2.00000001, 3.0])
b = np.array([1.0, 2.0,        3.1])

print(np.isclose(a, b))
# Output: [ True  True False]