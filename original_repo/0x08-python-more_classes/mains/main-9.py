#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle

my_square = Rectangle.square(5)
print("Area: {} - Perimeter: {}".format(my_square.area(), my_square.perimeter()))
print(my_square)
print("--")

try:
    my_square = Rectangle.square(-2)
    print("Area: {} - Perimeter: {}".format(my_square.area(), my_square.perimeter()))
    print(my_square)
except Exception as e:
    print(e)
print("--")

try:
    my_square = Rectangle.square(None)
    print("Area: {} - Perimeter: {}".format(my_square.area(), my_square.perimeter()))
    print(my_square)
except Exception as e:
    print(e)

print("--")

try:
    my_square = Rectangle.square()
    print("Area: {} - Perimeter: {}".format(my_square.area(), my_square.perimeter()))
    print(my_square)
except Exception as e:
    print(e)

print("--")
