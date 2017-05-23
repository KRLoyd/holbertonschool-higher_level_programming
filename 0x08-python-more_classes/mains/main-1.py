#!/usr/bin/python3
Rectangle = __import__('1-rectangle').Rectangle

my_rectangle = Rectangle(1, 1)
print(my_rectangle.__dict__)

my_rectangle.width = 10
my_rectangle.height = 3
print(my_rectangle.__dict__)
print()

try:
    print("height = negative")
    my_rectangle.width = 10
    my_rectangle.height = -3
except Exception as e:
    print(e)
print()


try:
    print("width = negative")
    my_rectangle.width = -10
    my_rectangle.height = 3
except Exception as e:
    print(e)
print()


try:
    print("width = string")
    my_rectangle.width = "hello"
    my_rectangle.height = -3
except Exception as e:
    print(e)
print()


try:
    print("width = string")
    my_rectangle.width = 10
    my_rectangle.height = "yo"
except Exception as e:
    print(e)
print()


try:
    print("width = list")
    my_rectangle.width = (1, 2, 3, 4)
    my_rectangle.height = -3
except Exception as e:
    print(e)
print()


try:
    print("height  = dict")
    my_rectangle.width = 10
    my_rectangle.height = {'name':'uhhu'}
except Exception as e:
    print(e)
print()


try:
    print("width = True")
    my_rectangle.width = True
    my_rectangle.height = 3
except Exception as e:
    print(e)
print()
