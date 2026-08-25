# Q4. Read a text file and count its lines, words, and characters.

try:
    with open("sample.txt", "r") as file:
        content = file.read()

    lines = content.splitlines()
    words = content.split()
    characters = len(content)

    print("Number of lines =", len(lines))
    print("Number of words =", len(words))
    print("Number of characters =", characters)

except FileNotFoundError:
    print("File not found")