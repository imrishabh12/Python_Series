# Q11. Create a Person -> Student inheritance example.

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person(self):
        print("Name:", self.name)
        print("Age:", self.age)


class Student(Person):

    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course

    def display_student(self):
        print("Course:", self.course)


student = Student("Rishabh", 21, "B.Tech")

student.display_person()
student.display_student()