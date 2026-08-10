from pathlib import Path
file_path = Path("student.txt")
file_path.write_text("Welcome to Python File Handling.")
content = file_path.read_text()
print(content)