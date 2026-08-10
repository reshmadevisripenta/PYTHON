with open("student.txt", "r") as source_file:
    content = source_file.read()
with open("demo.txt", "w") as destination_file:
    destination_file.write(content)
print("File copied successfully.")