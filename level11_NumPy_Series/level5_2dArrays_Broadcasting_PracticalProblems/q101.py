# Q101 - Find the unique elements from a NumPy array and sort them in ascending order.

import numpy as np

arr = np.array([40, 20, 10, 30, 20, 40, 50, 10])

result = np.unique(arr)

print("Original array:", arr)
print("Unique sorted elements:", result)