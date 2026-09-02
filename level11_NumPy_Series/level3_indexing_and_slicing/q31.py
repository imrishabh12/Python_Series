# Q31. Print the first two rows of a 2D NumPy array using slicing.

import numpy as np

arr = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print("First two rows:")
print(arr[:2])