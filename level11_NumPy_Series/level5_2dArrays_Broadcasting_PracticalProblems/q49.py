# Q49 - Normalize an array so that its values are between 0 and 1 using normalized = (x - min) / (max - min).

import numpy as np

arr = np.array([10, 20, 30, 40, 50])

minimum = np.min(arr)
maximum = np.max(arr)

normalized = (arr - minimum) / (maximum - minimum)

print("Original array:", arr)
print("Normalized array:", normalized)