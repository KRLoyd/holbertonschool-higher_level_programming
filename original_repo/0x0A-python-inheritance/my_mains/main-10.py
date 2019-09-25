#!/usr/bin/python3
Square = __import__('10-square').Square

s = Square(13)

print(s)
print(s.area())
print()

try:
    s = Square(-893)
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
    s = Square("hello")
    print(s)
    print(s.area())
    print()
except Exception as e:
    print(e)
