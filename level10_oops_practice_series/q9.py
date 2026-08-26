# Q9. Create a static method.

class Calculator:

    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def multiply(a, b):
        return a * b


print("Addition:", Calculator.add(10, 20))
print("Multiplication:", Calculator.multiply(10, 20))