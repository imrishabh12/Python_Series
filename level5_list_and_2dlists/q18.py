# Q18. Rotate a list to the left by K positions.

numbers = [1, 2, 3, 4, 5]

k = int(input("Enter K: "))

k = k % len(numbers)

rotated = numbers[k:] + numbers[:k]

print("Left rotated list =", rotated)