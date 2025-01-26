def reverse_string(input_string):
    return input_string[::-1]

user_input = input("Enter a string to reverse: ")

reversed_string = reverse_string(user_input)
print(f"Reversed string: {reversed_string}")