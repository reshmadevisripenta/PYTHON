try:
   number = int(input("Enter a number: "))
   print(100 / number)
except ValueError:
   print("Invalid number.")
except ZeroDivisionError:
   print("Cannot divide by zero.")
except Exception as error:
   print("Unexpected error:", error)