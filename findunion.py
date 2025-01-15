def find_union(list1, list2):
    union_set = set(list1) | set(list2)
    union_list = list(union_set)
    return union_list

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
result = find_union(list1, list2)
print("Union of the two lists:", result)
