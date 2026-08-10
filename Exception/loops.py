while True:
    try:
        number = int(input("Enter an integer: "))
        break
    except ValueError:
        print("Invalid input. Please try again.")
print("Valid number entered:", number)