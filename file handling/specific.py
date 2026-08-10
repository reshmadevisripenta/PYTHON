line_number = int(input("Enter line number: "))
with open("student.txt", "r") as file:
    lines = file.readlines()
if 1 <= line_number <= len(lines):
    print(lines[line_number- 1])
else:
    print("Invalid line number.")