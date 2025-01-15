def concatenate_dictionarie(dict1, dict2):
    return {**dict1, **dict2}

if __name__ == "__main__":
    dict1 = {"name": "John", "age": 30}
    dict2 = {"city": "New York", "occupation": "Enginner"}
    
    print("Dictionary 1: ")
    print(dict1)
    
    print("\nDictionary 2: ")
    print(dict2)
    
    concatenated_dict = concatenate_dictionarie(dict1, dict2)
    
    
    print("\nConcatenated Dictionary: ")
    print(concatenated_dict)