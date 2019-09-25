# 0x07. Python - Classes and Objects

## Purpose
The files in this folder correspond to Holberton School tasks to become familiar with Object Oriented Programming with Python. Tasks include making objects, defining classes, inheriting from classes, and setting and getting attributes (public and private).

### Project Notes
#### Environment
These functions have been tested on Ubuntu 14.04.5 LTS.
Tests done in VirtualBox on Ubuntu via Vagrant(1.8.6) using `python3` (version 3.4.3).

#### Style
All files are written in the PEP 8 style.
Information about this style can be found at https://www.python.org/dev/peps/pep-0008/

## Files
All files must be executable to run. To add executable permissions to any file: `chmod u+x file_name`

##### [0-square.py](0-square.py)
Defines an empty class `Square`.
* Corresponding main file: [test-0.py](tests/test-0.py)

##### [1-square.py](1-square.py)
Based on [0-square.py](0-square.py), defines a class `Square`.
* Notes
  * Private instance attribute: `size`
  * Instantiation of `size` without type and/or value verification
  * Corresponding main file: [test-1.py](my_tests/test-1.py)

##### [2-square.py](2-square.py)
Based on [1-square.py](1-square.py), defines a class `Square`.
* Notes
  * Private instance attribute `size`
  * Instantiation with optional `size`
    * If no `size` is passed, `size=0`
    * If `size` is not an integer, a `TypeError` exception is raised with the message `size must be an integer`
    * If `size` is negative, a `ValueError` exception is raised with the message `size must be >= 0`
  * Corresponding main file: [test-2.py](my_tests/test-2.py)

##### [3-square.py](3-square.py)
Based on [2-square.py](2-square.py), defines a class `Square`.
* Notes
  * Private instance attribute `size`
  * Instantiation with optional `size`
    * If no `size` is passed, `size=0`
    * If `size` is not an integer, a `TypeError` exception is raised with the message `size must be an integer`
    * If `size` is negative, a `ValueError` exception is raised with the message `size must be >= 0`
  * Public instance method `area`
    * `def area(self):`
    * Returns the current square area
  * Corresponding main file: [test-3.py](my_tests/test-3.py)

##### [4-square.py](4-square.py)
Based on [3-square.py](3-square.py), defines a class `Square`.
* Notes
  * Private instance attribute `size`
    * property `def size(self):` to retrieve `size`
    * property setter `def size(self, value):` to set `size`
      * If `size` is not an integer, a `TypeError` exception is raised with the message `size must be an integer`
      * If `size` is negative, a `ValueError` exception is raised with the message `size must be >= 0`
  * Instantiation with optional `size`
    * `def __init__(self, size=0)`
  * Public instance method `area`
    * `def area(self):`
    * Returns the current square area
  * Corresponding main file: [test-4.py](my_tests/test-4.py)

##### [5-square.py](5-square.py)
Based on [4-square.py](4-square.py), defines a class `Square`.
* Notes
  * Private instance attribute `size`
    * property `def size(self):` to retrieve `size`
    * property setter `def size(self, value):` to set `size`
      * If `size` is not an integer, a `TypeError` exception is raised with the message `size must be an integer`
      * If `size` is negative, a `ValueError` exception is raised with the message `size must be >= 0`
  * Instantiation with optional `size`
    * `def __init__(self, size=0)`
  * Public instance method `area`
    * `def area(self):`
    * Returns the current square area
  * Public instance method `my_print`
    * `def my_print(self):`
    * Prints in stdout the square using character `#`
      * If `size` is 0, an empty line is printed
  * Corresponding main file: [test-5.py](my_tests/test-5.py)

##### [6-square.py](6-square.py)
Based on [5-square.py](5-square.py), defines a class `Square`.
* Notes
  * Private instance attribute `size`
    * property `def size(self):` to retrieve `size`
    * property setter `def size(self, value):` to set `size`
      * If `size` is not an integer, a `TypeError` exception is raised with the message `size must be an integer`
      * If `size` is negative, a `ValueError` exception is raised with the message `size must be >= 0`
  * Private instance attribute `position`
    * property `def position(self):` to retrieve `position`
    * property setter `def position(self, value):` to set `position`
      * if `position` is not a tuple of 2 positive integers, a `TypeError` exception is raised with the message `position must be a tuple of 2 positive integers`
  * Instantiation with optional `size` and optional `position`
    * `def __init__(self, size=0, position=(0, 0)):`
  * Public instance method `area`
    * `def area(self):`
    * Returns the current square area
  * Public instance method `my_print`
    * `def my_print(self):`
    * Prints in stdout the square using character `#`
      * If `size` is 0, an empty line is printed
      * `position` is utilized with spaces
  * Corresponding main file: [test-6.py](my_tests/test-6.py)

#### [my_tests](my_tests)
Folder to hold my main files to test my classes.

#### [tests](tests)
Folder with my tests for task # 4.


## Authors
Kristen Loyd        <a href='https://github.com/KRLoyd'>Github</a> ,  <a href='https://www.linkedin.com/in/kristen-loyd-34984a92/'>Linkedin</a>

## License
Public Domain, no copyright protection
