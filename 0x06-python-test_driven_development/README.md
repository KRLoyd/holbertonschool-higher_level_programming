# 0x06. Python - Test-driven development

## Purpose
* 

### Project Notes
#### Environment
These functions have been tested on Ubuntu 14.04.5 LTS.
Tests done in VirtualBox on Ubuntu via Vagrant(1.8.6) using `python3` (version 3.4.3).

#### Style
All files are written in the PEP 8 style.
Information about this style can be found at https://www.python.org/dev/peps/pep-0008/

## Files
All files must be executable to run. To add executable permissions to any file: `chmod u+x file_name`

##### [0-add_integer.py](0-add_integer.py)
Function that adds two integers.
* Prototype: `def add_integer(a, b):`
  * @a: first argument to add
  * @b: second argument to add
  * Return: the addition of `a` and `b`
* Notes:
  * If `a` is not an integer or float: raises a `TypeError` exception with message `a must be an integer`
  * If `b` is not an integer or float: raises a `TypeError` exception with message `b must be an integer`
  * If `a` or `b` are floats, they are cast into an integer

##### [2-matrix_divided.py](2-matrix_divided.py)
Function that divides all elements of a matrix.
* Prototype: `def matrix_divided(matrix, div):`
  * @matrix: matrix to be divided
  * @div: number to divide matrix elements by
  * Returns: new matrix with values of `matrix` divided by `div` rounded to two decimal places
* Notes:
  * If `matrix` isn't a list of lists of integers or floats, a `TypeError` exception is raised with the message `matrix must be a matrix (list of lists) of integers/floats`
  * If each row of `matrix` is not the same size, a `TypeError` exception is raised with the message `Each row of the matrix must have the same size`
  * If `div` is not a number, a `TypeError` exception is raised with the message `div must be a number`
  * If `div` == 0, a `ZeroDivisionError` exception is raised with the message `division by zero`

##### [3-say_my_name.py](3-say_my_name.py)
Function that prints "My name is " followed by the passed parameters.
* Prototype: `def say_my_name(first_name, last_name=""):`
  * @first_name: first argument to print
  * @last_name: second argument to print, if none provided, it is set to an empty string
* Notes:
  * If `first_name` is not a string, `TypeError` exception is raised with the message `fisrt_name must be a string`
  * If `last_name` is not a string, `TypeError` exception is raised with the message `last_name must be a string`

##### [4-print_square.py](4-print_square.py)
Function that prints a square with the character `#`.
* Prototype: `def print_square(size):`
  * @size: length of the square
* Notes:
  * If `size` is not an integer, a `TypeError` exception is raised with the message `size must be an integer`
  * If `size` < 0, a `ValueError` exception is raised with the message `size must be >= 0`
  * If `size` is a float and is less than 0, a `TypeError` is raised with the message `sizemust be an integer`

##### [5-text_indentation.py](5-text_indentation.py)
Function that prints a text with 2 new lines after each of those characters: `.`, `?` and `:`.
* Prototype: `def text_indentation(text):`
  * @text: text to print with extra new lines
* Note: if `text` is not a string, a `TypeError` exception is raised with the message `text must be a string`

##### [6-max_integer.py](6-max_integer.py)
Function provided by Holberton School to find the max integer in a list. A Unittest, [6-max_integer_test.py](tests/6-max_integer_test.py) is created to test this function and can be found in the `tests` folder.

#### [my_tests](my_tests)
Files to run my functions.

#### [tests](tests)
Files of tests for my functions.
* To run all tests: `$ python3 -m doctest -v ./tests/*`
* To run a specific test: `$ python3 -m doctest -v ./tests/<filename>`


## Authors
Kristen Loyd        <a href='https://github.com/KRLoyd'>Github</a> ,  <a href='https://www.linkedin.com/in/kristen-loyd-34984a92/'>Linkedin</a>

## License
Public Domain, no copyright protection
