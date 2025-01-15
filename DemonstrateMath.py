import math

def main():
    number = 16
    sqrt_result = math.sqrt(number)
    print(f"The Square root of {number} is {sqrt_result}")
    
    n = 5
    factorial_result = math.factorial(n)
    print(f"The Factorial of {n} is {factorial_result}")
    
    angle_radians = math.radians(45)
    sine_result = math.sin(angle_radians)
    print(f"The sine of {angle_radians} radian is {sine_result}")
    
    angle_radians = math.radians(30)
    cosine_result = math.cos(angle_radians)
    print(f"The cosine of {angle_radians} radian is {cosine_result}")
    
    number = 2.71828
    log_result = math.log(number)
    print(f"The natural logarithm of {number} is {log_result}")
    
    exponent = 2
    exp_result = math.exp(exponent)
    print(f"The value of e raised to the power of {exponent} is {exp_result}")
    
    num1 = 36
    num2 = 48
    gcd_result = math.gcd(num1, num2)
    print(f"The GCD of {num1} and {num1} is {gcd_result}")
    
    pi_value = math.pi
    e_value = math.e
    print(f"The value of pi is {pi_value}")
    print(f"The value of e is {e_value}")
    
if __name__ == "__main__":
    main()     