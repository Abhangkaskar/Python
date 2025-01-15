number = int(input("Enter a 4-digit number: "))

# Extracting the individual digits
digit1 = number // 1000
digit2 = (number // 100) % 10
digit3 = (number // 10) % 10
digit4 = number % 10

# Reversing the digits
reversed_number = digit4 * 1000 + digit3 * 100 + digit2 * 10 + digit1

print("Original number:", number)
print("Reversed number:", reversed_number)