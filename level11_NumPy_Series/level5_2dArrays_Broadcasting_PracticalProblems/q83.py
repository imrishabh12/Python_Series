# Q83- Stack two NumPy arrays vertically and horizontally.

import numpy as np

arr1 = np.array([10, 20, 30])
arr2 = np.array([40, 50, 60])

vertical = np.vstack((arr1, arr2))
horizontal = np.hstack((arr1, arr2))

print("Vertical stack:")
print(vertical)

print("Horizontal stack:")
print(horizontal)