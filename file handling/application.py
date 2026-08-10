from datetime import datetime
message = input("Enter log message: ")
timestamp = datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")
with open("application.log", "a") as file:
    file.write(f"{timestamp} - {message}\n")
print("Log saved successfully.")