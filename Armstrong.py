def is_armstrong(number):
    
    str_number = str(number)
    order = len(str_number)

    
    sum = 0

    
    for digit in str_number:
        sum += int(digit) ** order

    
    if number == sum:
        return True
    else:
        return False


number = int(input("Enter a number: "))

if is_armstrong(number):
    print(number, "is an Armstrong number.")
else:
    print(number, "is not an Armstrong number.")