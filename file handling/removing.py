import os
if os.path.exists("StudentFiles"):
    os.rmdir("StudentFiles")
    print("Directory removed successfully.")
else:
    print("Directory does not exist.")