# 0x14. Javascript - Web scraping

## Description
Tasks in this directory are from Holberton School's project 333 to practice web scraping with JavaSript.

### Project Notes
#### Environment
These functions have been tested on Ubuntu 14.04.5 LTS.
Tests done in VirtualBox on Ubuntu via Vagrant(1.8.6) using `python3` (version 3.4.3).

#### Style
All files are `semistandard` compliant.
Information about this style can be found at https://standardjs.com/rules.html and https://github.com/Flet/semistandard .

## Files
All files must be executable to run. To add executable permissions to any file: `chmod u+x file_name`

##### [0-readme.js](0-readme.js)
Script that reads and prints the content of a file. If an error occurs during reading, the error objec tis printed.
* Usage: `./0-readme.js <file name>`

##### [1-writeme.js](1-writeme.js)
Script to write a string to a file. If an error occurs during writing, the error object is printed.
* Usage: `./1-writeme.js <file path> <string to write>`

##### [2-statuscode.js](2-statuscode.js)
Script to display the status code of a `GET` request.
* Usage: `./2-statuscode.js <url to request>`

##### [3-starwars_title.js](3-starwars_title.js)
Script to print the title of a Star Wars movie where the episode number matches a given integer.
* Usage: `./3-starwars_title.js <episode number>`

##### [4-starwars_count.js](4-starwars_count.js)
Script to print the number of movies where the character "Wedge Antilles" is present.
* Usage: `./4-starwars_count.js http://swapi.co/api/films`

##### [5-request_store.js](5-request_store.js)
Script to get the contents of a webpage and store it in a file.
* Usage: `./5-request_store.js <url to request> <file path>`

##### [6-completed_tasks.js](6-completed_tasks.js)
Script to compute the number of tasks completed by user id.
* Usage: `./6-completed_tasks.js https://jsonplaceholder.typicode.com/todos`

## Authors
Kristen Loyd        [Github](https://github.com/KRLoyd) |  [LinkedIn](https://www.linkedin.com/in/kristen-loyd-34984a92)

## License
Public Domain, no copyright protection