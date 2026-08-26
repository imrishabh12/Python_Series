# Q6. Demonstrate instance variables and instance methods.

class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)

    def check_result(self):
        if self.marks >= 40:
            print("Pass")
        else:
            print("Fail")


student1 = Student("Rishabh", 85)
student2 = Student("Rahul", 35)

student1.display()
student1.check_result()

print()

student2.display()
student2.check_result()