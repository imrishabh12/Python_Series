# Q15. Determine whether a triangle is equilateral, isosceles, or scalene.

side1 = float(input("Enter first side: "))
side2 = float(input("Enter second side: "))
side3 = float(input("Enter third side: "))

if side1 == side2 == side3:
    print("Equilateral triangle")
elif side1 == side2 or side1 == side3 or side2 == side3:
    print("Isosceles triangle")
else:
    print("Scalene triangle")