# Q3. Create a program using try-except-else-finally.

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    result = num1 / num2

except ZeroDivisionError:
    print("Cannot divide by zero")

except ValueError:
    print("Please enter valid numbers")

else:
    print("Result =", result)

finally:
    print("Program execution completed")