# Q50 - Create a NumPy-based Student Marks Analyzer that calculates average, highest, lowest, median, standard deviation, number passed, number failed, and students scoring above average.

import numpy as np

marks = np.array([65, 80, 45, 90, 72, 55, 88, 40, 76, 95])

average = np.mean(marks)
highest = np.max(marks)
lowest = np.min(marks)
median = np.median(marks)
standard_deviation = np.std(marks)

passed = marks[marks >= 40]
failed = marks[marks < 40]

above_average = marks[marks > average]

print("Student Marks:", marks)
print("Average:", average)
print("Highest:", highest)
print("Lowest:", lowest)
print("Median:", median)
print("Standard Deviation:", standard_deviation)
print("Number of students passed:", len(passed))
print("Number of students failed:", len(failed))
print("Students scoring above average:", above_average)