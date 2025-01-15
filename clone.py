def clone_tuple(original_tuple):
    cloned_tuple = tuple(original_tuple)
    return cloned_tuple

original_tuple = (1,2,3,4)
cloned_tuple = clone_tuple(original_tuple)

print("Original Tuple: ", original_tuple)
print("Cloned Tuple: ", cloned_tuple)