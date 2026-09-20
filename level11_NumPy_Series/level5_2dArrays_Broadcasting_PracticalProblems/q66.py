# Q66 - Find the sum and average of each row in a 2D NumPy array.

import numpy as np

arr = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

row_sum = np.sum(arr, axis=1)
row_average = np.mean(arr, axis=1)

print("Array:")
print(arr)

print("Row sums:", row_sum)
print("Row averages:", row_average)