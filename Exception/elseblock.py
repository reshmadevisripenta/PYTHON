try:
   number1 = int(input("Enter first number: "))
   number2 = int(input("Enter second number: "))
   result = number1 / number2
except ValueError:
   print("Please enter valid numbers.")
except ZeroDivisionError:
   print("Division by zero is not allowed.")
else:
   print("Division result:", result)