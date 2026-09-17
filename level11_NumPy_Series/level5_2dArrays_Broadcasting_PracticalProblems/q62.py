# Q62 - Find the median of each row in a 2D NumPy array.

import numpy as np

arr = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

row_median = np.median(arr, axis=1)

print("Array:")
print(arr)

print("Median of each row:", row_median)