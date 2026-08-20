# Q6. Count the number of digits in a string.

text = input("Enter a string: ")

count = 0

for char in text:

    if char.isdigit():
        count += 1

print("Number of digits =", count)