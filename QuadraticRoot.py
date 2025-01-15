import math

def quadratic_roots(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return None
    elif discriminant == 0:
        root = -b / (2*a)
        return root
    else:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return root1, root2

def main():
    a = 25
    b = 64
    c = 36

    roots = quadratic_roots(a, b, c)

    if roots is None:
        print("No real roots.")
    elif isinstance(roots, float):
        print(f"Root of the quadratic function: {roots}")
    else:
        root1, root2 = roots
        print(f"Roots of the quadratic function: {root1} and {root2}")

if __name__ == "__main__":
    main()
