def merge_and_sort_list(list1, list2):
    merged_list = list1 + list2
    merged_list.sort()
    return merged_list

list1 = [1, 3, 5, 7, 9]
list2 = [2, 4, 6, 8, 10]
result = merge_and_sort_list(list1, list2)
print("Merged and sorted list: ", result)