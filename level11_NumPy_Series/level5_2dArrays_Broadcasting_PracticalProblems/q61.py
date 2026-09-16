# Q62 - Calculate the difference between the maximum and minimum values of a NumPy array.

import numpy as np

arr = np.array([10, 25, 40, 15, 60, 30])

difference = np.max(arr) - np.min(arr)

print("Array:", arr)
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))
print("Difference:", difference)