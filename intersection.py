def find_intersection(list1, list2):
    intersection_list = [element for element in list1 if element in list2]
    return intersection_list

# Example usage:
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
result = find_intersection(list1, list2)
print("Intersection of the two lists:", result)
