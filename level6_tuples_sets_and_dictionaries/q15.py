# Q15. Group elements of a list based on a property using a dictionary.

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

groups = {
    "even": [],
    "odd": []
}

for num in numbers:
    if num % 2 == 0:
        groups["even"].append(num)
    else:
        groups["odd"].append(num)

print("Even numbers:", groups["even"])
print("Odd numbers:", groups["odd"])