try:
   number1 = int(input("Enter first number: "))
   number2 = int(input("Enter second number: "))
   result = number1 / number2
except ValueError:
   print("Please enter numbers only.")
except ZeroDivisionError:
   print("The second number cannot be zero.")
else:
   print("Result:", result)
finally:
   print("Thank you for using the calculator.")