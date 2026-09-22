# Q68 - Find the minimum value of each row and each column in a 2D NumPy array.

import numpy as np

arr = np.array([
    [10, 25, 30],
    [45, 50, 20],
    [70, 15, 90]
])

row_min = np.min(arr, axis=1)
column_min = np.min(arr, axis=0)

print("Array:")
print(arr)

print("Minimum of each row:", row_min)
print("Minimum of each column:", column_min)