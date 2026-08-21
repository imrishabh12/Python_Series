# Q12. Sort a list without using sort().

numbers = [50, 20, 40, 10, 30]

n = len(numbers)

for i in range(n):

    for j in range(0, n - i - 1):

        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

print("Sorted list =", numbers)