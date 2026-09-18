# Q64 - Create a NumPy array and change all negative values to 0.

import numpy as np

arr = np.array([-10, 20, -5, 30, -15, 40])

result = np.where(arr < 0, 0, arr)

print("Original array:", arr)
print("After replacing negatives:", result)