from pathlib import Path
file_path = Path("student.txt")
if file_path.exists():
    print("File exists.")
else:
    print("File does not exist.")