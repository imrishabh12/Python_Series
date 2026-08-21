# Q7. Count even and odd numbers in a list.

numbers = [10, 15, 20, 25, 30, 35]

even_count = 0
odd_count = 0

for num in numbers:

    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Even numbers =", even_count)
print("Odd numbers =", odd_count)