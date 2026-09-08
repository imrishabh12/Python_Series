# Q54 - Find the unique elements in a NumPy array and count how many times each element appears.

import numpy as np

arr = np.array([10, 20, 20, 30, 30, 30, 40, 40])

unique, counts = np.unique(arr, return_counts=True)

print("Original array:", arr)
print("Unique elements:", unique)
print("Count of each element:", counts)