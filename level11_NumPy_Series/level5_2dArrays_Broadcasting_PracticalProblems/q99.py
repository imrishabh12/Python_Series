# Q99 - Find the cumulative product of all elements in a NumPy array.

import numpy as np

arr = np.array([2, 3, 4, 5])

result = np.cumprod(arr)

print("Original array:", arr)
print("Cumulative product:", result)