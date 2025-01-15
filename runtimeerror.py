def divide_number(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        return None
    
if __name__ == "__main__":
    try:
        num1 = int(input("Enter the Fist number: "))
        num2 = int(input("Enter the Second number: "))
        
        result = divide_number(num1, num2)
        if result is not None:
            print(f"The result of {num1} / {num2} is {result}")
    except ValueError:
        print("Enter: Please Enter valid integer value.")            
    