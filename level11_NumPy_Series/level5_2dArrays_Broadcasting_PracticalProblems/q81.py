# Q81 - Count the number of occurrences of each unique element in a NumPy array.

import numpy as np

arr = np.array([10, 20, 10, 30, 20, 10, 40, 30])

values, counts = np.unique(arr, return_counts=True)

print("Original array:", arr)
print("Unique elements:", values)
print("Occurrences:", counts)