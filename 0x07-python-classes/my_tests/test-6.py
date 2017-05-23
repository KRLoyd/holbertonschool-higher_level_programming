#!/usr/bin/python3
Square = __import__('6-square').Square

print("Square(3)")
my_square_1 = Square(3)
my_square_1.my_print()

print("--")

print("Square(3, (1, 1))")
my_square_2 = Square(3, (1, 1))
my_square_2.my_print()

print("--")

print("Square(3, (3, 0))")
my_square_3 = Square(3, (3, 0))
my_square_3.my_print()

print("--")

print("Square(3, (3, 0, 8))")
try:
    my_square_3 = Square(3)
    my_square_3.position = (3, 0, 8)
    my_square_3.my_print()
except Exception as e:
    print(e)

print("--")
print("Square(3, (5, 6))")
my_square_3 = Square(3, (5, 6))
my_square_3.my_print()

print("--")
print("Square(3, (1, 0))")
my_square_3 = Square(3, (1, 0))
my_square_3.my_print()

print("--")
print("--")
try:
    print("Square(3, (1, \"3\"))")
    my_square_3 = Square(3, (1, "3"))
    my_square_3.my_print()
except Exception as e:
    print(e)

print("--")
try:
    print("Square(3, \"Position\")")
    my_square_3 = Square(3, "Position")
    my_square_3.my_print()
except Exception as e:
    print(e)

print("--")
try:
    print("Square(3, (1,))")
    my_square_3 = Square(3, (1,))
    my_square_3.my_print()
except Exception as e:
    print(e)

print("--")
try:
    print("Square(3, (1, -3))")
    my_square_3 = Square(3, (1, -3))
    my_square_3.my_print()
except Exception as e:
    print(e)
