def key_exists_in_dictionary(dictionary, key):
    return key in dictionary

if __name__ == "__main__":
    my_dictionary = {"name": "John", "age": 30, "city": "New York"}

    print("Dictionary:")
    print(my_dictionary)

    key_to_check = "age"
    if key_exists_in_dictionary(my_dictionary, key_to_check):
        print(f"\nThe key '{key_to_check}' exists in the dictionary.")
    else:
        print(f"\nThe key '{key_to_check}' does not exist in the dictionary.")
