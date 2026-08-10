class InvalidMarksError(Exception):
    pass
def validate_marks(marks):
    if marks < 0 or marks > 100:
        raise InvalidMarksError(
            "Marks should be between 0 and 100."
)
    return True
try:
    student_marks = float(input("Enter marks: "))
    validate_marks(student_marks)
except ValueError:
    print("Enter marks in numerical format.")
except InvalidMarksError as error:
    print("Invalid marks:", error)
else:
    print("Marks saved successfully.")