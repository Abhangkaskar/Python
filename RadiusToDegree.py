import math

def radians_to_degrees(radians):
    return math.degrees(radians)

def main():
    radians = 0.52
    degrees = radians_to_degrees(radians)
    print(f"Radian: {radians}")
    print(f"Expected Result in degrees: {degrees}")

if __name__ == "__main__":
    main()
