# Q90 - Reshape a NumPy array into 2 rows and 4 columns.

import numpy as np

arr = np.arange(1, 9)

result = arr.reshape(2, 4)

print("Original array:", arr)
print("Reshaped array:")
print(result)