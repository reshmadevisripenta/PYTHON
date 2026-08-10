try:
    with open("unknown.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("The requested file was not found.")