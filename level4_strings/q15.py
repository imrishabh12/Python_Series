# Q15. Reverse every word in a sentence.

sentence = input("Enter a sentence: ")

words = sentence.split()

result = []

for word in words:
    result.append(word[::-1])

result = " ".join(result)

print("Result =", result)