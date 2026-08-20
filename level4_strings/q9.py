# Q9. Remove all spaces from a string.

text = input("Enter a string: ")

result = ""

for char in text:

    if char != " ":
        result += char

print("String without spaces =", result)