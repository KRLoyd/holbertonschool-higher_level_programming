# 0x02. Python - import & modules

## Purpose
* How to import functions from another file
* How to use imported functions
* How to create a module
* How to use the built-in function `dir()`
* How to prevent code in your script from being executed when imported
* How to use command line arguments with your Python programs

### Project Notes
#### Environment
These functions have been tested on Ubuntu 14.04.5 LTS.
Tests done in VirtualBox on Ubuntu via Vagrant(1.8.6) using `python3` (version 3.4.3).

#### Style
All files are written in the PEP 8 style.
Information about this style can be found at https://www.python.org/dev/peps/pep-0008/

## Files
All files must be executable to run. To add executable permissions to any file: `chmod u+x file_name`

##### `0-add.py`
Program that imports the function `def add(a, b):` from file `add_0.py` and prints the result.
* to run: `./0-add.py`

##### `add_0.py`
Python script with a function to be executed by `0-add.py`.
* Prototype: `def add(a, b):`
	* `a`: first integer
	* `b`: second integer
	* Return: value of a + b

##### `1-calculation.py`
Program that imports functions from file `calculator_1.py`, calculates based on the functions, and prints the result. 
* to run: `./1-calculation.py`

##### `calculator_1.py`
File with descriptions with various functions to be used in other programs.
* `def add(a, b):`
	* `a` : first integer
	* `b` : second integer
	* Return: result of a + b
* `def sub(a, b):`
	* `a` : first integer
	* `b` : second integer
	* Return: result of a - b
* `def mul(a, b):`
	* `a` : first integer
	* `b` : second integer
	* Return: result of a * b
* `def div(a, b):`
	* `a` : first integer
	* `b` : second integer
	* Return: result of a / b

##### `2-args.py`
Program that prints the number of and lists arguments it was given.
* to run: `./2-args.py [arguments...]`

##### `3-infinite_add.py`
Program tht prints the result of the addition of all arguments passed to it.
Note: all arguments must be integers.
* to run: `./3-infinite_add.py`

##### `4-hidden_discovery.py`
Program that prints the names defined by the compiled module `hidden_4.pyc` that do not start with "__".
* to run: `./4-hidden_discovery.py`

##### `hidden_4.pyc`
Compiled module with names defined to be used when running `4-hidden_discovery.py`.

##### `5-variable_load.py`
Program that imports a variable from file `variable_load_5.py` and prints its value.
* to run: `./5-variable_load.py`

##### `variable_load_5.py`
File with variables to be used with file `5_variable_load.py`

##### `100-my_calculator.py`
Program that imports all functions from file `calculator_1.py` and handles basic operation. 
* Usage: `./100-my_calculator.py <a> <operator> <b>`
	* `a`: first integer
	* operator: can be one of the following: +, -, *, /
	* 'b': second integer

##### `101-easy_print.py`
Program that prints `#pythoniscool` without `print` or `import sys` in this source code.
* Usage: `./101-easy_print.py`

##### `import_for_101.py`
Python script to print `#pythoniscool`. To be used by `101-easy_print.py`

##### `103-fast_alphabet.py`
Program that prints the alphabet in uppercase.
* to run: `./103-fast_alphabet.py`
  
## Authors
Kristen Loyd        <a href='https://github.com/KRLoyd'>Github</a> ,  <a href='https://www.linkedin.com/in/kristen-loyd-34984a92/'>Linkedin</a>

## License
Public Domain, no copyright protection
