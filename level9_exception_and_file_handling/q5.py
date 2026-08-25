# Q5. Write student information to a file and then read it back.

name = input("Enter student name: ")
age = input("Enter student age: ")
course = input("Enter student course: ")
marks = input("Enter student marks: ")

with open("student.txt", "w") as file:
    file.write("Name: " + name + "\n")
    file.write("Age: " + age + "\n")
    file.write("Course: " + course + "\n")
    file.write("Marks: " + marks + "\n")

print("\nStudent information:")

with open("student.txt", "r") as file:
    content = file.read()

print(content)