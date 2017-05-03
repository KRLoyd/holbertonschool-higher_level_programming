# 0x00. Python - Hello, World

## Purpose
To be able to explain the following:
* Why Python programming is awesome
* Who created Python
* Who is Guido van Rossum
* Where does the name 'Python' come from
* What is the Zen of Python
* How to use the Python interpreter
* How to print text and variables using `print`
* How to use strings
* What are indexing and slicing in Python
* What is the official Holberton Python coding style and how to check code with `PEP 8`

### Project Notes
#### Environment
These functions have been tested on Ubuntu 14.04.5 LTS.
Tests done in VirtualBox on Ubuntu via Vagrant(1.8.6) using `python3` (version 3.4.3).

#### Style
All files are written in the PEP 8 style.
Information about this style can be found at https://www.python.org/dev/peps/pep-0008/

## Files
All files must be executable to run. To add executable permissions to any file: `chmod u+x file_name`

##### `0-run`
Shell script that runs a Python script.
* script will use environment variable `$PYFILE`
	* to use, `export PYFILE=main.py`
* `main.py`: Python script to run, if you do not have this file, please create with the contents listed.
	* contents of file:
	```
	#!/usr/bin/python3
	print("Holberton School")
	```
* To use: run `./main.py`

#### `1-run_inline`
Shell script that runs Python code.
* script will use environment variable `$PYCODE`
	* to use: `export PYCODE='print("Holberton School: {}".format(88+10))'`
* to run: `./1-run_inline`

#### `2-print.py`
Python script that prints `"Programming is like building a multilingual puzzle`.
* to run: `./2-print.py`

#### `3-print_number.py`
Python script to print the integer stored in variable `number`, followed by `Battery street`
* to run: `./3-print_number.py`

#### `4-print_float.py`
Python script that prints the float stored in variable `number` with a precision of 2 digits.
* to run: `./4-print_float.py`

#### `5-print_string.py`
Python script to print the variable in `str` 3 times, followed by its first 9 characters/
* to run: `./-print_string.py`

#### `6-concat.py`
Python script to print `Welcome to Holberton School!`.
* to run: `./6-concat.py`

#### `7-edges.py`
Python script to print the following from variable `word`: first 3 letters, last 2 letters, and all letters but the first and last.
* to run: `./7-edges.py`

#### `8-concat_edges.py`
Python script to print `object-oriented programming with Python` from the variable `str`
* to run: `./8-concat_edges.py`

#### `9-easter_egg.py`
Python script that prints "The Zen of Python", by Tim Peters.
* to run: `./9-easter_egg.py`

## Authors
Kristen Loyd        <a href='https://github.com/KRLoyd'>Github</a> ,  <a href='https://www.linkedin.com/in/kristen-loyd-34984a92/'>Linkedin</a>

## License
Public Domain, no copyright protection
