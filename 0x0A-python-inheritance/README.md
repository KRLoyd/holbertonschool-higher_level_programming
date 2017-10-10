# 0x0A. Python - Inheritance

## Purpose
Files in this folder correlate with the Holberton School project focusing on inheritance in Python.

### Project Notes
#### Environment
These functions have been tested on Ubuntu 14.04.5 LTS.
Tests done in VirtualBox on Ubuntu via Vagrant(1.8.6) using `python3` (version 3.4.3).

#### Style
All files are written in the PEP 8 style.
Information about this style can be found at https://www.python.org/dev/peps/pep-0008/

## Files
To add executable permissions to a file: `chmod u+x file_name`

##### [0-lookup.py](0-lookup.py)
Function that returns the list of available attributes and methods of an object.
* Prototype: `def lookup(obj):`
* Main file: [main-0.py](my_mains/main-0.py)

##### [1-my_list.py](1-my_list.py)
Defines a class `MyList` that inherits from `list`.
* Notes
  * Publid instance method: `print_sorted`
    * `def print_sorted(self):`
    * Assumes all elements of the list are of type `int`
  * Main file: [main-1.py](my_mains/main-1.py)
  * Test file: [1-my_list.txt](tests/1-my_list.txt)

##### [2-is_same_class.py](2-is_same_class.py)
Function that checks if an object is exactly an instance of a specified class.
* Notes
  * Prototype: `def is_same_class(obj, a_class):`
    * @obj: object to check
    * @a_class: class to check `obj` against
    * Returns
      * `obj` is an instance of `a_class`: Returns `True`
      * `obj` is not an instance of `a_class`: Returns `False`
  * Main file: [main-2.py](my_mains/main-2.py)

##### [3-is_kind_of_class.py](3-is_kind_of_class.py)
Function to check if an object is and instance of, or an instance of a class that inherited from, a specified class.
* Notes
  * Prototype: `def is_kind_of_class(obj, a_class):`
    * @obj : object to check
    * @a_class: class to check `obj` against
    * Returns
      * `obj` is an instance of, of is an instance that inherits from, `a_class`: Returns `True`
      * `obj` is not an instance of, nor does it inherit from, `a_class`: Returns `False`
  * Main file: [main-3.py](my_mains/main-3.py)

##### [4-inherits_from.py](4-inherits_from.py)
Function that checks if an object is an instance of a class that inherited from a specified class.
* Notes
  * Prototype: `def inherits_from(obj, a_class):`
    * @obj : object to check
    * @a_class: class to check `obj` inheritance
    * Returns
      * `obj` is an instance of a class that inherited `a_class`: Returns `True`
      * `obj` is not an instance of a class that inherited from`a_class`: Returns `False`
  * Main file: [main-4.py](my_mains/main-4.py)

##### [5-base_geometry.py](5-base_geometry.py)
Defines an empty class `BaseGeometry`.
* Main file: [main-5.py](my_mains/main-5.py)

##### [6-base_geometry.py](6-base_geometry.py)
Defines a class `BaseGeometry`, based on [5-base_geometry.py](5-base_geometry.py).
* Notes/Additions
  * Public instance method: `area`
    * `def area(self):`
    * Raises an `Exception` with the message `area() is not implemented`
  * Main file: [main-6.py](my_mains/main-6.py)

##### [7-base_geometry.py](7-base_geometry.py)
Defines a class `BaseGeometry`, based on [6-base_geometry.py](6-base_geometry.py).
* Notes/Additions
  * Public instance method: `integer_validator` to validate `value`
    * `def integer_validator(self, name, value):`
      * assumes `name` is always a string
      * if `value` isn't an integer, a `TypeError` exception is raised with the message `<name> must be an integer`
      * if `value` is less than or equal to 0, a `ValueError` exception is raised with the message `<name> must be greater than 0`
  * Main file: [main-6.py](my_mains/main-6.py)
  * Test file: [7-base_geometry.txt](tests/7-base_geometry.txt)

##### [8-rectangle.py](8-rectangle.py)
Defines a class `Rectangle` that inherits from `BaseGeometry` ([7-base_geometry.py](7-base_geometry.py0).
* Notes
  * Instantiation with `width` and `height`
    * `def __init__(self, width, height):`
    * `width` and `height` are private
      * They must be positive integers, validated by `integer_validator`
  * Main file: [main-8.py](my_mains/main-8.py)
  * Test file: [8-rectangle.txt](tests/8-rectangle.txt)

##### [9-rectangle.py](9-rectangle.py)
Defines a class `Rectangle` that inherits from `BaseGeometry` ([7-base_geometry.py](7-base_geometry.py0), based on [8-rectangle.py](8-rectanlge.py).
* Notes
  * Instantiation with `width` and `height`
    * `def __init__(self, width, height):`
    * `width` and `height` are private
      * They must be positive integers, validated by `integer_validator`
  * `area()` method is implemented
  * `print()` prints, and `str()` returns, the description of the rectangle
     * format: `[Rectangle] <width>/<height>`
  * Main file: [main-9.py](my_mains/main-9.py)
  * Test file: [9-rectangle.txt](tests/9-rectangle.txt)

##### [10-square.py](10-square.py)
Defines a class `Square` that inherits from `Rectangle` ([9-rectangle.py](9-rectangle.py).
* Notes
  * Instantiation with `width` and `height`
    * `def __init__(self, width, height):`
    * `width` and `height` are private
      * They must be positive integers, validated by `integer_validator`
  * `area()` method is implemented
  * Main file: [main-10.py](my_mains/main-10.py)

##### [11-square.py](11-square.py)
Defines a class `Square` that inherits from `Rectangle` ([9-rectangle.py](9-rectangle.py)), based on [10-square.py](10-square.py).
* Notes/Additions
  * `print()` prints, and `str()` returns, the square description
    * format: `[Square] <width>/<height>`
  * Main file: [main-11.py](my_mains/main-11.py)

#### [tests](tests)
Folder to hold Python tests for some tasks. 
* To execute all tests, use this command: `python3 -m doctest ./tests/*`

#### [my_mains](my_mains)
Folder to hold the main files to utilize functions/classes created in the above files. 


  
## Authors
Kristen Loyd        <a href='https://github.com/KRLoyd'>Github</a> ,  <a href='https://www.linkedin.com/in/kristen-loyd-34984a92/'>Linkedin</a>

## License
Public Domain, no copyright protection
