# 0x0E. SQL - More queries

## Description
Scripts in this folder correspond to Holberton School tasks to continue working with MySQL.


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

##### [0-privileges.sql](0-privileges.sql)
Script to list all priviledges of the MySQL users `user_0d_1` and `user_0d_2` on your server.
* Usage: `cat 0-privileges.sql | mysql -hlocalhost -uroot -p`

##### [1-create_user.sql](1-create_user.sql)
Script to create the MySQL server user `user_0d_1` with all privileges and a password.
* Usage: `cat 1-create_user.sql | mysql -hlocalhost -uroot -p`

##### [2-create_read_user.sql](2-create_read_user.sql)
Script that creates the database `hbtn_0d_2` and the server user `user_0d_2` with a password and SELECT priviledge on the new database.
* Usage: `cat 2-create_read_user.sql | mysql -hlocalhost -uroot -p`

##### [3-force_name.sql](3-force_name.sql)
Script that creates the table `force_name` in the specifeid database of your MySQL server.
* Usage: `cat 3-force_name.sql | mysql -hlocalhost -uroot -p <database name>`

##### [4-never_empty.sql](4-never_empty.sql)
Script to create the table `id_not_null` in the specified database of your MySQL server.
* Usage: `cat 4-never_empty.sql | mysql -hlocalhost -uroot -p <database name>`

##### [5-unique_id.sql](5-unique_id.sql)
Script to create the table `unique_id` in the specified database of your MySQL server.
* Usage: `cat 5-unique_id.sql | mysql -hlocalhost -uroot -p <database name>`

##### [6-states.sql](6-states.sql)
Script to create the database `hbtn_0d_usa` and a table within it, `states`, in your MySQL server.
* Usage: `cat 6-states.sql | mysql -hlocalhost -uroot -p`

##### [7-cities.sql](7-cities.sql)
Script to create the database `hbtn_0d_usa` and a table within it, `cities`, in your MySQL server.
* Usage: `cat 7-cities.sql | mysql -hlocalhost -uroot -p`

##### [8-cities_of_california_subquery.sql](8-cities_of_california_subquery.sql)
Script that lists all the cities of California that can be found in the specified database in your MySQL server.
* Usage: `cat 8-cities_of_california_subquery.sql | mysql -hlocalhost -uroot -p <database name>`

##### [9-cities_by_state_join.sql](9-cities_by_state_join.sql)
Script that lists all cities containes in the specified database of your MySQL server.
* Usage: `cat 9-cities_by_state_join.sql | mysql -hlocalhost -uroot -p <database name>`

##### [10-genre_id_by_show.sql](10-genre_id_by_show.sql)
Script to list all shows contained in the database `hbtn_0d_tvshows` that have at least one genre linked.
* To create the database and populate with downloaded information:
  ```
  $ echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
  Enter password: 
  $ curl "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" -s | mysql -uroot -p hbtn_0d_tvshows
  ```
* Usage: `cat 10-genre_id_by_show.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows`

##### [11-genre_id_all_shows.sql](11-genre_id_all_shows.sql)
Script to list all shows contained in the specified database of your MySQL server.
* Usage: `cat 11-genre_id_all_shows.sql | mysql -hlocalhost -uroot -p <database name>`

##### [12-no_genre.sql](12-no_genre.sql)
Script to list all shows without a genre linked contained in the specified database of your MySQL server.
* Usage: `cat 12-no_genre.sql | mysql -hlocalhost -uroot -p <database name>`

##### [13-count_shows_by_genre.sql](13-count_shows_by_genre.sql)
Script to list all genres and the number of shows linked to each from the specified database of your MySQL server.
* Usage: `cat 13-count_shows_by_genre.sql | mysql -hlocalhost -uroot -p <database name>`

##### [14-my_genres.sql](14-my_genres.sql)
Script to list all genres of the show `Dexter` from the specified databaes of your MySQL server.
* Usage: `cat 14-my_genres.sql | mysql -hlocalhost -uroot -p <database name>`

##### [15-comedy_only.sql](15-comedy_only.sql)
Script that lists all Comedy shows in the specified database of your MySQL server.
* Usage: `cat 15-comedy_only.sql | mysql -hlocalhost -uroot -p <database name>`

##### [16-shows_by_genre.sql](16-shows_by_genre.sql)
Script to list all shows, and all genres linked to each show, from the specified database of your MySQL server.
* Usage: `cat 16-shows_by_genre.sql | mysql -hlocalhost -uroot -p <database name>`


## Authors
Kristen Loyd        [Github](https://github.com/KRLoyd) |  [LinkedIn](https://www.linkedin.com/in/kristen-loyd-34984a92)

## License
Public Domain, no copyright protection
