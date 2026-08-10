def divide_numbers(number1, number2):
    try:
        result = number1 / number2
        return result
    except ZeroDivisionError:
        return "Cannot divide by zero."
print(divide_numbers(20, 4))
print(divide_numbers(20, 0))