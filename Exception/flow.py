try:
    print("Try block started")
    result = 10 / 0
    print("Try block completed")
except ZeroDivisionError:
    print("Exception handled")
else:
    print("No exception occurred")
finally:
    print("Finally block executed")