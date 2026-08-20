# Q13. Check whether two strings are anagrams.

text1 = input("Enter first string: ")
text2 = input("Enter second string: ")

text1 = text1.lower().replace(" ", "")
text2 = text2.lower().replace(" ", "")

if sorted(text1) == sorted(text2):
    print("Strings are anagrams")
else:
    print("Strings are not anagrams")