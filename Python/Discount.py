quantity = int(input("Enter the quantity: "))
one_unit_cost = 100
total_cost = quantity + one_unit_cost

if total_cost > 100:
    discount = 0.1 * total_cost
    discount_cost = total_cost - discount
    print("Total cost (with dicount):", discount_cost)
else:
    print("Total cost:", total_cost)