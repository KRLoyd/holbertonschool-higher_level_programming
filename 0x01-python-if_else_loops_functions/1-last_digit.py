#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    abs_number = -number
else:
    abs_number = number
last_digit = abs_number % 10
print(number, last_digit)
