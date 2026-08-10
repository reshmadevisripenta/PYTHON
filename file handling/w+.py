with open("demo.txt", "w+") as file:
    file.write("Python File Handling")
    file.seek(0)
    print(file.read())