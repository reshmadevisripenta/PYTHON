from datetime import datetime
student_name = input("Enter student name: ")
current_date = datetime.now().strftime("%d-%m-%Y")
current_time = datetime.now().strftime("%I:%M %p")
with open("attendance.txt", "a") as file:
    file.write(
        f"{student_name},{current_date},{current_time},Present\n"
    )
print("Attendance recorded successfully.")