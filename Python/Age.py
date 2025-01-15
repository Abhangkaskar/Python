age1 = int(input("Enter the age of the first person: "))
age2 = int(input("Enter the age of the second person: "))

if age1 > age2:
    oldest = age1
    youngest = age2
else:
    oldest = age2
    youngest = age1
    
    print("Oldest person's age: ", oldest)
    print("Youngest person's age: ", youngest)