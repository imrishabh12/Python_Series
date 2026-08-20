# Q8. Count spaces in a string.

text = input("Enter a string: ")

count = 0

for char in text:

    if char == " ":
        count += 1

print("Number of spaces =", count)