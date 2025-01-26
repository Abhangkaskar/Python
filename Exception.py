Basic Syntax of Try-Except
try:
    result = 10 / 0
except ZeroDivisionError:
    print("You can't divide by zero!")

Steps for Handling Exceptions
try:
    number = int(input("Enter a number: "))
    print(10 / number)
except ZeroDivisionError:
    print("Division by zero is not allowed.")
except ValueError:
    print("Invalid input! Please enter a number.")

Catching Multiple Exceptions
try:
    num = int(input("Enter a number: "))
    print(10 / num)
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("Please enter a valid number!")

#try:
    num = int(input("Enter a number: "))
    print(10 / num)
except (ZeroDivisionError, ValueError) as e:
    print(f"An error occurred: {e}")

Using else

try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("Invalid input!")
else:
    print(f"The result is: {result}")