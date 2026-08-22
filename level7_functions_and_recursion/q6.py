# Q6. Create a function to reverse a string.

def reverse_string(text):
    reverse = ""

    for char in text:
        reverse = char + reverse

    return reverse


text = input("Enter a string: ")

print("Reversed string =", reverse_string(text))