# 0x11. Python - Network #1

## Description
Files in this directory correspond to tasks in the Holberton School project to continue working with `requests` in Python.

### Project Notes
#### Environment
These functions have been tested on Ubuntu 14.04.5 LTS.
Tests done in VirtualBox on Ubuntu via Vagrant(1.8.6) using `python3` (version 3.4.3).

#### Style
All files are written in the PEP 8 style.
Information about this style can be found at https://www.python.org/dev/peps/pep-0008/

## Files
All files must be executable to run. To add executable permissions to any file: `chmod u+x file_name`

##### [0-hbtn_status.py](0-hbtn_status.py)
Script that fetches `https://intranet.hbtn.io/status`.
* Usage:
```
$ ./0-hbtn_status.py | cat -e
Body response:$
    - type: <class 'bytes'>$
    - content: b'OK'$
    - utf8 content: OK$
$
```

##### [1-hbtn_header.py](1-hbtn_header.py)
Script that takes in a URL, sends a request to the URL, and displays the value of `X-Request_id` variable found in the header of the response.
* Usage:
```
$ ./1-hbtn_header.py https://intranet.hbtn.io
ade2627e-41dd-4c34-b9d9-a0fa0f47b237
$
```

##### [2-post_email.py](2-post_email.py)
Script to take in a URL and an email, sends a `POST` request to the URL with the email as a parameter, and displays the body of the response decoded in `utf-8`.
* Usage:
```
$ ./2-post_email.py http://0.0.0.0:5000/post_email hr@holbertonschool.com
Your email is: hr@holbertonschool.com
$
```

##### [3-error_code.py](3-error_code.py)
Script to take in a URL, sends a request to the URL, and displays the body of the response decoded in `utf-8`.
* Notes:
  * `urllib.error.HTTPError` exceptions are managed
    * Prints `Error code:` and the HTTP status code
* Usage:
```
$ ./3-error_code.py http://0.0.0.0:5000
Index
$ ./3-error_code.py http://0.0.0.0:5000/status_401
Error code: 401
$ ./3-error_code.py http://0.0.0.0:5000/doesnt_exist
Error code: 404
$ ./3-error_code.py http://0.0.0.0:5000/status_500
Error code: 500
$
```

##### [4-hbtn_status.py](4-hbtn_status.py)
Script that fetches `https://intranet.hbtn.io/status`.
* Usage:
```
$ ./4-hbtn_status.py | cat -e
Body response:$
    - type: <class 'str'>$
    - content: OK$
$
```

##### [5-hbtn_header.py](5-hbtn_header.py)
Script that takes in a URL, sends a request to the URL, and displays the value of the variable `X-Request-Id` in the response header.
* Usage:
```
$ ./5-hbtn_header.py https://intranet.hbtn.io
5e52e160-c822-4669-8b3a-8b3bbca7b090
$
```

##### [6-post_email.py](6-post_email.py)
Script to take in a URL and email address, sends a `POST` request to the URL with the email as a parameter, and displays the body of the response.
* Usage:
```
$ ./6-post_email.py http://0.0.0.0:5000/post_email hr@holbertonschool.com
Your email is: hr@holbertonschool.com
$
```

##### [7-error_code.py](7-error_code.py)
Script to take in a URL, send a request to the URL, and displays the body of the response.
* Usage:
```
$ ./7-error_code.py http://0.0.0.0:5000
Index
$ ./7-error_code.py http://0.0.0.0:5000/status_401
Error code: 401
$ ./7-error_code.py http://0.0.0.0:5000/doesnt_exist
Error code: 404
$ ./7-error_code.py http://0.0.0.0:5000/status_500
Error code: 500
$
```

##### [8-json_api.py](8-json_api.py)
Script that takes in a letter and sends a `POST` request to `http://0.0.0.0:5000/search_user` with the letter as a parameter.
* Notes
  * The letter must be sent in the variable `q`
  * If no argument is given, `q=""`
  * If the response body is properly JSON formatted and not empty, `id` and `name` are displayed
  * If JSON is invalid: displays `Not a valid JSON`
  * If JSON is empty: displays `No result`
* Usage:
```
$ ./8-json_api.py 
No result
$ ./8-json_api.py a
[8446] amnirqhtfjq
$ ./8-json_api.py 2
No result
$ ./8-json_api.py b
[7094] bmofakakhke
$
```

##### [9-starwars.py](9-starwars.py)
Script that takes in a string and sends a serach request to the [Star Wars API](https://swapi.co/documentation).
* NOtes:
  * The string argument is used as the `search` value of the request
  * Displays: `Number of results: <count>` and the list of names
* Usage:
```
$ ./9-starwars.py r2
Number of results: 1
R2-D2
$ ./9-starwars.py lu
Number of results: 2
Luke Skywalker
Luminara Unduli
$ ./9-starwars.py ju
Number of results: 0
$ ./9-starwars.py g
Number of results: 16
Leia Organa
Biggs Darklighter
Greedo
Wedge Antilles
IG-88
Qui-Gon Jinn
Nute Gunray
Rugor Nass
Gasgano
Adi Gallia
$
```

##### [10-my_github.py](10-my_github.py)
Script to take your Github credentials and uses the [Github API](https://developer.github.com/v3/users/#get-the-authenticated-user) to display your `id`.
* Notes:
  * First argument is username
  * Second argument is password
* Usage: `./10-my_github.py <username> <password>`

##### []()


	
## Authors
Kristen Loyd        [Github](https://github.com/KRLoyd) |  [LinkedIn](https://www.linkedin.com/in/kristen-loyd-34984a92)

## License
Public Domain, no copyright protection
