# Q16. Create an integer array and convert it to a float array.

import numpy as np

arr = np.array([1, 2, 3, 4, 5])

float_arr = arr.astype(float)

print("Integer array:", arr)
print("Float array:", float_arr)