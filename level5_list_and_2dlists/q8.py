# Q8. Count positive and negative numbers.

numbers = [-10, 20, -5, 0, 15, -8, 30]

positive_count = 0
negative_count = 0

for num in numbers:

    if num > 0:
        positive_count += 1
    elif num < 0:
        negative_count += 1

print("Positive numbers =", positive_count)
print("Negative numbers =", negative_count)