def calculate_simple_interest(principal, rate, time):
    interest = (principal * rate * time) / 100
    return interest

# Example usage
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the interest rate: "))
time = float(input("Enter the time period (in years): "))

simple_interest = calculate_simple_interest(principal, rate, time)
print("The simple interest is:", simple_interest)
