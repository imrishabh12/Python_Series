# Q100 - Find the common elements between two NumPy arrays and display them in sorted order.

import numpy as np

arr1 = np.array([50, 20, 30, 10, 40])
arr2 = np.array([30, 60, 20, 70, 50])

common = np.intersect1d(arr1, arr2)

print("Array 1:", arr1)
print("Array 2:", arr2)
print("Common elements:", common)