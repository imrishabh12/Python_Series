# Q88 - Convert a NumPy array of integers into floating-point numbers.

import numpy as np

arr = np.array([10, 20, 30, 40, 50])

result = arr.astype(float)

print("Original array:", arr)
print("Converted array:", result)
print("Data type:", result.dtype)