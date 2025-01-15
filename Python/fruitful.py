def reverse_number(number):
    reverse = 0

    while number != 0:
        last_digit = number % 10
        reverse = (reverse * 10) + last_digit
        number = number // 10

    return reverse

# Example usage
number = int(input("Enter a number: "))
reversed_number = reverse_number(number)
print("Reverse of", number, "is", reversed_number)