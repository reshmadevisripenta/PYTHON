import logging
logging.basicConfig(
    filename="application.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
try:
    number = int(input("Enter a number: "))
    result = 100 / number
    print(result)
except Exception as error:
    logging.error("An exception occurred", exc_info=True)
    print("An error occurred. Check the log file.")