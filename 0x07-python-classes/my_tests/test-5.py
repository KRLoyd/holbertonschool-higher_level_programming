#!/usr/bin/python3
Square = __import__('5-square').Square

my_square = Square(3)
my_square.my_print()

print("--")

my_square.size = 10
my_square.my_print()

print("--")

my_square.size = 0
my_square.my_print()

print("--")

try:
    my_square.size = True
    my_square.my_print()
except Exception as e:
    print(e)

try:
    my_square.size = -1
    my_square.my_print()
except Exception as e:
    print(e)

try:
    my_square.size = "hey you"
    my_square.my_print()
except Exception as e:
    print(e)
