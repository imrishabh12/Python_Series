# Q56 - Find the sum of each column in a 2D NumPy array.

import numpy as np

arr = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

column_sum = np.sum(arr, axis=0)

print("Array:")
print(arr)

print("Sum of each column:", column_sum)