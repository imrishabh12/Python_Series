# Q6. Find the second-largest element.

numbers = [10, 45, 23, 78, 12, 78]

largest = float("-inf")
second_largest = float("-inf")

for num in numbers:

    if num > largest:
        second_largest = largest
        largest = num

    elif num > second_largest and num != largest:
        second_largest = num

if second_largest == float("-inf"):
    print("No second-largest element")
else:
    print("Second-largest element =", second_largest)