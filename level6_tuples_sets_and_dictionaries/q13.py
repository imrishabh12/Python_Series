# Q13. Find the key having the maximum value.

marks = {
    "Rishabh": 85,
    "Rahul": 92,
    "Aman": 78,
    "Rohit": 88
}

maximum_key = max(marks, key=marks.get)

print("Key with maximum value:", maximum_key)
print("Maximum value:", marks[maximum_key])