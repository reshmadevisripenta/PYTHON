sentence = input("Enter sentence: ")
words = sentence.split()
shortest = min(words, key=len)
print("Shortest Word:", shortest)