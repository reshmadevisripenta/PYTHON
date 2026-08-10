text = "Python@123#Programming!"
special = ""
for character in text:
    if not character.isalnum() and not character.isspace():
        special += character
print(special)