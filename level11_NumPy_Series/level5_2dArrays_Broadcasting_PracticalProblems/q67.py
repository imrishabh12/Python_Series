# Q67 - Find the maximum value of each row and each column in a 2D NumPy array.

import numpy as np

arr = np.array([
    [10, 25, 30],
    [45, 50, 20],
    [70, 15, 90]
])

row_max = np.max(arr, axis=1)
column_max = np.max(arr, axis=0)

print("Array:")
print(arr)

print("Maximum of each row:", row_max)
print("Maximum of each column:", column_max)