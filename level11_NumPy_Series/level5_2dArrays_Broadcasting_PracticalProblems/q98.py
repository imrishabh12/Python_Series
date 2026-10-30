# Q98 - Check whether all elements in a NumPy array are positive.

import numpy as np

arr = np.array([10, 20, 30, 40, 50])

result = np.all(arr > 0)

print("Array:", arr)
print("Are all elements positive?", result)