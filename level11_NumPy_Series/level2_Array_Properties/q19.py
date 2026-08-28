# Q19. Create a 2D array and convert it into a 1D array using flatten().

import numpy as np

arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

new_arr = arr.flatten()

print("2D array:")
print(arr)

print("1D array:")
print(new_arr)