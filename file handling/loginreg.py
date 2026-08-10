def register_user():
    username = input("Create username: ")
    password = input("Create password: ")
    with open("users.txt", "a") as file:
        file.write(f"{username},{password}\n")
    print("Registration successful.")

def login_user():
    username = input("Enter username: ")
    password = input("Enter password: ")
    try:
        with open("users.txt", "r") as file:
            users = file.readlines()
        for user in users:
            saved_username, saved_password = user.strip().split(",")
            if username == saved_username and password == saved_password:
                print("Login successful.")
                return
        print("Invalid username or password.")
    except FileNotFoundError:
        print("No registered users found.")
register_user()
login_user()