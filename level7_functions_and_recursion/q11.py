# Q11. Create a function using *args.

def add_numbers(*args):

    total = 0

    for num in args:
        total += num

    return total


print("Sum =", add_numbers(10, 20))
print("Sum =", add_numbers(10, 20, 30))
print("Sum =", add_numbers(10, 20, 30, 40, 50))