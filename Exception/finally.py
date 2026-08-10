try:
   number = int(input("Enter a number: "))
   print(100 / number)
except ValueError:
   print("Invalid input.")
except ZeroDivisionError:
   print("Zero is not allowed.")
finally:
   print("Program execution completed.")