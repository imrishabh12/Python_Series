# Q47 - Given an array of student marks, find the average marks, highest marks, lowest marks, and students scoring above average.

import numpy as np

marks = np.array([65, 80, 45, 90, 72, 55, 88, 40])

average = np.mean(marks)
highest = np.max(marks)
lowest = np.min(marks)

above_average = marks[marks > average]

print("Marks:", marks)
print("Average marks:", average)
print("Highest marks:", highest)
print("Lowest marks:", lowest)
print("Students scoring above average:", above_average)