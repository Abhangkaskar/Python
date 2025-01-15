number = int(input("Enter a number: "))


number_str = str(number)

sum_of_digits = 0

for digit in number_str:
    sum_of_digits += int(digit)

print("Sum of digits:", sum_of_digits)