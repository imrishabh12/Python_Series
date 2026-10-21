# Q92 - Find the elements present in the first array but not in the second.

import numpy as np

arr1 = np.array([10, 20, 30, 40, 50])
arr2 = np.array([30, 40, 60])

result = np.setdiff1d(arr1, arr2)

print("Array 1:", arr1)
print("Array 2:", arr2)
print("Elements only in Array 1:", result)