def add_student():
    name = input("Enter student name: ")
    course = input("Enter course: ")
    marks = input("Enter marks: ")
    with open("students.txt", "a") as file:
        file.write(f"{name},{course},{marks}\n")
    print("Student added successfully.")
def view_students():
    try:
        with open("students.txt", "r") as file:
            records = file.readlines()
        if not records:
            print("No student records found.")
            return
        for record in records:
            name, course, marks = record.strip().split(",")
            print("Name:", name)
            print("Course:", course)
            print("Marks:", marks)
            print("-" * 20)
    except FileNotFoundError:
        print("Student file does not exist.")

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        print("Program closed.")
        break
else:
    print("Invalid choice.")