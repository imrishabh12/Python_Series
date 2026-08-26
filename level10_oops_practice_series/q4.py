# Q4. Create a Rectangle class that calculates area and perimeter.

class Rectangle:

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


rectangle = Rectangle()

rectangle.length = 10
rectangle.width = 5

print("Area =", rectangle.area())
print("Perimeter =", rectangle.perimeter())