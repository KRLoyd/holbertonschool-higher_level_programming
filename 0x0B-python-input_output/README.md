# 0x0B. Python - Input/Output

## Purpose
These files correspond to Holberton School tasks to practice Input/Output with Python files as well as some practice with serialization and deserialization of Python objects.

### Project Notes
#### Environment
These functions have been tested on Ubuntu 14.04.5 LTS.
Tests done in VirtualBox on Ubuntu via Vagrant(1.8.6) using `python3` (version 3.4.3).

#### Style
All files are written in the PEP 8 style.
Information about this style can be found at https://www.python.org/dev/peps/pep-0008/

## Files
To add executable permissions to a file: `chmod u+x file_name`

##### [0-read_file.py](0-read_file.py)
Function that reads a text file (`UTF8`) and prints it to stdout.
* Prototype: `def read_file(filename=""):`
  * @filename: file to read. If none provided, it is set to an empty string.
* Main file: [main-0.py](my_mains/main-0.py)

##### [1-number_of_lines.py](1-number_of_lines.py)
Function that returns the number of lines of a text file.
* Prototype: `def number_of_lines(filename=""):`
  * @filename: file to evaluate. If none provided, it is set to an empty string.
* Main file: [main-1.py](my_mains/main-1.py)

##### [2-read_lines.py](2-read_lines.py)
Function that reads a specified number of lines of a text file (`UTF8`) and prints it to stdout.
* Prototype: `def read_lines(filename="", nb_lines=0):`
  * @filename: file to read. If none provided, it is set to an empty string.
  * @nb_lines: number of lines to read from `filename`
    * If `nb_lines` is not provided, it is set to 0
    * If nb_lines is <= 0 or >= number of lines in the file, the entire file is read
* Main file: [main-2.py](my_mains/main-2.py)

##### [3-write_file.py](3-write_file.py)
Function that writes a string to a text file (`UTF8`) and returns the number of characters written.
* Prototype: `def write_file(filename="", text=""):`
  * @filename: file to write to. If none provided, it is set to an empty string
  * @text: string to be written to `filename`. If none provided, it is set to an empty string.
* Main file: [main-3.py](my_mains/main-3.py)

##### [4-append_write.py](4-append_write.py)
Function that appends a string at the end of a text file (`UTF8`) and returns the number of characters added.
* Prototype: `def append_write(filename="", text=""):`
  * @filename: file to append `text` to. If none is provided, it is set to an empty string. If the `filename` provided doesn't exist, it is created.
  * @text: string to append to `filename`
* Main file: [main-4.py](my_mains/main-4.py)

##### [5-to_json_string.py](5-to_json_string.py)
Function that returns the JSON representation of an object (string).
* Prototype: `def to_json_string(my_obj):`
  * @my_obj: object to get the JSON representation of
* Note: does not manage exceptions if the object isn't serializable
* Main file: [main-5.py](my_mains/main-5.py)

##### [6-from_json_string.py](6-from_json_string.py)
Function that returns an object (Python data structure) represented by a JSON string.
* Prototype: `def from_json_string(my_str):`
  * @my_str: JSON string representing an object
* Main file: [main-6.py](my_mains/main-6.py)

##### [7-save_to_json_file.py](7-save_to_json_file.py)
Function that writes an Object to a text file using JSON representation.
* Prototype: `def save_to_json_file(my_obj, filename):`
  * @my_obj: object to write in JSON representation
  * @filename: file to write the JSON representation to
* Main file: [main-7.py](my_mains/main-7.py)
* Example output files
  * [my-dict.json](my_json/my_dict.json)
  * [my-list.json](my_json/my_list.json)
  * [my-set.json](my_json/my_set.json)

##### [8-load_from_json_file.py](8-load_from_json_file.py)
Function that creates an Object from a JSON file.
* Prototype: `def load_from_json_file(filename):`
  * @filename: JSON file to create an Object
* Main file: [main-8.py](my_mains/main-8.py)
* Example JSON file that won't work: [my_fake.json](my_json/my_fake.json)

##### [9-add_item.py](9-add_item.py)
Script to add all arguments to a Python list and save them to a file.
* Functions used:
  * `save_to_json_file` from [7-save_to_json_file.py](7-save_to_json_file.py)
  * `load_from_json_file` from [8-load_from_json_file.py](8-load_from_json_file.py)
* Example output file: [add_item.json](my_json/add_item.json)
* Usage: 
  ```
  $ ./9-add_item.py
  $ cat add_item.json ; echo ""
  []
  $ ./9-add_item.py Holberton School
  $ cat add_item.json ; echo ""
  ["Holberton", "School"]
  $ ./9-add_item.py 89 Python C
  $ cat add_item.json ; echo ""
  ["Holberton", "School", "89", "Python", "C"]
  $ 
  ```

##### [10-class_to_json.py](10-class_to_json.py)
Function that returns the dictionary description with simple data structure (list, dictionary, string, integer, and boolean) for JSON serialization of an object.
* Prototype: `def class_to_json(obj):`
  * @obj: an instance of a Class where all attributes are serializable
* First Main file: [main-10.py](my_mains/main-10.py)
  * Uses class `MyClass` from [10-my_class.py](my_helper_py/10-my_class.py)
* Second Main file: [main-10_2.py](my_mains/main-10_2.py)
  * Uses class `MyClass` from [10-my_class_2.py](my_helper_py/10-my_class_2.py)

##### [11-student.py](11-student.py)
Defines a class `Student` by:
* Public instance attributes:
  * `first_name`
  * `last_name`
  * `age`
* Instantiation:
  *  `def __init__(self, first_name, last_name, age):`
* Public method `to_json`
  * `def to_json(self):`
  * retrieves a dictionary representation of a `Student` instance
* Main file: [main-11.py](my_mains/main-11.py)

##### [12-student.py](12-student.py)
Defines a class `Student`, based on [11-student.py](11-student.py), by:
* Public method `to_json`
  * `def to_json(self, attrs=None):`
    * @attrs: if provided as a list of strings, only attributes contained in this list are retrieved, otherwise, all attributes are retrieved
  * retrieves a dictionary representation of a `Student` instance
* Main file: [main-12.py](my_mains/main-12.py)

##### [13-student.py](13-student.py)
Defines a class `Student`, based on [11-student.py](11-student.py), by:
* Public method: `reload_from_json`
  * `def reload_from_json(self, json):`
    * @json: a dictionary with key as a public attribute name and value as the value of the public attribute
* Main file: [main-13.py](my_mains/main-13.py)
* Sample JSON file: [student.json](my_json/student.json)

#### [my-mains](my_mains)
Folder holding main files to use my Python functions.


#### [my_json](my_json)
Folder holding JSON files corresponding to tasks 7, 8, 9, and 13.

#### [my_helper_py](my_helper_py)
Python files defining class `MyClass` for task 10.

## Authors
Kristen Loyd        <a href='https://github.com/KRLoyd'>Github</a> ,  <a href='https://www.linkedin.com/in/kristen-loyd-34984a92/'>Linkedin</a>

## License
Public Domain, no copyright protection
