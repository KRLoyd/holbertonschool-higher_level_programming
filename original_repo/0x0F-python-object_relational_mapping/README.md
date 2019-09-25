# 0x0F. Python - Object-relational mapping

## Description
Tasks are to link databases and Python. Some tasks use the module `MySQLdb` to connect to a MySQL database and execute SQL queries. Other tasks use the module `SQLAlchemy`, an Object Relational Mapper (ORM).

### Project Notes
#### Environment
These functions have been tested on Ubuntu 14.04.5 LTS.
Tests done in VirtualBox on Ubuntu via Vagrant(1.8.6) using `python3` (version 3.4.3).

#### Tools
##### `MySQLdb`
To install the `MySQLdb` module:
```
$ sudo apt-get install python3-dev
$ sudo apt-get install libmysqlclient-dev
$ sudo apt-get install zlib1g-dev
$ sudo pip3 install mysqlclient
...
$ python3
>>> import MySQLdb
>>> MySQLdb.__version__ 
'1.3.10'
```

##### `SQLAlchemy`
To install the `SQLAlchemy` module:
```
$ pip3 install SQLAlchemy
...
$ python3
>>> import sqlalchemy
>>> sqlalchemy.__version__ 
'1.1.6'
```

#### Style
All files are written in the PEP 8 style.
Information about this style can be found at https://www.python.org/dev/peps/pep-0008/

## Files
All files must be executable to run. To add executable permissions to any file: `chmod u+x file_name`

##### [0-select_states.py](0-select_states.py)
Scipt that lists all `states` from the database `hbtn_0e_0_usa`.
* Notes:
  * Script takes 3 arguments:
    * `mysql username`
    * `mysql password`
    * `database name`
  * Uses the `MySQLdb` module
  * Connects to a MySQL server running on `localhost` at port `3306`
  * Results are sorted in ascending order by `states.id`
  * Use [0-select_states.sql](0-select_states.sql) to create the database and table if they don't exist
* Usage: 
  ```
  $ cat 0-select_states.sql | mysql -uroot -p
  Enter password: 
  $ ./0-select_states.py root root hbtn_0e_0_usa
  (1, 'California')
  (2, 'Arizona')
  (3, 'Texas')
  (4, 'New York')
  (5, 'Nevada')
  $
  ```

##### [1-filter_states.py](1-filter_states.py)
Script to list all `states` with a `name` starting with `N` from the database `hbtn_0e_0_usa`.
* Notes:
  * Script takes 3 arguments:
    * `mysql username`
    * `mysql password`
    * `database name`
  * Uses the `MySQLdb` module
  * Connects to a MySQL server running on `localhost` at port `3306`
  * Results are sorted in ascending order by `states.id`
  * Use [0-select_states.sql](0-select_states.sql) to create the databse and table if they don't exist
* Usage:
  ```
  $ cat 0-select_states.sql | mysql -uroot -p
  Enter password: 
  $ ./1-filter_states.py root root hbtn_0e_0_usa
  (4, 'New York')
  (5, 'Nevada')
  $
  ```

##### [2-my_filter_states.py](2-my_filter_states.py)
Script that takes in an argument and displays all values in the `states` table of `hbnb_0e_0_usa` where `name` matches the argument.
* Notes:
  * Script takes 4 arguments:
    * `mysql username`
    * `mysql password`
    * `database name`
    * `state name searched`
  * Uses the `MySQLdb` module
  * Connects to a MySQL server running on `localhost` at port `3306`
  * Results are sorted in ascending order by `states.id`
  * Use [0-select_states.sql](0-select_states.sql) to create the database and table if they don't exist
* Usage:
  ```
  $ cat 0-select_states.sql | mysql -uroot -p
  Enter password: 
  $ ./2-my_filter_states.py root root hbtn_0e_0_usa 'Arizona'
  (2, 'Arizona')
  $
  ```

##### []()
Script that is safe from MySQL injections and takes in arguments and displays all values in the `states` table of `hbtn_0e_0_usa` where `name` matches the argument.
* Notes:
  * Script takes 4 arguments:
    * `mysql username`
    * `mysql password`
    * `database name`
    * `state name searched`
  * Uses the `MySQLdb` module
  * Connects to a MySQL server running on `localhost` at port `3306`
  * Results are sorted in ascending order by `states.id`
  * Use [0-select_states.sql](0-select_states.sql) to create the database and table if they don't exist
* Usage:
  ```
  $ cat 0-select_states.sql | mysql -uroot -p
  Enter password: 
  $ ./3-my_safe_filter_states.py root root hbtn_0e_0_usa 'Arizona'
  (2, 'Arizona')
  $
  ```

##### [4-cities_by_state.py](4-cities_by_state.py)
Script that lists all `cities` from the database `hbtn_0e_4_usa`.
* Notes:
  * Script takes 3 arguments:
    * `mysql username`
    * `mysql password`
    * `database name`
  * Uses the `MySQLdb` module
  * Connects to a MySQL server running on `localhost` at port `3306`
  * Results are sorted in ascending order by `cities.id`
  * Use [4-cities_by_state.sql](4-cities_by_state.sql) to create the database and table if they don't exist
* Usage: 
  ```
  $ cat 4-cities_by_state.sql | mysql -uroot -p
  Enter password: 
  $ ./4-cities_by_state.py root root hbtn_0e_4_usa
  (1, 'San Francisco', 'California')
  (2, 'San Jose', 'California')
  (3, 'Los Angeles', 'California')
  (4, 'Fremont', 'California')
  (5, 'Livermore', 'California')
  (6, 'Page', 'Arizona')
  (7, 'Phoenix', 'Arizona')
  (8, 'Dallas', 'Texas')
  (9, 'Houston', 'Texas')
  (10, 'Austin', 'Texas')
  (11, 'New York', 'New York')
  (12, 'Las Vegas', 'Nevada')
  (13, 'Reno', 'Nevada')
  (14, 'Henderson', 'Nevada')
  (15, 'Carson City', 'Nevada')
  $
  ```

##### [5-filter_cities.py](5-filter_cities.py)
Script that takes in the name of a state as an argument and lists all `cities` of that state, using the database `hbtn_0e_4_usa`.
* Notes:
  * Script takes 4 arguments:
    * `mysql username`
    * `mysql password`
    * `database name`
    * `state name`
  * Uses the `MySQLdb` module
  * Connects to a MySQL server running on `localhost` at port `3306`
  * Results are sorted in ascending order by `cities.id`
  * Use [4-cities_by_state.sql](4-cities_by_state.sql) to create the database and table if they don't exist
* Usage: 
  ```
  $ cat 4-cities_by_state.sql | mysql -uroot -p
  Enter password: 
  $ ./5-filter_cities.py root root hbtn_0e_4_usa Texas
  Dallas, Houston, Austin
  $
  ```

##### [model_state.py](model_state.py)
Python file that contains the class definition of a `State` and an instance `Base = declarative_base()`.
* Notes:
  * `State` information:
    * inherits from `Base`
    * links to the MySQL table `states`
    * Class attributes
      * `id`: a column of an auto-generated, unique integer, can't be null, is primary key
      * `name`: a column of a string with maximum 128 characters and can't be null
    * Uses `SQLAlchemy` module
    * Connects to a MySQL server running on `localhost` at port `3306`
    * Use [6-model_state.sql](6-model_state.sql) to create the database and table if they don't exist
    * Use [6-model_state.py](6-model_state.py) to link the class to the database
* Usage: 
  ```
  $ ./6-model_state.py root root hbtn_0e_6_usa
  $ cat 6-model_state.sql | mysql -uroot -p
  Enter password: 
  Table   Create Table
  states  CREATE TABLE `states` (\n  `id` int(11) NOT NULL AUTO_INCREMENT,\n  `name` varchar(128) NOT NULL,\n  PRIMARY KEY    (`id`)\n) ENGINE=InnoDB DEFAULT CHARSET=latin1
  $
  ```

##### [7-model_state_fetch_all.py](7-model_state_fetch_all.py)
Script to list all `State` objects from database `hbtn_0e_6_usa`.
* Notes:
  * Script takes 3 arguments:
    * `mysql username`
    * `mysql password`
    * `database name`
  * Uses the `SQLAlchemy` module
  * Connects to a MySQL server running on `localhost` at port `3306`
  * Results are sorted in ascending order by `states.id`
  * Use [7-model_state_fetch_all.sql](7-model_state_fetch_all.sql) to create the database and table if they don't exist
* Usage:
  ```
  $ cat 7-model_state_fetch_all.sql | mysql -uroot -p hbtn_0e_6_usa
  Enter password: 
  $ ./7-model_state_fetch_all.py root root hbtn_0e_6_usa
  1: California
  2: Arizona
  3: Texas
  4: New York
  5: Nevada
  $
  ```

##### [8-model_state_fetch_first.py](8-model_state_fetch_first.py)
Script that prints the first `State` object form the database `hbtn_0e_6_usa`.
* Notes:
  * Script takes 3 arguments:
    * `mysql username`
    * `mysql password`
    * `database name`
  * Uses the `SQLAlchemy` module
  * Connects to a MySQL server running on `localhost` at port `3306`
  * Results are sorted in ascending order by `states.id`
  * If table `states` is empty, `Nothing` is printed
* Usage:
  ```
  $ ./8-model_state_fetch_first.py root root hbtn_0e_6_usa
  1: California
  $
  ```

##### [9-model_state_filter_a.py](9-model_state_filter_a.py)
Script to list all `State` objects that contain the letter `a` from database `hbtn_0e_6_usa`.
* Notes:
  * Script takes 3 arguments:
    * `mysql username`
    * `mysql password`
    * `database name`
  * Uses the `SQLAlchemy` module
  * Connects to a MySQL server running on `localhost` at port `3306`
  * Results are sorted in ascending order by `states.id`
* Usage:
  ```
  $ ./9-model_state_filter_a.py root root hbtn_0e_6_usa
  1: California
  2: Arizona
  3: Texas
  5: Nevada
  $
  ```

##### [10-model_state_my_get.py](10-model_state_my_get.py)
Script to print the `State` object with the `name` passed as argument from the database `hbtn_0e_6_usa`.
* Notes:
  * Script takes 4 arguments:
    * `mysql username`
    * `mysql password`
    * `database name`
    * `state name to search`
  * Uses the `SQLAlchemy` module
  * Connects to a MySQL server running on `localhost` at port `3306`
  * Results are sorted in ascending order by `states.id`
  * If no state had the name searched for, `Not found` is displayed
* Usage:
  ```
  $ ./10-model_state_my_get.py root root hbtn_0e_6_usa Texas
  3
  $ ./10-model_state_my_get.py root root hbtn_0e_6_usa Illinois
  Not found
  $
  ```

##### [11-model_state_insert.py](11-model_state_insert.py)
Script to add the `State` object "Louisiana" to the database `hbtn_0e_6_usa`.
* Notes:
  * Script takes 3 arguments:
    * `mysql username`
    * `mysql password`
    * `database name`
  * Uses the `SQLAlchemy` module
  * Connects to a MySQL server running on `localhost` at port `3306`
  * The new state's `states.id` is printed after creation
* Usage:
  ```
  $ ./11-model_state_insert.py root root hbtn_0e_6_usa 
  6
  $
  ```
  * Use [7-model_state_fetch_all.py](7-model_state_fetch_all.py) to check that the state was added:
    ```
    $ ./7-model_state_fetch_all.py root root hbtn_0e_6_usa 
    1: California
    2: Arizona
    3: Texas
    4: New York
    5: Nevada
    6: Louisiana
    $ 
    ```

##### [12-model_state_update_id_2.py](12-model_state_update_id_2.py)
Script to update the name of a `State` object from the database `hbtn_0e_6_usa`.
* Notes:
  * `State` to be changed:
    * `id = 2`
    * Update name to `New Mexico`
  * Script takes 3 arguments:
    * `mysql username`
    * `mysql password`
    * `database name`
  * Uses the `SQLAlchemy` module
  * Connects to a MySQL server running on `localhost` at port `3306`
* Usage:
  ```
  $ ./12-model_state_update_id_2.py root root hbtn_0e_6_usa 
  ```
  * Use [7-model_state_fetch_all.py](7-model_state_fetch_all.py) to check that the state was updated:
    ```
    $ ./7-model_state_fetch_all.py root root hbtn_0e_6_usa 
    1: California
    2: New Mexico
    3: Texas
    4: New York
    5: Nevada
    6: Louisiana
    $
    ```

##### [13-model_state_delete_a.py](13-model_state_delete_a.py)
Script to delete all `State` objects with a name containing the letter `a` from the database `hbtn_0e_6_usa`.
* Notes:
  * Script takes 3 arguments:
    * `mysql username`
    * `mysql password`
    * `database name`
  * Uses the `SQLAlchemy` module
  * Connects to a MySQL server running on `localhost` at port `3306`
* Usage:
  ```
  $ ./13-model_state_delete_a.py root root hbtn_0e_6_usa
  ```
  * Use [7-model_state_fetch_all.py](7-model_state_fetch_all.py) to check that the states were deleted:
    ```
    $ ./7-model_state_fetch_all.py root root hbtn_0e_6_usa 
    2: New Mexico
    4: New York
    $
    ```

##### Task 14
* [model_city.py](model_city.py): Contains the class definition of a `City`
  * `City` class 
    * inherits from `Base` (inherited from model_state)
    * links to the MySQL table `cities`
    * Class attributes:
      * `id`: column of an auto-generated, unique integer, can't be null and is a primary key
      * `name`: column of a string of 128 characters and can't be null
      * `state_id`: column of an integer, can't be null and is a foreign key to `states.id`
  * Uses the `SQLAlchemy` module
* [14-model_city_fetch_by_state.py](14-model_city_fetch_by_state.py): Script to print all `City` objects from the database `hbtn_0e_6_usa`.
  * Notes:
    * Script takes 3 arguments:
      * `mysql username`
      * `mysql password`
      * `database name`
    * Uses the `MySQLdb` module
    * Connects to a MySQL server running on `localhost` at port `3306`
    * Results are sorted in ascending order by `cities.id`
    * Use [14-model_city_fetch_by_state.sql](14-model_city_fetch_by_state.sql) to create the database and table if they don't exist
  * Usage:
    ```
    $ cat 14-model_city_fetch_by_state.sql | mysql -uroot -p
    Enter password: 
    $ ./14-model_city_fetch_by_state.py root root hbtn_0e_14_usa
    California: (1) San Francisco
    California: (2) San Jose
    California: (3) Los Angeles
    California: (4) Fremont
    California: (5) Livermore
    Arizona: (6) Page
    Arizona: (7) Phoenix
    Texas: (8) Dallas
    Texas: (9) Houston
    Texas: (10) Austin
    New York: (11) New York
    Nevada: (12) Las Vegas
    Nevada: (13) Reno
    Nevada: (14) Henderson
    Nevada: (15) Carson City
    $
    ```


## Authors
Kristen Loyd        [Github](https://github.com/KRLoyd) |  [LinkedIn](https://www.linkedin.com/in/kristen-loyd-34984a92)

## License
Public Domain, no copyright protection
