# Q10. Check whether a number is a multiple of 3 or 7.

num = int(input("Enter a number: "))

if num % 3 == 0 or num % 7 == 0:
    print("Number is a multiple of 3 or 7")
else:
    print("Number is not a multiple of 3 or 7")