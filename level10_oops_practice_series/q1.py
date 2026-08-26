# Q1. Create a Student class with name and age.

class Student:

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)


student = Student()

student.name = "Rishabh"
student.age = 21

student.display()