def generate_squared_dictionary(N):
    squared_dict = {x: x * x for x in range(1 , N + 1)}
    return squared_dict
if __name__ == "__main__":
    N = 10
    
    squared_dictionary = generate_squared_dictionary(N)
    
    print("Generated Dictionary:")
    print(squared_dictionary)