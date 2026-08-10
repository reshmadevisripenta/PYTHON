try:
    student_name = input("Enter student name: ").strip()
    if not student_name:
        raise ValueError("Student name cannot be empty.")
    age = int(input("Enter age: "))
    if age < 5 or age > 100:
        raise ValueError("Enter a valid age.")
    email = input("Enter email address: ").strip()
    if "@" not in email or "." not in email:
        raise ValueError("Enter a valid email address.")
except ValueError as error:
    print("Registration failed:", error)
else:
    print("Student registered successfully.")
    print("Name:", student_name)
    print("Age:", age)
    print("Email:", email)
finally:
    print("Registration process completed.")