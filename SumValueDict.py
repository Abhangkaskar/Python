def sum_dictionary_values(dictionary):
    total_sum = sum(dictionary.values())
    return total_sum

if __name__ == "__main__":
    my_dictionary = {"a": 10, "b": 20, "c": 30, "d": 40}

    print("Dictionary:")
    print(my_dictionary)

    dictionary_sum = sum_dictionary_values(my_dictionary)

    print("\nSum of all items in the dictionary:", dictionary_sum)
