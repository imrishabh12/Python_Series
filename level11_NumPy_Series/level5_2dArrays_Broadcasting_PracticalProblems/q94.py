# Q94 - Find the indices that would sort a NumPy array in ascending order.

import numpy as np

arr = np.array([40, 10, 50, 20, 30])

indices = np.argsort(arr)

print("Original array:", arr)
print("Sorting indices:", indices)
print("Sorted array:", arr[indices])