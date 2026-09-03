# Q40 - Index of maximum and minimum elements

import numpy as np

arr = np.array([25, 10, 45, 5, 30])

max_index = np.argmax(arr)
min_index = np.argmin(arr)

print("Index of maximum element:", max_index)
print("Index of minimum element:", min_index)