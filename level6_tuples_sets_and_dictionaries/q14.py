# Q14. Merge two dictionaries.

dict1 = {
    "name": "Rishabh",
    "age": 21
}

dict2 = {
    "course": "B.Tech",
    "marks": 85
}

merged = {**dict1, **dict2}

print("Merged dictionary:", merged)