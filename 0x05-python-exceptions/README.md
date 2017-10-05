# 0x05. Python - Exceptions

## Description
Files in this folder correlate to the Holberton School project to practice using and handling exceptions in Python.

### Project Notes
#### Environment
These functions have been tested on Ubuntu 14.04.5 LTS.
Tests done in VirtualBox on Ubuntu via Vagrant(1.8.6) using `python3` (version 3.4.3).

#### Style
All files are written in the PEP 8 style.
Information about this style can be found at https://www.python.org/dev/peps/pep-0008/

## Files
All files must be executable to run. To add executable permissions to any file: `chmod u+x file_name`

##### [0-safe_print_list.py](0-safe_print_list.py)
Function that that prints a certain number of elements of a list.
* Prototype: `def safe_print_list(my_list=[], x=0):`
  * @my_list: list to evaluate. If no list provided, it is set to an empty list.
  * @x: number of elements to print. If no `x` is provided, it is set to 0

##### [1-safe_print_integer.py](1-safe_print_integer.py)
Function that prints an integer with `"{:d}".format()`.
* Prototype: `* ef safe_print_integer(value):`
  * @value: value to be printed, can be any type
  * Returns:
    * if `value` has been printed correctly (is an integer): `True`
    * if `value` has not been printed correctly (it is not an integer): `False`

##### [2-safe_print_list_integers.py](2-safe_print_list_integers.py)
Function that prints the first 'x' integer elements of a list.
* Prototype: `def safe_print_list_integers(my_list=[], x=0):`
  * @my_list: list to print, contains any type of element. If none is provided, it is set to an empty list.
  * @x: number of elements to access. If none is provided, it is set to 0.
  * Return: the real number of integers printed

##### [3-safe_print_division.py](3-safe_print_division.py)
Function that divides 2 integers and prints the result.
* Prototype: `def safe_print_division(a, b):`
  * @a: integer to be divided
  * @b: integer to divide `a` by
  * Returns:
    * Success: value of the division
    * Failure: None

##### [4-list_division.py](4-list_division.py)
Function that divides elements of one list by their corresponding element in a second list.
* Prototype: `def list_division(my_list_1, my_list_2, list_length):`
  * @my_list_1: list to be divided by `my_list_2`  
  * @my_list_2: list to divide `my_list_1`
  * @list_length: length of the new list to be returned
  * Returns: a new list with all divisions
* Notes:
  * If 2 elements can't be divided, the division result is `0`
  * If an element is not an integer or float, `wrong type` is printed
  * If the division can't be done (ie: dividing by `0`), `division by 0` is printed
  * If `my_list_1` or `my_list_2` is too short, `out of range` is printed

##### [5-raise_exception.py](5-raise_exception.py)
Function to raise a type exception.
* Prototype: `def raise_exception():`

##### [6-raise_exception_msg.py](6-raise_exception_msg.py)
Function that raises a name exception with a message.
* Prototype: `def raise_exception_msg(message=""):`
  * @message: meddage to print for the name exception. If none provided, it is set to an empty string


## Authors
Kristen Loyd        <a href='https://github.com/KRLoyd'>Github</a> ,  <a href='https://www.linkedin.com/in/kristen-loyd-34984a92/'>Linkedin</a>

## License
Public Domain, no copyright protection
