# NumPy Quick Revision

import numpy as np


# 1. CREATE ARRAY

arr = np.array([10, 20, 30, 40, 50])

print(arr)


# 2. CREATE COMMON ARRAYS

print(np.zeros(5))
print(np.ones(5))
print(np.arange(1, 11))
print(np.linspace(0, 1, 5))


# 3. ARRAY INFORMATION

print(arr.ndim)      # dimensions
print(arr.shape)     # shape
print(arr.size)      # total elements
print(arr.dtype)     # data type


# 4. INDEXING

print(arr[0])        # first
print(arr[-1])       # last
print(arr[2])        # third


# 5. SLICING

print(arr[1:4])      # index 1 to 3
print(arr[:3])       # first 3
print(arr[-3:])      # last 3
print(arr[::2])      # every 2nd element


# 6. 2D ARRAY

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print(matrix)


# 7. 2D INDEXING

print(matrix[0, 1])      # row 1, column 2
print(matrix[0])         # first row
print(matrix[:, 0])      # first column
print(matrix[:, -1])     # last column


# 8. RESHAPE

arr = np.arange(1, 13)

matrix = arr.reshape(3, 4)

print(matrix)


# 9. FLATTEN

print(matrix.flatten())


# 10. TRANSPOSE

print(matrix.T)


# 11. BASIC MATH

a = np.array([10, 20, 30])
b = np.array([2, 4, 5])

print(a + b)
print(a - b)
print(a * b)
print(a / b)


# 12. IMPORTANT MATH FUNCTIONS

print(np.sum(a))
print(np.mean(a))
print(np.min(a))
print(np.max(a))
print(np.median(a))
print(np.std(a))


# 13. MAX/MIN INDEX

print(np.argmax(a))
print(np.argmin(a))


# 14. CONDITIONS

arr = np.array([10, 20, 30, 40, 50])

print(arr[arr > 25])
print(arr[arr % 2 == 0])


# 15. WHERE

print(np.where(arr > 25, 1, 0))


# 16. SORT

arr = np.array([40, 10, 50, 20, 30])

print(np.sort(arr))


# 17. UNIQUE

arr = np.array([10, 20, 20, 30, 30, 30])

print(np.unique(arr))


# 18. SUM BY ROW / COLUMN

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(np.sum(matrix, axis=1))   # row sums
print(np.sum(matrix, axis=0))   # column sums


# 19. CONCATENATE

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(np.concatenate((a, b)))


# 20. RANDOM

print(np.random.randint(1, 10, 5))
print(np.random.rand(5))


# 21. MATRIX MULTIPLICATION

A = np.array([
    [1, 2],
    [3, 4]
])

B = np.array([
    [5, 6],
    [7, 8]
])

print(A @ B)


# 22. DATA TYPE CONVERSION

arr = np.array([1, 2, 3])

print(arr.astype(float))


# 23. COPY

copy_arr = arr.copy()

print(copy_arr)