try:
    with open("student.txt", "r") as file:
        print(file.read())
except Exception as error:
    print("An error occurred:", error)