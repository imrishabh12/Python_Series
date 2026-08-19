# Q10. Reverse a number.

num = int(input("Enter a number: "))

original = num
num = abs(num)

reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10

if original < 0:
    reverse = -reverse

print("Reversed number =", reverse)