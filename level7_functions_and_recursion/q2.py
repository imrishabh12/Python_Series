# Q2. Create a function to check even/odd.

def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"


num = int(input("Enter a number: "))

print(check_even_odd(num))