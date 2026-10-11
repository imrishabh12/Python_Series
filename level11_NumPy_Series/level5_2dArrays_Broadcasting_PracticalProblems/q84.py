# Q84 - Split a NumPy array into 3 equal parts.

import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90])

parts = np.split(arr, 3)

print("Original array:", arr)
print("Part 1:", parts[0])
print("Part 2:", parts[1])
print("Part 3:", parts[2])