with open("student.txt", "r") as file:
    content = file.read()
old_word = input("Enter old word: ")
new_word = input("Enter new word: ")
updated_content = content.replace(old_word, new_word)
with open("student.txt", "w") as file:
    file.write(updated_content)
print("Text replaced successfully.")