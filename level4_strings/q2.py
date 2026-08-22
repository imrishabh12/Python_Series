# Q2. Find the length of a string without using len().

text = input("Enter a string: ")

count = 0

for char in text:
    count += 1

print("Length =", count)