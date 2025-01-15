import math
import random
from decimal import Decimal
from datetime import date, time

def math_example():
    num = 16
    square_root = math.sqrt(num)
    print(f"The square root of {num} is: {square_root}")

def random_example():
    random_number = random.randint(1, 100)
    print(f"Random number between 1 and 100: {random_number}")

def decimal_example():
    num1 = Decimal('10.5')
    num2 = Decimal('2.5')
    result = num1 + num2
    print(f"The sum of {num1} and {num2} is: {result}")

def date_example():
    today = date.today()
    print(f"Today's date: {today}")

def time_example():
    current_time = time(hour=12, minute=30, second=45)
    print(f"Current time: {current_time}")

if __name__ == "__main__":
    math_example()
    random_example()
    decimal_example()
    date_example()
    time_example()
