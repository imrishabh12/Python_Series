# Q4. Find the largest element in a list.

numbers = [10, 45, 23, 78, 12]

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("Largest element =", largest)