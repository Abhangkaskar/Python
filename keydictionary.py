def add_to_dictionary(dictionary, key, value):
    dictionary[key] = value
    
if __name__ == "__main__":
    my_dictionary ={"name" : "John", "age": 30, "city": "New York"}
    
    print("Original Dictionary: ")
    print(my_dictionary)
    
    new_key = "occupation"
    new_value = "Enginner"
    
    add_to_dictionary(my_dictionary, new_key, new_value)
    
    print("/nUpdated Dictionary")
    print(my_dictionary)