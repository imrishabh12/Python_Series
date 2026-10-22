# Q93 - Find the union of two NumPy arrays without duplicate elements.

import numpy as np

arr1 = np.array([10, 20, 30, 40])
arr2 = np.array([30, 40, 50, 60])

result = np.union1d(arr1, arr2)

print("Array 1:", arr1)
print("Array 2:", arr2)
print("Union:", result)