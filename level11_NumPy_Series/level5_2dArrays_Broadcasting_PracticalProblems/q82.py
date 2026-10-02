# Q82 - Combine two NumPy arrays into a single array using np.concatenate().

import numpy as np

arr1 = np.array([10, 20, 30])
arr2 = np.array([40, 50, 60])

result = np.concatenate((arr1, arr2))

print("Array 1:", arr1)
print("Array 2:", arr2)
print("Combined array:", result)