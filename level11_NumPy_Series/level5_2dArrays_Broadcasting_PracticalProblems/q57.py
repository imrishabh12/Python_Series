# Q58 - Find the elements that are greater than the average of a NumPy array.

import numpy as np

arr = np.array([10, 20, 30, 40, 50])

average = np.mean(arr)

above_average = arr[arr > average]

print("Array:", arr)
print("Average:", average)
print("Elements greater than average:", above_average)