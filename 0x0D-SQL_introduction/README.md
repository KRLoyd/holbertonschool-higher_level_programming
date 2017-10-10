# Project Name

## Description
Scripts in this folder correspond to Holberton School tasks to begin working with MySQL.


### Project Notes
#### Environment
These SQL queries have been tested on Ubuntu 14.04.5 LTS.
Tests and development are done in VirtualBox on Ubuntu via Vagrant(1.8.1) using MySQL 5.7.

To install MySQL 5.7:
```
$ echo 'deb http://repo.mysql.com/apt/ubuntu/ trusty mysql-5.7' | sudo tee -a /etc/apt/sources.list
$ sudo apt-get update
$ sudo apt-get install mysql-server-5.7
...
$ mysql --version
mysql  Ver 14.14 Distrib 5.7.8-rc, for Linux (x86_64) using  EditLine wrapper
$
```


## Files

##### [0-list_databases.sql](0-list_databases.sql)
Script that lists all databases of your MySQL server.
* Usage: `$ cat 0-list_databases.sql | mysql -hlocalhost -uroot -p`

##### [1-create_database_if_missing.sql](1-create_database_if_missing.sql)
Script that creates the database `hbtn_0c_0` in your MySQL server.
* Usage: `$ cat 1-create_database_if_missing.sql | mysql -hlocalhost -uroot -p`

##### [2-remove_database.sql](2-remove_database.sql)
Script to delete the database `hbtn_0c_0` in your MySQL server.
* Usage: `$ cat 0-list_databases.sql | mysql -hlocalhost -uroot -p`

##### [3-list_tables.sql](3-list_tables.sql)
Script to list all the tables of a database in your MySQL server.
* Usage: `cat 3-list_tables.sql | mysql -hlocalhost -uroot -p <database name>`

##### [4-first_table.sql](4-first_table.sql)
Script that creates a table called `first_table` in the specified database in your MySQL server.
* Usage: `cat 4-first_table.sql | mysql -hlocalhost -uroot -p <database name>`

##### [5-full_table.sql](5-full_table.sql)
Script that prints the full description of the table `first_table` in the specified database of your MySQL server.
* Usage: `cat 5-full_table.sql | mysql -hlocalhost -uroot -p <database name>`

##### [6-list_values.sql](6-list_values.sql)
Script that lists all rows of the table `first_table` from the specified database in your MySQL server.
* Usage: `cat 6-list_values.sql | mysql -hlocalhost -uroot -p <database name>`

##### [7-insert_value.sql](7-insert_value.sql)
Script to insert a new row in the table `first_table` in the specified database in yout MySQL server.
* Usage: `cat 7-insert_value.sql | mysql -hlocalhost -uroot -p <database name>`

##### [8-count_89.sql](8-count_89.sql)
Script to display the number of records with `id = 89` in the table `first_table` of the specified database in your MySQL server.
* Usage: `cat 8-count_89.sql | mysql -hlocalhost -uroot -p <database name>`

##### [9-full_creation.sql](9-full_creation.sql)
Script that creates a table `second_table` in the specified database in your MySQL server and adds multiple rows in the table.
* Usage: `cat 9-full_creation.sql | mysql -hlocalhost -uroot -p <database name>`

##### [10-top_score.sql](10-top_score.sql)
Script to list all records of the table `second_table` of the specified database in your MySQL server.
* Usage: `cat 10-top_score.sql | mysql -hlocalhost -uroot -p <database name>`

##### [11-best_score.sql](11-best_score.sql)
Script that lists all records in the table `second_table` with a `score >= 10` from the specified database in your MySQL server.
* Usage: `$ cat 11-best_score.sql | mysql -hlocalhost -uroot -p <database name>`

##### [12-no_cheating.sql](12-no_cheating.sql)
Script that updates the score of Bob to `10` in table `second_table` of the specified database of your MySQL server.
* Usage: `cat 12-no_cheating.sql | mysql -hlocalhost -uroot -p <database name>`

##### [13-change_class.sql](13-change_class.sql)
Script that removes all records with a `score <= 5` in the table `second_table` of the specified database of your MySQL server.
* Usage: `cat 13-change_class.sql | mysql -hlocalhost -uroot -p <database name>`

##### [14-average.sql](14-average.sql)
Script that computes the score average of all records in the table `second_table` of the specified database of your MySQL server.
* Usage: `cat 14-average.sql | mysql -hlocalhost -uroot -p <database name>`

##### [15-groups.sql](15-groups.sql)
Script that lists the number of records with the same score in the table `second_table` of the specified database in your MySQL server.
* Usage: `cat 15-groups.sql | mysql -hlocalhost -uroot -p <database name>`

##### [16-no_link.sql](16-no_link.sql)
Script that lists all records of the table `second_table` of the specified database in your MySQL server.
* Note: Rows without a `name` value are not displayed
* Usage: `cat 16-no_link.sql | mysql -hlocalhost -uroot -p <database name>`


## Authors
Kristen Loyd        [Github](https://github.com/KRLoyd) |  [LinkedIn](https://www.linkedin.com/in/kristen-loyd-34984a92)

## License
Public Domain, no copyright protection
