# Q2. Handle invalid user input using exception handling.

try:
    num = int(input("Enter a number: "))

    print("You entered:", num)

except ValueError:
    print("Invalid input. Please enter a number.")