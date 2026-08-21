# Q16. Find the intersection of two lists.

list1 = [10, 20, 20, 30, 40]
list2 = [20, 20, 30, 50]

intersection = []

for num in list1:

    if num in list2 and num not in intersection:
        intersection.append(num)

print("Intersection =", intersection)