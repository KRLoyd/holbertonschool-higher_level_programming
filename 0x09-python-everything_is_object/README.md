# 0x09. Python - Everything is object

## Purpose
Most files in this folder are answer files for a Holberton School project that asked a variety of questions about working with Python objects.

### Project Notes
#### Environment
Functions have been tested on Ubuntu 14.04.5 LTS.
Tests done in VirtualBox on Ubuntu via Vagrant(1.8.6) using `python3` (version 3.4.3).

#### Style
All .txt files are one line long and end with a new line.

All python are written in the PEP 8 style.
Information about this style can be found at https://www.python.org/dev/peps/pep-0008/

## Files
To add executable permissions to a file: `chmod u+x file_name`

##### [0-answer.txt](0-answer.txt)
The name of the function to print the type of an object.

##### [1-answer.txt](1-answer.txt)
The name of the function to get a variable identifier (the memory address in CPython implementation).

##### [2-answer.txt](2-answer.txt)
Answer to the following question:
 * In the below code, do `a` and `b` pointer to the same object?
  ```
  >>> a = 89
  >>> b = 100
  ```

##### [3-answer.txt](3-answer.txt)
Answer to the following question:
 * In the below code, do `a` and `b` pointer to the same object?
  ```
  >>> a = 89
  >>> b = 89
  ```

##### [4-answer.txt](4-answer.txt)
Answer to the following question:
 * In the below code, do `a` and `b` pointer to the same object?
  ```
  >>> a = 89
  >>> b = a
  ```

##### [5-answer.txt](5-answer.txt)
Answer to the following question:
 * In the below code, do `a` and `b` pointer to the same object?
  ```
  >>> a = 89
  >>> b = a + 1
  ```

##### [6-answer.txt](6-answer.txt)
Answer to the following question:
 * What should the following 3 lines print?
  ```
  >>> s1 = "Holberton"
  >>> s2 = s1
  >>> print(s1 == s2)
  ```

##### [7-answer.txt](7-answer.txt)
Answer to the following question:
 * What should the following 3 lines print?
  ```
  >>> s1 = "Holberton"
  >>> s2 = s1
  >>> print(s1 is s2)
  ```

##### [8-answer.txt](8-answer.txt)
Answer to the following question:
 * What should the following 3 lines print?
  ```
  >>> s1 = "Holberton"
  >>> s2 = "Holberton"
  >>> print(s1 == s2)
  ```

##### [9-answer.txt](9-answer.txt)
Answer to the following question:
 * What should the following 3 lines print?
  ```
  >>> s1 = "Holberton"
  >>> s2 = "Holberton"
  >>> print(s1 is s2)
  ```

##### [10-answer.txt](10-answer.txt)
Answer to the following question:
 * What should the following 3 lines print?
  ```
  >>> l1 = [1, 2, 3]
  >>> l2 = [1, 2, 3]
  >>> print(l1 == l2)
  ```

##### [11-answer.txt](11-answer.txt)
Answer to the following question:
 * What should the following 3 lines print?
  ```
  >>> l1 = [1, 2, 3]
  >>> l2 = [1, 2, 3]
  >>> print(l1 is l2)
  ```

##### [12-answer.txt](12-answer.txt)
Answer to the following question:
 * What should the following 3 lines print?
  ```
  >>> l1 = [1, 2, 3]
  >>> l2 = l1
  >>> print(l1 == l2)
  ```

##### [13-answer.txt](13-answer.txt)
Answer to the following question:
 * What should the following 3 lines print?
  ```
  >>> l1 = [1, 2, 3]
  >>> l2 = l1
  >>> print(l1 is l2)
  ```

##### [14-answer.txt](14-answer.txt)
Answer to the following question:
 * What does this script print?
  ```
  l1 = [1, 2, 3]
  l2 = l1
  l1.append(4)
  print(l2)
  ```

##### [15-answer.txt](15-answer.txt)
Answer to the following question:
 * What does this script print?
  ```
  l1 = [1, 2, 3]
  l2 = l1
  l1 = l1 + [4]
  print(l2)
  ```

##### [16-answer.txt](16-answer.txt)
Answer to the following question:
 * What does this script print?
  ```
  def increment(n):
     n += 1
  
  a = 1
  increment(a)
  print(a)
  ```


##### [17-answer.txt](17-answer.txt)
Answer to the following question:
 * What does this script print?
  ```
  def increment(n):
     n.append(4)
  
  l = [1, 2, 3]
  increment(l)
  print(l)
  ```


##### [18-answer.txt](18-answer.txt)
Answer to the following question:
 * What does this script print?
  ```
  def assign_value(n, v):
     n = v
  
  l1 = [1, 2, 3]
  l2 = [4, 5, 6]
  assign_value(l1, l2)
  print(l1)
  ```

##### [19-copy_list.py](19-copy_list.py)
Function `def copy_list(l):`. Returns a copy of a list.
* To be used with [main-19.py](my_mains/main-19.py)

##### [20-answer.txt](20-answer.txt)
Answer to the following question:
  * In the following code, is `a` a tuple?
  ```
  a = ()
  ```

##### [21-answer.txt](21-answer.txt)
Answer to the following question:
  * In the following code, is `a` a tuple?
  ```
  a = (1, 2)
  ```

##### [22-answer.txt](22-answer.txt)
Answer to the following question:
  * In the following code, is `a` a tuple?
  ```
  a = (1)
  ```

##### [23-answer.txt](23-answer.txt)
Answer to the following question:
  * In the following code, is `a` a tuple?
  ```
  a = (1, )
  ```

##### [24-answer.txt](24-answer.txt)
Answer to the following question:
 * What does this script print?
  ```
  a = (1)
  b = (1)
  a is b
  ```

##### [25-answer.txt](25-answer.txt)
Answer to the following question:
 * What does this script print?
  ```
  a = (1, 2)
  b = (1, 2)
  a is b
  ```

##### [26-answer.txt](26-answer.txt)
Answer to the following question:
 * What does this script print?
  ```
  a = ()
  b = ()
  a is b
  ```

##### [27-answer.txt](27-answer.txt)
Answer to the following question:
 * Will the last line of this script print `139926795932424`?
  ```
  >>> id(a)
  139926795932424
  >>> a 
  [1, 2, 3, 4]
  >>> a = a + [5]
  >>> id(a)
  ```

##### [28-answer.txt](28-answer.txt)
Answer to the following question:
 * Will the last line of this script print `139926795932424`?
  ```
  >>> a
  [1, 2, 3]
  >>> id(a)
  139926795932424
  >>> a += [4]
  >>> id(a)
  ```


## Authors
Kristen Loyd        <a href='https://github.com/KRLoyd'>Github</a> ,  <a href='https://www.linkedin.com/in/kristen-loyd-34984a92/'>Linkedin</a>

## License
Public Domain, no copyright protection
