my_set ={1, 2, 3, 4, 5}

try:
    my_set.remove(3)
    print("After removing 3 using remove(): ", my_set)
except KeyError:
    print("Item not found in the set.")
    
my_set.discard(4)
print("After removing 4 using discard():", my_set)

my_set.discard(10)
print("After removing 10 using discard():", my_set)        