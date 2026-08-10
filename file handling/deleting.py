line_number = int(input("Enter line number to delete: "))
with open("student.txt", "r") as file:
    lines = file.readlines()
if 1 <= line_number <= len(lines):
    del lines[line_number- 1]
with open("student.txt", "w") as file:
    file.writelines(lines)
    print("Line deleted successfully.")
else:
    print("Invalid line number.")