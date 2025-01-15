number = int(input("Enter a number to generate its multiplication table: "))

print(f"\nMultiplication Table for {number}:")
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")


#numbers = input("Enter numbers separated by spaces: ").split()
#for num in numbers:
#    print(f"\nMultiplication Table for {num}:")
#    for i in range(1, 11):
#        print(f"{int(num)} x {i} = {int(num) * i}")
