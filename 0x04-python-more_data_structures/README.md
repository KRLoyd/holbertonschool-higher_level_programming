# 0x04. Python - More Data Structures: Set, Dictonary

## Description
Files in this folder correlate to tasks in a Holberton Project to become more familiar with data structures in Python, specifically sets and dictionaries.

### Project Notes
#### Environment
These functions have been tested on Ubuntu 14.04.5 LTS.
Tests done in VirtualBox on Ubuntu via Vagrant(1.8.6) using `python3` (version 3.4.3).

#### Style
All files are written in the PEP 8 style.
Information about this style can be found at https://www.python.org/dev/peps/pep-0008/

## Files
All files must be executable to run. To add executable permissions to any file: `chmod u+x file_name`

##### [0-square_matrix_simple.py](0-square_matrix_simple.py)
Function that computes the square value of all integers in a matrix.
* Prototype: `def square_matrix_simple(matrix=[]):`
  * @matrix: a 2 dimensional array
  * Returns: a new matrix the same size as `matrix` where each value is the square of the value of the input.
* Note: The original matrix is not modified

##### [1-search_replace.py](1-search_replace.py)
Function that replaces all occurences of an element by another in a new list.
* Prototype: `def search_replace(my_list, search, replace):`
  * @list: initial list
  * @search: element to replace in the list
  * @replace: new element to replace `search` elements
  * Returns: new list with the `search` elements replaced with `replace` element

##### [2-uniq_add.py](2-uniq_add.py)
Function that makes the addition of all unique integers in a list.
* Prototype: `def uniq_add(my_list=[]):`
  * @my_list: list to evaluate
  * Returns: the sum of all unique integers in `my_list`

##### [3-common_elements.py](3-common_elements.py)
Funtion that returns a set of common elements in two sets.
* Prototype: `def common_elements(set_1, set_2):`
  * @set_1: first set to compare
  * @set_2: second set to compare
  * Returns: Set of elements common to both sets

##### [4-only_diff_elements.py](4-only_diff_elements.py)
Function that returns a set of all elements present in only one set.
* Prototype: `def only_diff_elements(set_1, set_2):`
  * @set_1: first set to compare
  * @set_2: second set to compare
  * Returns: list of elements only found in either `set_1` and `set_2`

##### [5-number_keys.py](5-number_keys.py)
Function that returns the number of keys in a dictionary.
* Prototype: `def number_keys(my_dict):`
  * @my_dict: dictionary to evaluate
  * Returns: Number of keys in the dictionary formatted as `Number of keys: <number of keys>`

##### [6-print_sorted_dictionary.py](6-print_sorted_dictionary.py)
Function that prints a dictionary by ordered keys.
* Prototype: `def print_sorted_dictionary(my_dict):`
  * @my_dict: dictionary to be printed
* Notes: 
  * Function assumes all keys are strings
  * Function sorts only the first level (doesn't sort keys of a dictionary inside the main dictionary)
  * Each item is on its own line

##### [7-update_dictionary.py](7-update_dictionary.py)
Function that replaces or adds a key/value pair in a dictionary.
* Prototype: `def update_dictionary(my_dict, key, value):`
  * @my_dict: dictionary to update
  * @key: key to find/add
  * @value: value associated with `key`
  * Returns: updated dictionary
* Note: function assumes that keys are strings

##### [8-simple_delete.py](8-simple_delete.py)
Function that deletes a key in a dictionary.
* Prototype: `def simple_delete(my_dict, key=""):`
  * @my_dict: dictionary to be updated
  * @key: key to delete
  * Returns:
    * If key exists in the dictionary: updated version of `my_dict`
    * If key does not exist: original `my_dict`
* Note: function assumes that keys are strings

##### [9-multiply_by_2.py](9-multiply_by_2.py)
Function that multiplies all values of a dictionary by 2.
* Prototype: `def multiply_by_2(my_dict):`
  * @my_dict: dictionary to copy and manipulate
  * Returns: a new dictionary with values that are 2 times the values of `my_dict`
* Note: function assumes all values of `my_dict` are integers

##### [10-best_score.py](10-best_score.py)
Function that returns a key with the biggest integer value.
* Prototype: `def best_score(my_dict):`
  * @my_dict: dictionary to evaluate
  * Returns:
    * If no scores are found: `None`
    * If scores are found: The key with the biggest integer value
* Note: Function assumes all values are unique integers

##### [11-mutiply_list_map.py](11-mutiply_list_map.py)
Function that returns a list with all values multiplied by a number without using any loops.
* Prototype: `def mutiply_list_map(my_list=[], number=0):`
  * @my_list: list to base new list on. If no list is passed, it is set to an empty list
  * @number: number to multiply all list values by. If no number is supplied, it is set to 0
  * Return: new list with values being the `my_list` value multiplied by `number`


## Authors
Kristen Loyd        <a href='https://github.com/KRLoyd'>Github</a> ,  <a href='https://www.linkedin.com/in/kristen-loyd-34984a92/'>Linkedin</a>

## License
Public Domain, no copyright protection
