text = "programming"
result = ""
for character in text:
    if character not in result:
        result += character
print(result)