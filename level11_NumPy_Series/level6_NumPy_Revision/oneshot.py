# NumPy Complete Revision Code - Important Functions & Methods in One Place

import numpy as np


# ============================================================
# 1. ARRAY CREATION
# ============================================================

arr = np.array([10, 20, 30, 40, 50])
print("Array:", arr)

zeros = np.zeros(5)
ones = np.ones(5)

range_arr = np.arange(1, 11)
even_arr = np.arange(2, 11, 2)

linear_arr = np.linspace(0, 1, 5)

identity = np.eye(3)

print("Zeros:", zeros)
print("Ones:", ones)
print("Arange:", range_arr)
print("Even numbers:", even_arr)
print("Linspace:", linear_arr)
print("Identity matrix:\n", identity)


# ============================================================
# 2. ARRAY PROPERTIES
# ============================================================

matrix = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print("\nMatrix:\n", matrix)

print("ndim:", matrix.ndim)
print("shape:", matrix.shape)
print("size:", matrix.size)
print("dtype:", matrix.dtype)
print("itemsize:", matrix.itemsize)


# ============================================================
# 3. DATA TYPE CONVERSION
# ============================================================

float_arr = arr.astype(float)
int_arr = float_arr.astype(int)

print("\nFloat array:", float_arr)
print("Integer array:", int_arr)


# ============================================================
# 4. INDEXING
# ============================================================

numbers = np.array([10, 20, 30, 40, 50])

print("\nFirst element:", numbers[0])
print("Last element:", numbers[-1])
print("Third element:", numbers[2])


# 2D indexing

matrix = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print("\nElement at row 2, column 3:", matrix[1, 2])
print("First row:", matrix[0])
print("Last row:", matrix[-1])
print("Last column:", matrix[:, -1])


# ============================================================
# 5. SLICING
# ============================================================

numbers = np.array([10, 20, 30, 40, 50, 60])

print("\nFirst 3:", numbers[:3])
print("Last 3:", numbers[-3:])
print("Every second element:", numbers[::2])
print("Reverse:", numbers[::-1])

print("First 2 rows:\n", matrix[:2])
print("First 2 columns:\n", matrix[:, :2])


# ============================================================
# 6. RESHAPE
# ============================================================

arr = np.arange(1, 13)

matrix = arr.reshape(3, 4)

print("\nOriginal:", arr)
print("Reshaped:\n", matrix)

print("Flatten:", matrix.flatten())
print("Ravel:", matrix.ravel())


# ============================================================
# 7. TRANSPOSE
# ============================================================

print("\nOriginal matrix:\n", matrix)
print("Transpose:\n", matrix.T)


# ============================================================
# 8. COPY vs VIEW
# ============================================================

original = np.array([1, 2, 3, 4])

copy_arr = original.copy()
view_arr = original.view()

copy_arr[0] = 100
view_arr[1] = 200

print("\nOriginal after copy/view:")
print(original)

print("Copy:", copy_arr)
print("View:", view_arr)


# ============================================================
# 9. ELEMENT-WISE MATHEMATICAL OPERATIONS
# ============================================================

a = np.array([10, 20, 30])
b = np.array([2, 4, 5])

print("\nAddition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Power:", a ** 2)

print("Square root:", np.sqrt(a))
print("Absolute:", np.abs(np.array([-10, -20, 30])))


# ============================================================
# 10. AGGREGATE FUNCTIONS
# ============================================================

marks = np.array([70, 80, 90, 60, 85])

print("\nSum:", np.sum(marks))
print("Mean:", np.mean(marks))
print("Median:", np.median(marks))
print("Minimum:", np.min(marks))
print("Maximum:", np.max(marks))

print("Standard deviation:", np.std(marks))
print("Variance:", np.var(marks))

print("Index of maximum:", np.argmax(marks))
print("Index of minimum:", np.argmin(marks))


# ============================================================
# 11. ROW-WISE AND COLUMN-WISE OPERATIONS
# ============================================================

matrix = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print("\nRow sums:", np.sum(matrix, axis=1))
print("Column sums:", np.sum(matrix, axis=0))

print("Row means:", np.mean(matrix, axis=1))
print("Column means:", np.mean(matrix, axis=0))

print("Row maximum:", np.max(matrix, axis=1))
print("Column minimum:", np.min(matrix, axis=0))


# ============================================================
# 12. CONDITIONAL OPERATIONS
# ============================================================

numbers = np.array([10, 25, 30, 45, 50, 65])

print("\nNumbers greater than 30:", numbers[numbers > 30])

print("Even numbers:", numbers[numbers % 2 == 0])

print(
    "Replace values > 30 with 100:",
    np.where(numbers > 30, 100, numbers)
)

print(
    "Pass/Fail:",
    np.where(numbers >= 40, "Pass", "Fail")
)


# ============================================================
# 13. COUNTING CONDITIONS
# ============================================================

print("\nCount > 30:", np.sum(numbers > 30))
print("Count even:", np.sum(numbers % 2 == 0))

print("Any number > 60:", np.any(numbers > 60))
print("All numbers > 5:", np.all(numbers > 5))


# ============================================================
# 14. SORTING
# ============================================================

numbers = np.array([50, 20, 80, 10, 40])

print("\nSorted:", np.sort(numbers))
print("Reverse sorted:", np.sort(numbers)[::-1])

indices = np.argsort(numbers)

print("Sorting indices:", indices)
print("Sorted using indices:", numbers[indices])


# ============================================================
# 15. UNIQUE VALUES
# ============================================================

numbers = np.array([10, 20, 20, 30, 30, 30, 40])

print("\nUnique values:", np.unique(numbers))

unique, counts = np.unique(numbers, return_counts=True)

print("Unique:", unique)
print("Counts:", counts)


# ============================================================
# 16. CONCATENATION
# ============================================================

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

combined = np.concatenate((a, b))

print("\nConcatenated:", combined)


# ============================================================
# 17. STACKING
# ============================================================

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("\nVertical stack:")
print(np.vstack((a, b)))

print("Horizontal stack:")
print(np.hstack((a, b)))


# ============================================================
# 18. SPLITTING
# ============================================================

numbers = np.arange(1, 10)

parts = np.split(numbers, 3)

print("\nOriginal:", numbers)
print("Split:", parts)


# ============================================================
# 19. BROADCASTING
# ============================================================

matrix = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print("\nMatrix + 10:\n", matrix + 10)
print("Matrix * 2:\n", matrix * 2)

row = np.array([1, 2, 3])

print("Matrix + row:\n", matrix + row)


# ============================================================
# 20. MATRIX MULTIPLICATION
# ============================================================

A = np.array([
    [1, 2],
    [3, 4]
])

B = np.array([
    [5, 6],
    [7, 8]
])

print("\nElement-wise multiplication:\n", A * B)

print("Matrix multiplication:\n", A @ B)

print("Matrix multiplication using np.matmul:")
print(np.matmul(A, B))

print("Dot product:")
print(np.dot(A, B))


# ============================================================
# 21. DIAGONAL AND TRACE
# ============================================================

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print("\nDiagonal:", np.diag(matrix))
print("Trace:", np.trace(matrix))


# ============================================================
# 22. RANDOM NUMBERS
# ============================================================

print("\nRandom floats:")
print(np.random.rand(5))

print("Random integers:")
print(np.random.randint(1, 100, 5))

print("Random 2D array:")
print(np.random.rand(3, 3))


# ============================================================
# 23. RANDOM SEED
# ============================================================

np.random.seed(42)

print("\nFixed random numbers:")
print(np.random.randint(1, 100, 5))


# ============================================================
# 24. NORMAL DISTRIBUTION
# ============================================================

random_normal = np.random.normal(
    loc=50,
    scale=10,
    size=5
)

print("\nNormal distribution:")
print(random_normal)


# ============================================================
# 25. NaN HANDLING
# ============================================================

data = np.array([10, 20, np.nan, 40, 50])

print("\nData:", data)

print("Normal mean:", np.mean(data))
print("NaN-safe mean:", np.nanmean(data))
print("NaN-safe sum:", np.nansum(data))
print("NaN-safe min:", np.nanmin(data))
print("NaN-safe max:", np.nanmax(data))


# ============================================================
# 26. NORMALIZATION (0 TO 1)
# ============================================================

marks = np.array([50, 60, 70, 80, 90])

normalized = (
    marks - np.min(marks)
) / (
    np.max(marks) - np.min(marks)
)

print("\nOriginal marks:", marks)
print("Normalized marks:", normalized)


# ============================================================
# 27. CLIPPING VALUES
# ============================================================

numbers = np.array([10, 20, 30, 40, 50])

clipped = np.clip(numbers, 20, 40)

print("\nOriginal:", numbers)
print("Clipped:", clipped)


# ============================================================
# 28. ROUNDING
# ============================================================

numbers = np.array([1.2345, 2.5678, 3.9999])

print("\nRound:", np.round(numbers, 2))
print("Floor:", np.floor(numbers))
print("Ceil:", np.ceil(numbers))


# ============================================================
# 29. EXPONENTIAL AND LOG
# ============================================================

numbers = np.array([1, 2, 3])

print("\nExponential:", np.exp(numbers))
print("Natural log:", np.log(numbers))
print("Log10:", np.log10(numbers))


# ============================================================
# 30. SAVE AND LOAD NUMPY ARRAY
# ============================================================

data = np.array([10, 20, 30, 40, 50])

np.save("data.npy", data)

loaded_data = np.load("data.npy")

print("\nSaved data:", data)
print("Loaded data:", loaded_data)


# ============================================================
# 31. MEMORY / EMPTY ARRAYS
# ============================================================

empty = np.empty(5)

print("\nEmpty array:")
print(empty)


# ============================================================
# 32. INSERT / DELETE
# ============================================================

numbers = np.array([10, 20, 30, 40])

inserted = np.insert(numbers, 2, 99)
deleted = np.delete(numbers, 1)

print("\nOriginal:", numbers)
print("After insert:", inserted)
print("After delete:", deleted)


# ============================================================
# 33. APPEND
# ============================================================

numbers = np.array([10, 20, 30])

appended = np.append(numbers, 40)

print("\nOriginal:", numbers)
print("After append:", appended)


# ============================================================
# 34. MATRIX SHAPE MANIPULATION
# ============================================================

arr = np.arange(1, 13)

print("\nOriginal:", arr)

print("Reshape 2x6:")
print(arr.reshape(2, 6))

print("Reshape 4x3:")
print(arr.reshape(4, 3))

print("Resize:")
print(np.resize(arr, (3, 4)))


# ============================================================
# 35. FINAL MINI EXAMPLE
# ============================================================

students_marks = np.array([
    [80, 75, 90],
    [60, 65, 70],
    [95, 90, 85],
    [50, 55, 60]
])

print("\n========== STUDENT ANALYSIS ==========")

print("Marks:\n", students_marks)

student_average = np.mean(students_marks, axis=1)
subject_average = np.mean(students_marks, axis=0)

print("Student averages:", student_average)
print("Subject averages:", subject_average)

print("Highest mark:", np.max(students_marks))
print("Lowest mark:", np.min(students_marks))

print("Overall average:", np.mean(students_marks))

print(
    "Students above overall average:",
    np.where(student_average > np.mean(students_marks))[0] + 1
)

print(
    "Students who passed:",
    np.where(student_average >= 40)[0] + 1
)

print(
    "Students who failed:",
    np.where(student_average < 40)[0] + 1
)

print("Overall standard deviation:", np.std(students_marks))


# ============================================================
# END OF NUMPY REVISION
# ============================================================

print("\n========== NUMPY REVISION COMPLETE ==========")