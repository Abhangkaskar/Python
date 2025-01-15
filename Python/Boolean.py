set_var = set()
print(type(set_var))
set_var = {1,2,3,4}
print(set_var)
set_var.add(5)
print(set_var)

set2={ 5, 10,9,11,12}
set_var.intersection_update(set2)
print(set_var)