# nba-db
NBA stats DB api

### build
```sh
docker-compose build
```

### insert
```sh
docker-compose up
```

### mysql 
another window
```sh
$ docker container exec -it mysql_host bash -c "mysql -uroot -proot"
# use test_database;
# select * from inactive_players limit 10;
mysql> select * from inactive_players limit 10;
+----+-----------------+------------+------------+-----------+---------------------+---------------------+
| id | full_name       | first_name | last_name  | is_active | created_at          | updated_at          |
+----+-----------------+------------+------------+-----------+---------------------+---------------------+
|  2 | Byron Scott     | Byron      | Scott      |         0 | 2022-08-19 13:41:37 | 2022-08-19 13:41:37 |
|  3 | Grant Long      | Grant      | Long       |         0 | 2022-08-19 13:41:37 | 2022-08-19 13:41:37 |
|  7 | Dan Schayes     | Dan        | Schayes    |         0 | 2022-08-19 13:41:37 | 2022-08-19 13:41:37 |
|  9 | Sedale Threatt  | Sedale     | Threatt    |         0 | 2022-08-19 13:41:37 | 2022-08-19 13:41:37 |
| 12 | Chris King      | Chris      | King       |         0 | 2022-08-19 13:41:37 | 2022-08-19 13:41:37 |
| 15 | Eric Piatkowski | Eric       | Piatkowski |         0 | 2022-08-19 13:41:37 | 2022-08-19 13:41:37 |
| 17 | Clyde Drexler   | Clyde      | Drexler    |         0 | 2022-08-19 13:41:37 | 2022-08-19 13:41:37 |
| 21 | Greg Anthony    | Greg       | Anthony    |         0 | 2022-08-19 13:41:37 | 2022-08-19 13:41:37 |
| 22 | Rik Smits       | Rik        | Smits      |         0 | 2022-08-19 13:41:37 | 2022-08-19 13:41:37 |
| 23 | Dennis Rodman   | Dennis     | Rodman     |         0 | 2022-08-19 13:41:37 | 2022-08-19 13:41:37 |
+----+-----------------+------------+------------+-----------+---------------------+---------------------+
10 rows in set (0.00 sec)
```

