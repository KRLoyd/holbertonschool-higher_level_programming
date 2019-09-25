#!/usr/bin/python3
new_in_list = __import__('4-new_in_list').new_in_list

# idx = 0
print("TEST CASE: nonempty list, idx = 0")
my_list = [1, 2, 3, 4, 5]
idx = 0
new_element = 100
new_list = new_in_list(my_list, idx, new_element)

print("new_list: ", new_list)
print(" my_list: ", my_list)
print()

# idx = -3
print("TEST CASE: nonempty list, idx = -3")
my_list = [1, 2, 3, 4, 5]
idx = -3
new_element = 101
new_list = new_in_list(my_list, idx, new_element)


print("new_list: ", new_list)
print(" my_list: ", my_list)
print()

# idx = 4
print("TEST CASE: nonempty list, idx = 4")
my_list = [1, 2, 3, 4, 5]
idx = 4
new_element = 102
new_list = new_in_list(my_list, idx, new_element)

print("new_list: ", new_list)
print(" my_list: ", my_list)
print()

# idx = 5
print("TEST CASE: nonempty list, idx = 5")
my_list = [1, 2, 3, 4, 5]
idx = 5
new_element = 103
new_list = new_in_list(my_list, idx, new_element)

print("new_list: ", new_list)
print(" my_list: ", my_list)
print()

# idx = 98
print("TEST CASE: nonempty list, idx = 98")
my_list = [1, 2, 3, 4, 5]
idx = 98
new_element = 104
new_list = new_in_list(my_list, idx, new_element)

print("new_list: ", new_list)
print(" my_list: ", my_list)
print()

# empty list
print("TEST CASE: empty list, idx = 0")
my_list = []
idx = 0
new_element = 105
new_list = new_in_list(my_list, idx, new_element)

print("new_list: ", new_list)
print(" my_list: ", my_list)
print()
