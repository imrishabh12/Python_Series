# Q58 - Count how many elements in a NumPy array are greater than 30.

import numpy as np

arr = np.array([10, 25, 35, 40, 15, 50, 60])

count = np.sum(arr > 30)

print("Array:", arr)
print("Number of elements greater than 30:", count)