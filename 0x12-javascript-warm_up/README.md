# 0x12. Javascript - Warm up

## Description
Tasks to start working with JavaScript!

### Project Notes
#### Environment
These functions have been tested on Ubuntu 14.04.5 LTS.
Tests done in VirtualBox on Ubuntu via Vagrant(1.8.6) using `nodejs`.

To install Node 6:
```
$ curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash -
$ sudo apt-get install -y nodejs
```

#### Style
All files are `semistandard` compliant.
Information about this style can be found at https://standardjs.com/rules.html and https://github.com/Flet/semistandard .

To install semi-standard:
```
$ sudo npm install semistandard --global
```

## Files
All files must be executable to run. To add executable permissions to any file: `chmod u+x file_name`

##### [0-javascript_is_amazing.js](0-javascript_is_amazing.js)
Script that prints "Javascript is amazing".
* Notes
	* Uses a constant variable `myVar` with value of "Javascript is amazing"
* Usage: `./0-javascript_is_amazing.js`

##### [1-multi_languages.js](1-multi_languages.js)
Script to print 3 lines.
* Notes
  * Lines to print
    * First: "C is fun"
    * Second: "Python is cool"
    * Third: "Javascript is amazing"
* Usage: `./1-multi_languages.js`

##### [2-arguments.js](2-arguments.js)
Script to print a message depending on the number of arguments passed.
* Notes:
  * No arguments: Prints "No Argument"
  * One argument: Prints "Argument found"
  * More than one argument: Prints "Arguments found"
* Usage: `./2-arguments.js [<arg 1> <arg 2> ... <arg n>]`

##### [3-value_argument.js](3-value_argument.js)
Script to print the first argument passed to it.
* Notes:
  * No arguments: Prints "No argument"
  * One or more arguments: Prints the first argument
* Usage: `./3-value_argument.js [<arg 1> <arg 2> ... <arg n>]`

##### [4-concat.js](4-concat.js)
Script to print two arguments passed to it in the format "`<arg 1>` is `<arg 2>`".
* Usage: 
```
$ ./4-concat.js c cool
c is cool
$ ./4-concat.js c 
c is undefined
$ ./4-concat.js
undefined is undefined
$
```

##### [5-to_integer.js](5-to_integer.js)
Script to print "My number: " and the number if the first argument can be converted to an integer.
* Notes:
  * If the argument cannot be converted to a number, prints "Not a number"
* Usage:
```
$ ./5-to_integer.js 
Not a number
$ ./5-to_integer.js 89
My number: 89
$ ./5-to_integer.js "89"
My number: 89
$ ./5-to_integer.js 89.89
My number: 89
$ ./5-to_integer.js Holberton
Not a number
$
```

##### [6-multi_languages_loop.js](6-multi_languages_loop.js)
Script to print three lines (same lines as [1-multi_languages.js](1-multi_languages.js)) using an array of strings and a loop.
* Usage: `./6-multi_languages_loop.js`

##### [7-multi_c.js](7-multi_c.js)
Script to print `x` times "C is fun".
* Notes:
  * `x` is the first argument of the script
    * If it cannot be converted to an integer, "Missing number of occurences" is printed.
* Usage:
```
$ ./7-multi_c.js 2
C is fun
C is fun
$ ./7-multi_c.js 5
C is fun
C is fun
C is fun
C is fun
C is fun
$ ./7-multi_c.js 
Missing number of occurrences
$ ./7-multi_c.js -3
$
```

##### [8-square.js](8-square.js)
Script to print a square.
* Notes:
  * First arguments is the size of the square
    * If it cannot be converted to an integer, "Missing size" is printed
  * Character `X` is used to print
* Usage:
```
$ ./8-square.js
Missing size
$ ./8-square.js Holberton
Missing size
$ ./8-square.js 2
XX
XX
$ ./8-square.js 6
XXXXXX
XXXXXX
XXXXXX
XXXXXX
XXXXXX
XXXXXX
$ ./8-square.js -3
$
```

##### [9-add,js](9-add.js)
Script to print the addition of two integers.
* Notes:
  * First argument is first integer
  * Second argument is second integer
  * Function prototype: `function add(a, b)`
* Usage: 
```
$ ./9-add.js 
NaN
$ ./9-add.js 1
NaN
$ ./9-add.js 1 7
8
$ ./9-add.js 13 89
102
$
```

##### [10-factorial.js](10-factorial.js)
Script to compute and print a factorial.
* Notes:
  * First argument is the integer for computing the factorial
  * Factorial of `NaN` is `1`
* Usage:
```
$ ./10-factorial.js 
1
$ ./10-factorial.js 3
6
$ ./10-factorial.js 89
1.6507955160908452e+136
$ ./10-factorial.js 333
Infinity
$
```

##### [11-second_biggest.js](11-second_biggest.js)
Script that searches for the second biggest integer in a list of arguments.
* Notes:
  * If no argument is passed, `0` is printed
  * If the number of arguments is 1, `0` is printed
* Usage:
```
$ ./11-second_biggest.js 
0
$ ./11-second_biggest.js 1
0
$ ./11-second_biggest.js 4 2 5 3 0 -3
4
```

##### []()
Update script template from Holberton School to replace the value `12` with `89`.
* Original script:
```
cat 12-object.js
#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
/*
YOUR CODE HERE
*/
console.log(myObject);`
```

##### [13-add.js](13-add.js)
Function that returns the addition of 2 integers.
* Notes:
  * Function is visible from outside the file.
  * Name of the function is `add`
  * Used by [13-main.js](13-main.js)


## Authors
Kristen Loyd        [Github](https://github.com/KRLoyd) |  [LinkedIn](https://www.linkedin.com/in/kristen-loyd-34984a92)

## License
Public Domain, no copyright protection
