# Q15. Create a 2D array and display ndim, shape, size, and dtype.

import numpy as np

arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print("Array:")
print(arr)

print("ndim:", arr.ndim)
print("shape:", arr.shape)
print("size:", arr.size)
print("dtype:", arr.dtype)