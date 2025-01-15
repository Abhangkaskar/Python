def divide_numbers(a, b):
    try:
        result = a / b
        return result
    except (ZeroDivisionError, ValueError) as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        
        result = divide_numbers(num1, num2)
        if result is not None:
            print(f"The result of {num1} / {num2} is {result}")
    except ValueError:
        print("Error: Please enter valid integer values.")
