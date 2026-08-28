# Q17. Create a float array and convert it to an integer array.

import numpy as np

arr = np.array([1.5, 2.7, 3.9, 4.2, 5.8])

int_arr = arr.astype(int)

print("Float array:", arr)
print("Integer array:", int_arr)