# Q20. Create an array of 24 numbers and reshape it into a 2 × 3 × 4 array.

import numpy as np

arr = np.arange(1, 25)

new_arr = arr.reshape(2, 3, 4)

print("Array:")
print(new_arr)