student_name = input("Enter student name: ")
course = input("Enter course name: ")
marks = input("Enter marks: ")
with open("student_record.txt", "w") as file:
    file.write("Student Name: " + student_name + "\n")
    file.write("Course: " + course + "\n")
    file.write("Marks: " + marks + "\n")
print("Student record saved successfully.")