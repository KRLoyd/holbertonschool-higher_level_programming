#!/usr/bin/python3
Rectangle = __import__('3-rectangle').Rectangle

my_rectangle = Rectangle(1, 1)
print(my_rectangle.__dict__)
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))
print(str(my_rectangle))
print(repr(my_rectangle))
print(my_rectangle)

print("--")

my_rectangle.width = 10
my_rectangle.height = 3
print(my_rectangle.__dict__)
print()
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))
print(str(my_rectangle))
print(repr(my_rectangle))
print(my_rectangle)

print("--")

my_rectangle.width = 0
my_rectangle.height = 3
print(my_rectangle.__dict__)
print()
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))
print(str(my_rectangle))
print(repr(my_rectangle))
print(my_rectangle)

print("--")


try:
    print("height = negative")
    my_rectangle.width = 10
    my_rectangle.height = -3
    print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))
    print(str(my_rectangle))
    print(repr(my_rectangle))
    print(my_rectangle)

except Exception as e:
    print(e)
print()
print("--")

try:
    print("width = negative")
    my_rectangle.width = -10
    my_rectangle.height = 3
    print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))
except Exception as e:
    print(e)
print()
print("--")

try:
    print("width = string")
    my_rectangle.width = "hello"
    my_rectangle.height = -3
    print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))
except Exception as e:
    print(e)
print()
print("--")

try:
    print("width = string")
    my_rectangle.width = 10
    my_rectangle.height = "yo"
    print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))
except Exception as e:
    print(e)
print()
print("--")

try:
    print("width = list")
    my_rectangle.width = (1, 2, 3, 4)
    my_rectangle.height = -3
    print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))
except Exception as e:
    print(e)
print()
print("--")

try:
    print("height  = dict")
    my_rectangle.width = 10
    my_rectangle.height = {'name':'uhhu'}
    print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))
except Exception as e:
    print(e)
print()
print("--")

try:
    print("width = True")
    my_rectangle.width = True
    my_rectangle.height = 3
    print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))
except Exception as e:
    print(e)
print()
print("--")

try:
    print("width = None")
    my_rectangle.width = None
    my_rectangle.height = 3
    print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))
except Exception as e:
    print(e)
print()
print("--")
