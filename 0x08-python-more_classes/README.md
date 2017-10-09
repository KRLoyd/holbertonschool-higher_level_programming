# 0x08. Python - More Classes and Objects

## Purpose
The tasks in this folder correspond with a Holberton School project to work with classes and oobjects in Python, specifiacally working with inheritance. 

### Project Notes
#### Environment
These functions have been tested on Ubuntu 14.04.5 LTS.
Tests done in VirtualBox on Ubuntu via Vagrant(1.8.6) using `python3` (version 3.4.3).

#### Style
All files are written in the PEP 8 style.
Information about this style can be found at https://www.python.org/dev/peps/pep-0008/

## Files
All files must be executable to run. To add executable permissions to any file: `chmod u+x file_name`

##### [0-rectangle.py](0-rectangle.py)
Defines an empty class `Rectangle`.
* Corresponding main file: [main-0.py](mains/main-0.py)

##### [1-rectangle.py](1-rectangle.py)
Defines a class `Rectangle`, based on [0-rectangle.py](0-rectangle.py).
* Notes/Additions
  * Private instance attribute: `width`
    * property `def width(self):` to retrieve `width`
    * property setter `def width(self, value):` to set `width`
      * if `width` is not an integer, a `TypeError` exception is raised with the message `width must be an integer`
      * if `width` is negative, a `ValueError` exception is raised with the message `width must be >= 0`
  * Private instance attribute `height`
    * property `def height(self):` to retrieve `height`
    * property setter `def heihgt(self, value):` to set `height`
      * if `height` is not an integer, a `TypeError` exception is raised with the message `height must be an integer`
      * if `height` is negative, a `ValueError` exception is raised with the message `height must be >= 0`
  * Instantiation with optional `width` and `height`
    * `def __init__(self, width=0, height=0):`
  * Corresponding main file: [main-1.py](mains/main-1.py)

##### [2-rectangle.py](2-rectangle.py)
Defines a class `Rectangle`, based on [1-rectangle.py](1-rectangle.py).
* Notes/Additions
  * Public instance method: `perimeter`
    * `def perimeter(self):`
    * Returns the rectangle perimeter
      * if `width` or `height` are `0`, perimeter is `0`
  * Corresponding main file: [main-2.py](mains/main-2.py)

##### [3-rectangle.py](3-rectangle.py)
Defines a class `Rectangle`, based on [2-rectangle.py](2-rectangle.py).
* Notes/Additions
  * methods `print()` and `str()` print the rectangle with character `#`
    * if `width` or `height` are `0`, an empty string is returned
  * Corresponding main file: [main-3.py](mains/main-3.py)

##### [4-rectangle.py](4-rectangle.py)
Defines a class `Rectangle`, based on [3-rectangle.py](3-rectangle.py).
* Notes/additions
  * `repr()` returns a string representation of the rectangle
    * To be able to recreate a new instance by using `eval()`
  * Corresponding main file: [main-4.py](mains/main-4.py)

##### [5-rectangle.py](5-rectangle.py)
Defines a class `Rectangle`, based on [4-rectangle.py](4-rectangle.py).
* Notes/Additions
  * `__del__`: when an instance of `Rectangle` is deleted, the message "Bye rectangle...: is printed
  * Corresponding main file: [main-5.py](mains/main-5.py)

##### [6-rectangle.py](6-rectangle.py)
Defines a class `Rectangle`, based on [5-rectangle.py](5-rectangle.py).
* Notes/Additions
  * Public class attribute `number_of_instances`
    * initialized to `0`
    * Incremented during each new instance instantiation
    * Decremented during each instance delition
  * Corresponding main file: [main-6.py](mains/main-6.py)

##### [7-rectangle.py](7-rectangle.py)
Defines a class `Rectangle`, based on [6-rectangle.py](6-rectangle.py).
* Notes/Additions
  * Public class attribute `print_symbol`
    * Initialized to `#`
    * Used as the symbol for string representation
    * Can be any type
  * Corresponding main file: [main-7.py](mains/main-7.py)
  
##### [8-rectangle.py](8-rectangle.py)
Defines a class `Rectangle`, based on [7-rectangle.py](7-rectangle.py).
* Notes/Additions
  * Static method `def bigger_or_equal(rect_1, rect_2):`
    * Returns the biggest rectangle based on area
      * If both rectangles have the same area value, `rect_1` is returned
    * If `rect_1` is not an instance of `Rectangle`, a `TypeError` exception is raised with the message `rect_1 must be an instance of Rectangle`
    * If `rect_2` is not an instance of `Rectangle`, a `TypeError` exception is raised with the message `rect_2 must be an instance of Rectangle`
  * Corresponding main file: [main-8.py](mains/main-8.py)

##### [9-rectangle.py](9-rectangle.py)
Defines a class `Rectangle`, based on [8-rectangle.py](8-rectangle.py).
* Notes/Additions
  * Class method `def square(cls, size=0):`
    * Returns a new Rectangle instance with `width` == `height` == `size`
  * Corresponding main file: [main-9.py](mains/main-9.py)

### [mains](mains)
Folder to hold the main files to use the classes defined in the above files.


## Authors
Kristen Loyd        <a href='https://github.com/KRLoyd'>Github</a> ,  <a href='https://www.linkedin.com/in/kristen-loyd-34984a92/'>Linkedin</a>

## License
Public Domain, no copyright protection
