# Q17. Find the missing number from a list containing numbers from 1 to N.

numbers = [1, 2, 3, 5, 6]

n = 6

expected_sum = 0

for i in range(1, n + 1):
    expected_sum += i

actual_sum = 0

for num in numbers:
    actual_sum += num

missing = expected_sum - actual_sum

print("Missing number =", missing)