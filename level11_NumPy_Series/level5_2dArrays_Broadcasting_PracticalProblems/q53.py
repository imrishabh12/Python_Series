# Q55 - Sort a NumPy array in ascending and descending order.

import numpy as np

arr = np.array([50, 20, 80, 10, 40, 30])

ascending = np.sort(arr)
descending = np.sort(arr)[::-1]

print("Original array:", arr)
print("Ascending:", ascending)
print("Descending:", descending)