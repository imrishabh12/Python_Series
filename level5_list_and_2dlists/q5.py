# Q5. Find the smallest element in a list.

numbers = [10, 45, 23, 78, 12]

smallest = numbers[0]

for num in numbers:
    if num < smallest:
        smallest = num

print("Smallest element =", smallest)