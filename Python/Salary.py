salary = float(input("Enter the employee salary:"))
year_of_service = int(input("Enter the employee's year of service: "))

bonus = 0
if year_of_service > 5:
    bonus = 0.05 * salary
    
    print("Net Bonus: ", bonus)