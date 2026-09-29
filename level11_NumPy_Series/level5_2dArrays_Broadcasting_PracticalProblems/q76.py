# Q76 - Round the decimal values in a NumPy array to 2 decimal places.

import numpy as np

arr = np.array([10.256, 20.789, 30.123, 40.567])

result = np.round(arr, 2)

print("Original array:", arr)
print("Rounded array:", result)