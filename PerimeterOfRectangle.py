def calculate_rectangle_properties(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter

length = 5
width = 8

rectangle_area, rectangle_perimeter = calculate_rectangle_properties(length, width)

print("Area:", rectangle_area)
print("Perimeter:", rectangle_perimeter)
