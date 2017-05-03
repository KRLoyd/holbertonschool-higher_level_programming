# 0x01. Python - if/else, loops, functions

## Purpose
* Why Python programming is awesome
* Why indentation is so important in Python
* How to use the `if`, `if ... else` statements
* How to use comments
* How to affect values to variables
* How to use the `while` and `for` loops
* How is the Python's `for` different from C's
* How to use the `break` and `continue` statements
* How to use `else` clauses on loops
* What does the `pass` statement do, and when to use it
* How to use `range`
* What is a function and how do you use functions
* What does a function return if it does not use a `return` statement
* Scope of variables
* What's a traceback
* What are the arithmetic operators and how to use them

### Project Notes
#### Environment
These functions have been tested on Ubuntu 14.04.5 LTS.
Tests done in VirtualBox on Ubuntu via Vagrant(1.8.6) using `python3` (version 3.4.3).

#### Style
All files are written in the PEP 8 style.
Information about this style can be found at https://www.python.org/dev/peps/pep-0008/

## Files

##### `0-positive_or_negative.py `
Python script that prints whether the number stored in varibale `number` is positive or negative. 
* to run: `0-positive_or_negative.py`

##### `1-last_digit.py`
Python script to print the last digit of the number in variable `number`
* to run: `./1-last_digit.py`

##### `2-print_alphabet.py`
Python script to print the alphabet.
* to run: `./2-print_alphabet`

##### `3-print_alphabt.py`
Python script to print the alphabet excludin `e` and `q`

##### `4-print_hexa.py`
Python program to print all numbers from `0` to `98` in decimal and hexadecimal.
* to run: `./4-print_hexa.py`

##### `5-print_comb2.py`
Python program that prints numbers from `0` to `99`
* to run: `./5-print_comb2.py`

##### `6-print_comb3.py`
Pyton program that prints all possible combinations of two digits.
* to run: `./6-print_comb3.py`

##### `7-islower.py`
Python function that checks for lowercase characters.
* Prototype: `def islower(c):`
	* `c`: character to check
* `7-main.py`: main file to utilize this function
	* to use, please create the file with the content specified below and make executable.
	* File content:
	```
	#!/usr/bin/env python3
	islower = __import__('7-islower').islower

	print("a is {}".format("lower" if islower("a") else "upper"))
	print("H is {}".format("lower" if islower("H") else "upper"))
	print("A is {}".format("lower" if islower("A") else "upper"))
	print("3 is {}".format("lower" if islower("3") else "upper"))
	print("g is {}".format("lower" if islower("g") else "upper"))
	```
	* to run: `./7-main.py`

##### `8-uppercase.py`
Python function that prints a string in uppercase.
* Prototype: `def uppercase(str):`
	* `str`: string to print in uppercase
* `8-main.py`: main file to utilize this function
	* to use, please create the file with the content specified below and make executable.
	* File content:
	```
	#!/usr/bin/env python3
	uppercase = __import__('8-uppercase').uppercase

	uppercase("holberton")
	uppercase("Holberton School 98 Battery street")
	```
	* to run: `./8-main.py`

##### `9-print_last_digit.py`
Python function that prints the last digit of a number.
* Prototype: `def print_last_digit(number):`
	* `number`: number to evaluate
* `9-main.py`: main file to utilize this funtion
	* to use, please create the file with the content specified below and make executable.
	* File content:
	```
	#!/usr/bin/env python3
	print_last_digit = __import__('9-print_last_digit').print_last_digit

	print_last_digit(98)
	print_last_digit(0)
	r = print_last_digit(-1024)
	print(r)
	```
	* to run: `./9-main.py`

##### `10-add.py`
Python function that adds two integers.
* Prototype: `def add(a, b):`
	* `a`: first integer to add
	* `b`: sencond integer to add
	* Returns: result of addidion
* `10-main.py`: main file to utilize this function
	* to use, please create the file with the content specified below and make executable.
	* File content:
	```
	#!/usr/bin/env python3
	add = __import__('10-add').add

	print(add(1, 2))
	print(add(98, 0))
	print(add(100, -2))
	```
	* to run: `./10-add.py`

##### `11-pow.py`
Python function that computes `a` to the power of `b`.
* Prototype: `def pow(a, b):`
	* `a`: number to be computed
	*  `b`: power to be computed
	* Return: value of computation
* `11-main.py`: main file to utilize this function
	* to use, please create the file with the content specified below and make executable.
	* File content:
	```
	#!/usr/bin/env python3
	pow = __import__('11-pow').pow

	print(pow(2, 2))
	print(pow(98, 2))
	print(pow(98, 0))
	print(pow(100, -2))
	print(pow(-4, 5))
	```
	* to run: `./10-add.py`

##### `12-fizzbuzz.py`
Python function that prints the numbers from 1 to 100. 
If the number is a multiple of 3,`Fizz` is printed instead of the number.
If the number is a multiple of 5, `Buzz` is printed instead of the number.
If the number is a multiple of 3 and 5, `FizzBuzz` is printed instead of the number.

* Prototype: `def fizzbuzz():`
* `12-main.py`: main file to utilize this function
	* to use, please create the file with the content specified below and make executable.
	* File content:
	```
	#!/usr/bin/env python3
	fizzbuzz = __import__('12-fizzbuzz').fizzbuzz

	fizzbuzz()
	print("")
	```
	* to run: `./12-main.py`

##### `100-print_tebahpla.py`
Python program that prints the alphabet in reverse with alternating lowercase and uppercase characters.
* to run: `./100-print_tebahpla.py`

##### `101-remove_char_at.py`
Python function that creates a copy of the string; the character at position `n` is removed.
* Prototype: `def remove_char_at(str, n):`
	* `str`: string to copy
	* `n`: character position to remove from the string
* `101-main.py`: main file to utilize this function
	* to use, please create the file with the content specified below and make executable
	* File content:
	```
	#!/usr/bin/env python3
	remove_char_at = __import__('101-remove_char_at').remove_char_at

	print(remove_char_at("Holberton School", 3))
	print(remove_char_at("Chicago", 2))
	print(remove_char_at("C is fun!", 0))
	print(remove_char_at("School", 10))
	print(remove_char_at("Python", -2))
	```
	* to run: `./101-main.py`

## Authors
Kristen Loyd        <a href='https://github.com/KRLoyd'>Github</a> ,  <a href='https://www.linkedin.com/in/kristen-loyd-34984a92/>Linkedin</a>

## License
Public Domain, no copyright protection
