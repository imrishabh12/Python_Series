# Q48 - Given an array of temperatures, find the average temperature, maximum temperature, minimum temperature, and days where temperature was above average.

import numpy as np

temperatures = np.array([28, 32, 30, 35, 29, 31, 36])

average = np.mean(temperatures)
maximum = np.max(temperatures)
minimum = np.min(temperatures)

above_average = temperatures[temperatures > average]

print("Temperatures:", temperatures)
print("Average temperature:", average)
print("Maximum temperature:", maximum)
print("Minimum temperature:", minimum)
print("Temperatures above average:", above_average)