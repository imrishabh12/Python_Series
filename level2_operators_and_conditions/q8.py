# Q8. Check whether a character is a vowel or consonant.

character = input("Enter a character: ")

if character.lower() in "aeiou":
    print("Vowel")
else:
    print("Consonant")