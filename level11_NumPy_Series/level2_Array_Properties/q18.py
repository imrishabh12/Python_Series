# Q18. Create a 1D array containing numbers from 1 to 12
# and reshape it into a 3 × 4 array.

import numpy as np

arr = np.arange(1, 13)

new_arr = arr.reshape(3, 4)

print("1D array:")
print(arr)

print("3 × 4 array:")
print(new_arr)