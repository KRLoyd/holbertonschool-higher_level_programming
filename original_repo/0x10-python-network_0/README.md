# 0x10. Python - Network #0

## Description
The files in this directory correspond to tasks in a Holberton School project to use Bash scripts to request web pages and display information.

### Project Notes
#### Environment
These Bash scripts have been tested on Ubuntu 14.04.5 LTS.
Tests and development are done in VirtualBox on Ubuntu via Vagrant(1.8.1).
#### Style
`Shellchecker` was used to check all Bash scripts.


## Files
All files must be executable to run. To add executable permissions to any file: `chmod u+x file_name`

##### [0-body_size.sh](0-body_size.sh)
Script that takes in a URL, sends a request to the URL, and displays the size of the body of the response.
* Notes:
  * The size is displayed in bytes
* Usage: `./0-body_size.sh <URL>`

##### [1-body.sh](1-body.sh)
Script to take in a URL, send a `GET` request to the URL, and displays the body of the response, if it has a `200` status code response.
* Usage: `./1-body.sh <URL> ; echo ""`

##### [2-delete.sh](2-delete.sh)
Script to send a `DELETE` request to the URL passed at the first argument and displays the body of the response.
* Usage: `./2-delete.sh <URL>  ; echo ""`

##### [3-methods.sh](3-methods.sh)
Script to take in a URL and displays all HTTP methods the server will accept.
* Usage: `./3-methods.sh <URL>`

##### [4-header.sh](4-header.sh)
Script to take in a URL as an argument, sends a `GET` request to the URL, and displays the body of the response.
* Note:
  * A header variable `X-HolbertonSchool-User-Id` with value `98` is sent with the request
* Usage: `./4-header.sh <URL>`

##### [5-post_params.sh](5-post_params.sh)
Script to take in a URL, send a `POST` request to the URL, and displays the body of the response.
* Variables sent:
  * `email` with value `hr@holbertonschool.com`
  * `subject` with value `I will always be here for PLD`
* Usage: `./5-post_params.sh <URL>`


## Authors
Kristen Loyd        [Github](https://github.com/KRLoyd) |  [LinkedIn](https://www.linkedin.com/in/kristen-loyd-34984a92)

## License
Public Domain, no copyright protection
