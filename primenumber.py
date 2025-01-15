def is_prime(number):
    if number < 2:
        return False
    
    for i in range(2, int(number ** 0.5) + 1):
        if number % 1 == 0:
            return False
        
    return True

print(is_prime(7))
print(is_prime(10))    