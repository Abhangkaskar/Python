def find_largest_number(numbers):
    if not numbers:
        return None  
    
    largest = numbers[0]  

    for num in numbers:
        if num > largest:
            largest = num  

    return largest


input_list = [12, 45, 9, 67, 32, 89, 5]
result = find_largest_number(input_list)
print("The largest number in the list is:", result)
