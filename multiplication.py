def print_multiplication_table(num, count):
    if count > 10:
        return
    else:
        result = num * count
        print(f"{num} x {count} = {result}")
        print_multiplication_table(num, count + 1)
        
print_multiplication_table(12,1)