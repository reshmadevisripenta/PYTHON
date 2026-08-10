with open("student.txt", "r") as first_file:
    content1 = first_file.read()
with open("demo.txt", "r") as second_file:
    content2 = second_file.read()
with open("newfile.txt", "w") as merged_file:
    merged_file.write(content1)
    merged_file.write("\n")
    merged_file.write(content2)
print("Files merged successfully.")