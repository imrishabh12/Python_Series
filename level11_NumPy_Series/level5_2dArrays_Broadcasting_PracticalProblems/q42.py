# Q42 - Create a 3 × 3 matrix and calculate the sum of each column.

import numpy as np

arr = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

column_sum = np.sum(arr, axis=0)

print("Matrix:")
print(arr)
print("Sum of each column:", column_sum)