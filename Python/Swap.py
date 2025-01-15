def swap_numbers(num1, num2):
    temp = num1
    num1 = num2
    num2 = temp
    print("After swapping: num1 =", num1, "and num2 =", num2)

number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

print("Before swapping: num1 =", number1, "and num2 =", number2)
swap_numbers(number1, number2)