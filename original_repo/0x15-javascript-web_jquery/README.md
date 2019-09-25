# 0x15. Javascript - Web JQuery

## Description
Files in this directory correspond with tasks in a Holberton School project to continue working with Javascript; this time, we are adding JQuesry to begin making dynamic content.

### Project Notes
#### Environment
These functions have been tested on Ubuntu 14.04.5 LTS.
Tests done in VirtualBox on Ubuntu via Vagrant(1.8.6) using `python3` (version 3.4.3).

#### Style
All files are `semistandard` compliant with the flag `--global`.
Information about this style can be found at https://standardjs.com/rules.html and https://github.com/Flet/semistandard .

## Files

##### [0-script.js](0-script.js)
Script to update the text color of the HTML tag `HEADER` to red (`#FF0000`).
* Notes
  * Uses `document.querySelector`
  * To be used with [0-main.html](0-main.html).

##### [1-script.js](1-script.js)
Script to update the text color of the HTML tag `HEADER` to red (`#FF0000`).
* Notes
  * Uses the jQuery API
  * To be used with [1-main.html](1-main.html)

##### [2-script.js](2-script.js)
Script to update the text color of the HTML tag `HEADER` to red (`#FF0000`) when the user clicks on the tag `DIV#red_header`.
* Notes
  * Uses the jQuery API
  * To be used with [2-main.html](2-main.html)

##### [3-script.js](3-script.js)
Script to add the class `red` to the HTML tag `HEADER` when the user clicks on the tag `DIV#red_header`.
* Notes
  * Uses the jQuery API
  * To be used with [3-main.html](3-main.html)

##### [4-script.js](4-script.js)
Script to toggle the class of the HTML tag `HEADER` when the user clicks on the tag `DIV#toggle_header`.
* Notes
  * Uses the jQuery API
  * Class is toggled between `red` and `green`
  * To be used with [4-main.html](4-main.html)

##### [5-script.js](5-script.js)
Script to add a `LI` element to a list when the user clicks on the tag `DIV#add_item`.
* Notes
  * Uses the jQuery API
  * New element is `<li>Item</li>`
  * New element is added to `UL.my_list`
  * To be used with [5-main.html](5-main.html)

##### [6-script.js](6-script.js)
Script to update the text of the HTML tag `HEADER` to "New Header!!!" when user clicks on `DIV#update_header`.
* Notes
  * Uses the jQuery API
  * To be used with [6-main.html](6-main.html)

##### [7-script.js](7-script.js)
Script to fetch and replace the `name` of URL `http://swapi.co/api/people/5/?format=json`.
* Notes
  * Name is displayed in the HTML tag `DIV#character`
  * Uses the jQuery API
  * To be used with [7-main.html](7-main.html)

##### [8-script.js](8-script.js)
Script that fetches all movies `title` by using URL `http://swapi.co/api/films?format=json`.
* Notes
  * All movie titles are listed in the HTML tag `UL#list_movies`
  * Uses the jQuery API
  * To be used with [8-main.html](8-main.html)

##### [9-script.js](9-script.js)
Script to fetch and print the San Francisco wind speed by using URL `https://query.yahooapis.com/v1/public/yql?q=select%20wind%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22San%20Francisco%2C%20CA%22)&format=json`.
* Notes
  * Wind speed is displayed in the HTML tag `DIV#sf_wind_speed`
  * Uses the jQuery API
  * To be used with [9-main.html](9-main.html)


## Authors
Kristen Loyd        [Github](https://github.com/KRLoyd) |  [LinkedIn](https://www.linkedin.com/in/kristen-loyd-34984a92)

## License
Public Domain, no copyright protection