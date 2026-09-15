# Q61 - Find the index of the maximum and minimum elements in a NumPy array.

import numpy as np

arr = np.array([25, 10, 45, 5, 30, 50])

max_index = np.argmax(arr)
min_index = np.argmin(arr)

print("Array:", arr)
print("Index of maximum element:", max_index)
print("Index of minimum element:", min_index)