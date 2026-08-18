# Q5. Find the greatest of three numbers.

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

if num1 >= num2 and num1 >= num3:
    print("Greatest number =", num1)
elif num2 >= num1 and num2 >= num3:
    print("Greatest number =", num2)
else:
    print("Greatest number =", num3)