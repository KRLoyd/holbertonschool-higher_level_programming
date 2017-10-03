# 0x03. Python - Data Structures: Lists, Tuples

## Description
Files in this directory correlate with Holberton School tasks to work with Python lists and tuples.

### Project Notes
#### Environment
These functions have been tested on Ubuntu 14.04.5 LTS.
Tests done in VirtualBox on Ubuntu via Vagrant(1.8.6) using `python3` (version 3.4.3).

#### Style
All files are written in the PEP 8 style.
Information about this style can be found at https://www.python.org/dev/peps/pep-0008/

## Files
All files must be executable to run. To add executable permissions to any file: `chmod u+x file_name`

##### [0-print_list_integer.py](0-print_list_integer.py)
Function that prints all integers of a list.
* Prototype: `def print_list_integer(my_list=[]):`
  * @my_list: list of integers to print. If no list is passed, the default is an empty list.

##### [1-element_at.py](1-element_at.py)
Function that retrieves an element from a list.
* Prototype: `def element_at(my_list, idx);`
  * @my_list: list of elements
  * @idx: index of the element to retreive
  * Returns:
    * Success: element at `idx` of `my_list`
    * Failure: if `idx` is negative or out of range, `None` is returned

##### [2-replace_in_list.py](2-replace_in_list.py)
Function that replaces an element of a list at a specific position.
* Prototype: `def replace_in_list(my_list, idx, element):`
  * @my_list: list to update
  * @idx: index of the element to update
  * @element: new element to replace old element
  * Returns:
    * Success: new list
    * Failure: if `idx` is negative or out of range, the original list is returned

##### [3-print_reversed_list_integer.py](3-print_reversed_list_integer.py)
Function that prints all integers of a list, in reverse order.
* Prototype: `def print_reversed_list_integer(my_list=[]):`
  * @my_list: list to print, if none passed it defaults to an empty list
* Note: prints one integer per line

##### [4-new_in_list.py](4-new_in_list.py)
Function that replaces an element in a list at a specific position without modifying the original list.
* Prototype: `def new_in_list(my_list, idx, element):`
  * @my_list: list to copy and modify
  * @idx: index of the eement to replace
  * @element: new element to replace element at `idx`
  * Returns:
    * Success: the new list
    * Failure: if `idx` is negative or out of range, a copy of the original list is returned

##### [5-no_c.py](5-no_c.py)
Function that removes all characters `c` and `C` from a string.
* Prototype: `def no_c(my_string):`
  * @my_string: string to modify
  * Return: the new string

##### [6-print_matrix_integer.py](6-print_matrix_integer.py)
Function that prints a matrix of integers.
* Prototype: `def print_matrix_integer(matrix=[[]]):`
  * @matrix: matrix to print, if none provided, and empty matrix is used

##### [7-add_tuple.py](7-add_tuple.py)
Function to add 2 tuples.
* Prototype: `def add_tuple(typle_a=(), tuple_b=()):`
  * @tuple_a : first tuple, if none passed, an empty tuple is used
  * @tuple_b : first tuple, if none passed, an empty tuple is used
  * Returns: a new tuple of the result
* Notes:
  * If a tuple is smaller than 2: value `0` is used for each missing integer
  * If a tuple is bigger than 2: only the first 2 integers are used

##### [8-multiple_returns.py](8-multiple_returns.py)
Function to return a tuple with the length of a string and it's first character.
* Prototype: `def myltiple_returns(sentence):`
  * @sentence: string to evaluate
  * Returns: tuple where first value is length of `sentence` and second value is the charst character in `sentence`
* Note: If `sentence` is an empty string, the second value of the tuple is `None`

##### [9-max_integer.py](9-max_integer.py)
Function that finds the biggest integer of a list.
* Prototype: `def max_integer(my_list=[]):`
  * @my_list: list to evaluate, if none passed, and empty list is used
  * Returns: The biggest integer of the list
    * If the list is empty, `None` is returned

##### [10-divisible_by_2.py](10-divisible_by_2.py)
Function to find all the multipes of 2 in a list.
* Prototype: `def divisiable_by_2(my_list=[]):`
  * @my_list: list to evaluate, if none passed, and empty list is used
  * Returns: new list with values of `True` and `False`
    * `True`: number at this index is divisible by 2
    * `False`: number at this index is not divisible by 2

##### [11-delete_at.py](11-delete_at.py)
Function that deletes the item at a specific position in a list.
* Prototype: `def delete_at(my_list=[], idx=0):`
  * @my_list: list to evaluate, if none passed, and empty list is used
  * @idx: index of item to delete, if none passed, and `0` is used
  * Returns: updated list
    * if `idx` is negative or out of range, nothing is changed

##### [12-switch.py](12-switch.py)
Completed source code in order to switch the value of `a` and `b`. Source code can be found [here](https://github.com/holbertonschool/0x03.py/blob/master/12-switch_py).

  
#### [my_tests](my_tests)
Folder that holds my test files for the above files.
  
## Authors
Kristen Loyd        <a href='https://github.com/KRLoyd'>Github</a> ,  <a href='https://www.linkedin.com/in/kristen-loyd-34984a92/'>Linkedin</a>

## License
Public Domain, no copyright protection
