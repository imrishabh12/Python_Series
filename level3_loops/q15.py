# Q15. Generate the first N Fibonacci numbers.

n = int(input("Enter N: "))

a = 0
b = 1

for i in range(n):
    print(a, end=" ")
    
    next_num = a + b
    a = b
    b = next_num