# Q103 - Extract the diagonal elements from a 2D NumPy array.

import numpy as np

arr = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

result = np.diag(arr)

print("Original array:")
print(arr)

print("Diagonal elements:", result)