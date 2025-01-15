import math
def calculate_circle_properties(radius):
    area = math.pi * radius**2
    circumference = 2 * math.pi * radius
    return area, circumference

radius = 3.5
circle_area, circle_circumference = calculate_circle_properties(radius)
print("Area: ", circle_area)
print("Circumference: ", circle_circumference)