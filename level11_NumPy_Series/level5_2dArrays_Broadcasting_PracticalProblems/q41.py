# Q41 - Sum of each row

import numpy as np

arr = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

row_sum = np.sum(arr, axis=1)

print("Matrix:")
print(arr)
print("Sum of each row:", row_sum)