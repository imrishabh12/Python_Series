# Q8. Create a class method.

class Student:

    school = "ABC School"

    def __init__(self, name):
        self.name = name

    @classmethod
    def change_school(cls, new_school):
        cls.school = new_school


student1 = Student("Rishabh")
student2 = Student("Rahul")

print(Student.school)

Student.change_school("XYZ School")

print(Student.school)