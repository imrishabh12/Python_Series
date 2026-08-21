# Q10. Count the frequency of an element.

numbers = [10, 20, 10, 30, 10, 40, 20]

target = int(input("Enter element: "))

count = 0

for num in numbers:

    if num == target:
        count += 1

print("Frequency =", count)