# Q56 - Use np.where() to replace values greater than 50 with 50.

import numpy as np

arr = np.array([20, 45, 60, 80, 35, 90])

result = np.where(arr > 50, 50, arr)

print("Original array:", arr)
print("After replacing:", result)