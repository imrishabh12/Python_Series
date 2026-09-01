# Q27. Create a 3 × 3 matrix and access the element at row 2, column 3.

import numpy as np

arr = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print("Matrix:")
print(arr)

print("Element at row 2, column 3:", arr[1, 2])