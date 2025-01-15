import math

def degrees_to_radians(degrees):
    return math.radians(degrees)

def main():
    degrees = 15
    radians = degrees_to_radians(degrees)
    print(f"Degree: {degrees}")
    print(f"Expected Result in radians: {radians}")

if __name__ == "__main__":
    main()
