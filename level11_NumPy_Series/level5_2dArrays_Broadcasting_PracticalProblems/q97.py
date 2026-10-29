# Q97 - Count the number of positive, negative, and zero elements in a NumPy array.

import numpy as np

arr = np.array([-10, 20, 0, -5, 30, 0, 15])

positive = np.sum(arr > 0)
negative = np.sum(arr < 0)
zeros = np.sum(arr == 0)

print("Array:", arr)
print("Positive elements:", positive)
print("Negative elements:", negative)
print("Zero elements:", zeros)