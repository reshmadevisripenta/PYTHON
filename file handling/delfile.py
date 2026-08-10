import os
if os.path.exists("student.txt"):
    os.remove("student.txt")
    print("File deleted successfully.")
else:
    print("File does not exist.")