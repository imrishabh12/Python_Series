# Q95 - Find all elements in a NumPy array that are divisible by 3.

import numpy as np

arr = np.array([10, 12, 15, 22, 27, 30, 35])

result = arr[arr % 3 == 0]

print("Original array:", arr)
print("Elements divisible by 3:", result)