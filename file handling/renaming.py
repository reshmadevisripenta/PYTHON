import os
if os.path.exists("oldname.txt"):
    os.rename("oldname.txt", "newname.txt")
    print("File renamed successfully.")
else:
    print("File does not exist.")