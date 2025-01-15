def perfect_number(number):
    factor_sum = sum([i for i in range(1, number) if number % i == 0])
    return factor_sum == number

def find_perfect_numbers():
    perfect_numbers = []
    for number in range(1, 1001):
        if perfect_number(number):
            perfect_numbers.append(number)
    return perfect_numbers

perfect_numbers = find_perfect_numbers()
print("Perfect numbers between 1 and 1000:")
print(perfect_numbers)
