# Q7. Create a function to check palindrome.

def is_palindrome(text):

    reverse = ""

    for char in text:
        reverse = char + reverse

    return text == reverse


text = input("Enter a string: ")

if is_palindrome(text):
    print("Palindrome")
else:
    print("Not a palindrome")