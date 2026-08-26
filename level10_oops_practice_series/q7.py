# Q7. Demonstrate class variables.

class Student:

    school = "ABC School"

    def __init__(self, name):
        self.name = name

    def display(self):
        print("Name:", self.name)
        print("School:", Student.school)


student1 = Student("Rishabh")
student2 = Student("Rahul")

student1.display()
student2.display()