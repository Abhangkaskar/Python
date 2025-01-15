def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        return None
    else:
        print("No exception occurred.")
        return result
    finally:
        print("Finally block executed.")

if __name__ == "__main__":
    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        
        result = divide_numbers(num1, num2)
        if result is not None:
            print(f"The result of {num1} / {num2} is {result}")
    except ValueError:
        print("Error: Please enter valid integer values.")
