# Q9. Search for an element in a list.

numbers = [10, 20, 30, 40, 50]

target = int(input("Enter element to search: "))

found = False

for num in numbers:

    if num == target:
        found = True
        break

if found:
    print("Element found")
else:
    print("Element not found")