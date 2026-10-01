# Q80 - Find the indices of elements greater than 30 in a NumPy array.

import numpy as np

arr = np.array([10, 40, 20, 50, 30, 60])

indices = np.where(arr > 30)

print("Array:", arr)
print("Indices:", indices[0])