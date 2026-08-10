balance = 10000
try:
    pin = int(input("Enter your PIN: "))
    if pin != 1234:
        raise ValueError("Incorrect PIN.")
    amount = float(input("Enter withdrawal amount: "))
    if amount <= 0:
        raise ValueError("Amount must be greater than zero.")
    if amount > balance:
        raise ValueError("Insufficient account balance.")
    balance -= amount

except ValueError as error:
    print("Transaction failed:", error)
else:
    print("Please collect your cash.")
    print("Available balance:", balance)
finally:
    print("Thank you for using the ATM.")