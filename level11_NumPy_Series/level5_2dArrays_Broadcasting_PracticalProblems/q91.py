# Q91 - Find the common elements between two NumPy arrays.

import numpy as np

arr1 = np.array([10, 20, 30, 40, 50])
arr2 = np.array([30, 40, 50, 60, 70])

common = np.intersect1d(arr1, arr2)

print("Array 1:", arr1)
print("Array 2:", arr2)
print("Common elements:", common)