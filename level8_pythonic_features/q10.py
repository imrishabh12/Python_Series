# Q10. Sort a list of dictionaries using sorted() and a lambda key.

students = [
    {"name": "Rishabh", "marks": 85},
    {"name": "Rahul", "marks": 92},
    {"name": "Aman", "marks": 78},
    {"name": "Rohit", "marks": 88}
]

sorted_students = sorted(students, key=lambda student: student["marks"])

for student in sorted_students:
    print(student)