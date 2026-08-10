search_word = input("Enter a word to search: ")
with open("student.txt", "r") as file:
    content = file.read()
if search_word.lower() in content.lower():
    print("Word found.")
else:
    print("Word not found.")