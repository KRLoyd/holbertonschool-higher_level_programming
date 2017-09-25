# 0x13. Javascript - Objects, Scopes and Closures

## Description
Scripts in this directory are related to tasks in Holberton School project 304 to practice creating objects in JavaScript.

### Project Notes
#### Environment
These functions have been tested on Ubuntu 14.04.5 LTS.
Tests done in VirtualBox on Ubuntu via Vagrant(1.8.6) using `python3` (version 3.4.3).

#### Style
All files are `semistandard` compliant.
Information about this style can be found at https://standardjs.com/rules.html and https://github.com/Flet/semistandard .

## Files
All files must be executable to run. To add executable permissions to any file: `chmod u+x file_name`

##### [0-rectangle.js](0-rectangle.js)
Script that defines an empty class `Rectangle`.

##### [1-rectangle.js](1-rectangle.js)
Script that defines class `Rectangle`.
* Constructor takes two arguments: `w`, `h`
* Instance attributes initialized:
  * `width` with value `w`
  * `height` with value `h`

##### [3-rectangle.js](3-rectangle.js)
Script that defines class `Rectangle`.
* Constructor takes two arguments: `w`, `h`
* Instance attributes initialized:
  * `width` with value `w`
  * `height` with value `h`
* Instance methods:
  * `print()`: prints the rectangle using character `X`
* Notes:
  * If attributes are <= 0, an empty object is created

##### [4-rectangle.js](4-rectangle.js)
Script that defines class `Rectangle`.
* Constructor takes two arguments: `w`, `h`
* Instance attributes initialized:
  * `width` with value `w`
  * `height` with value `h`
* Instance methods:
  * `print()`: prints the rectangle using character `X`
  * `rotate()`: exchanges the `width` and `height` of the rectangle
  * `double()`: multiplies `width` and `height` of rectangle by 2
* Notes:
  * If attributes are <= 0, an empty object is created

##### [5-square.js](5-square.js)
Script that defines class `Square` that inherits from `Rectangle` of [4-rectangle.js](4-rectangle.js).
* Constructor takes one argument: `size`
* Notes:
  * Constructor of `Rectangle` is called

##### [6-square.js](6-square.js)
Script that defines class `Square` that inherits from `Square` of [5-square.js](5-square.js).
* Instance method:
  * `charPrint(c)`: prints the rectangle using character `c`
* Notes:
  * If `c` is undefined, character `X` is used

##### [7-occurrences.js](7-occurences.js)
Function that returns the number of occurances in a list.
* Prototype: `exports.nbOccurences = function (list, search_element)`
  * @list: list to evaluate
  * @search_element: item to count occurances of from `list`

##### [8-esrever.js](8-esrever.js)
Function that returns the reserved version of a list.
* Prototype: `exports.esrever = function (list)`
  * @list: list to evaluate

##### [9-logme.js](9-logme.js)
Function that prints the number of arguments already printed and the new argument value.
* Prototype: `exports.logMe = function (item)`
  * @item: item to print
* Output format: `<number of arguments already printed>: <current argument value>`

#### [mains](mains)
Folder to hold all main files to test JavaScript scripts in this directory.


## Authors
Kristen Loyd        [Github](https://github.com/KRLoyd) |  [LinkedIn](https://www.linkedin.com/in/kristen-loyd-34984a92)

## License
Public Domain, no copyright protection