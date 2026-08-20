# Q14. Find the largest word in a sentence.

sentence = input("Enter a sentence: ")

words = sentence.split()

largest_word = ""

for word in words:

    if len(word) > len(largest_word):
        largest_word = word

print("Largest word =", largest_word)