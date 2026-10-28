# Q96 - Replace all odd numbers in a NumPy array with 0.

import numpy as np

arr = np.array([10, 15, 20, 25, 30, 35, 40])

result = np.where(arr % 2 != 0, 0, arr)

print("Original array:", arr)
print("After replacement:", result)