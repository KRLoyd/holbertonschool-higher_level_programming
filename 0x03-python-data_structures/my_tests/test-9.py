#!/usr/bin/python3
max_integer = __import__('9-max_integer').max_integer

# Holberton test
my_list = [1, 90, 2, 13, 34, 5, -13, 3]
max_value = max_integer(my_list)
print("Max: {}".format(max_value))

# empty list
my_list = []
max_value = max_integer(my_list)
print("Max: {}".format(max_value))

# Largest value at end
my_list = [1, 27, 4, 7, 7, 100]
max_value = max_integer(my_list)
print("Max: {}".format(max_value))

# Largest value first
my_list = [101, 87, 3, 56, 2]
max_value = max_integer(my_list)
print("Max: {}".format(max_value))

# Largest value is a negative
my_list = [-1, -3, -89, -9, -10]
max_value = max_integer(my_list)
print("Max: {}".format(max_value))
