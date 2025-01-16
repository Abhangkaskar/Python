try:
    number = int(input("Enter a number: "))
    if number % 2 ==0:
        print(f"{number} is an Even number.")
    else:
        print(f"{number} is an Odd number.")
except ValueError:
    print("Invalid input! Please enter a valid integer.")
    
while True:
    number = int(input("Enter a number: "))
    if number % 2 ==0:
        print(f"{number} is an Even number.")
    else:
        print(f"{number} is an Odd number.")
        
    choice = input("Do you want to check another number> (yes/no): ").lower()
    if choice != 'yes':
        print("Goodbye!")
        break