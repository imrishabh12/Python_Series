# Q44 - Perform matrix multiplication between two matrices.

import numpy as np

arr1 = np.array([
    [1, 2],
    [3, 4]
])

arr2 = np.array([
    [5, 6],
    [7, 8]
])

result = np.matmul(arr1, arr2)

print("Matrix 1:")
print(arr1)

print("Matrix 2:")
print(arr2)

print("Matrix multiplication:")
print(result)