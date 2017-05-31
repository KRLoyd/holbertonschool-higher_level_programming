#!/usr/bin/python3
Square = __import__('11-square').Square

s = Square(13)

print(s)
print(s.area())
print()

try:
    s = Square({2, 3})

    print(s)
    print(s.area())
    print()
except Exception as e:
    print(e)

try:
    s = Square(0)

    print(s)
    print(s.area())
    print()
except Exception as e:
    print(e)

try:
    s = Square(-8)

    print(s)
    print(s.area())
    print()
except Exception as e:
    print(e)

try:
    s = Square([3, 4, 5])

    print(s)
    print(s.area())
    print()
except Exception as e:
    print(e)
