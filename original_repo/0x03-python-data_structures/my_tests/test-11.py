#!/usr/bin/python3
delete_at = __import__('11-delete_at').delete_at

# Holberton test
my_list = [1, 2, 3, 4, 5]
idx = 3
new_list = delete_at(my_list, idx)
print("idx: ", idx)
print(new_list)
print(my_list)

# empty list
my_list = []
idx = 3
new_list = delete_at(my_list, idx)
print("idx: ", idx)
print(new_list)
print(my_list)

# idx is 0
my_list = [1, 2, 3, 4, 5]
idx = 0
new_list = delete_at(my_list, idx)
print("idx: ", idx)
print(new_list)
print(my_list)

# idx is neg
my_list = [1, 2, 3, 4, 5]
idx = -4
new_list = delete_at(my_list, idx)
print("idx: ", idx)
print(new_list)
print(my_list)

# idx is out of range
my_list = [1, 2, 3, 4, 5]
idx = 98
new_list = delete_at(my_list, idx)
print("idx: ", idx)
print(new_list)
print(my_list)
