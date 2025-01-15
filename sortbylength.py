def sort_by_lenth(input_list):
    return sorted(input_list, key=len)

input_list = ["apple", "banna", "orange", "grape", "kiwi", "pear"]
result = sort_by_lenth(input_list)
print("Sorted by list of elements: ", result)