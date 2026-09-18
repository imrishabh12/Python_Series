# Q65 - Count how many even numbers are present in a NumPy array.

import numpy as np

arr = np.array([10, 15, 20, 25, 30, 35, 40])

count = np.sum(arr % 2 == 0)

print("Array:", arr)
print("Number of even elements:", count)