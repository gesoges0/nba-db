# nba-db
NBA stats DB api

### build
```sh
$ docker compose build; docker compose up
```

### mysql 
another window
```sh
$ docker container exec -it mysql_host bash -c "mysql -uroot -proot"
mysql> use test_database;
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


mysql> select * from player_game_log limit 10;
+-----------+-----------+------------+--------------+-------------+------+------+------+------+--------+------+------+---------+------+------+--------+------+------+------+------+------+------+------+------+------+------------+-----------------+---------------------+---------------------+
| SEASON_ID | Player_ID | Game_ID    | GAME_DATE    | MATCHUP     | WL   | MIN  | FGM  | FGA  | FG_PCT | FG3M | FG3A | FG3_PCT | FTM  | FTA  | FT_PCT | OREB | DREB | REB  | AST  | STL  | BLK  | TOV  | PF   | PTS  | PLUS_MINUS | VIDEO_AVAILABLE | created_at          | updated_at          |
+-----------+-----------+------------+--------------+-------------+------+------+------+------+--------+------+------+---------+------+------+--------+------+------+------+------+------+------+------+------+------+------------+-----------------+---------------------+---------------------+
| 22021     |    203500 | 0022100007 | OCT 20, 2021 | MEM vs. CLE | W    |   32 |    4 |    7 |  0.571 |    0 |    0 |       0 |    0 |    0 |      0 |    6 |    8 |   14 |    3 |    1 |    1 |    2 |    0 |    8 |          1 |               1 | 2022-08-23 17:32:59 | 2022-08-23 17:32:59 |
| 22021     |    203500 | 0022100034 | OCT 23, 2021 | MEM @ LAC   | W    |   27 |    6 |    9 |  0.667 |    0 |    0 |       0 |    5 |    5 |      1 |    5 |    4 |    9 |    5 |    2 |    0 |    1 |    0 |   17 |         17 |               1 | 2022-08-23 17:32:59 | 2022-08-23 17:32:59 |
| 22021     |    203500 | 0022100040 | OCT 24, 2021 | MEM @ LAL   | L    |   34 |    7 |   11 |  0.636 |    0 |    0 |       0 |    0 |    0 |      0 |    8 |    8 |   16 |    6 |    0 |    0 |    4 |    5 |   14 |         15 |               1 | 2022-08-23 17:32:59 | 2022-08-23 17:32:59 |
| 22021     |    203500 | 0022100063 | OCT 27, 2021 | MEM @ POR   | L    |   18 |    2 |    8 |   0.25 |    0 |    0 |       0 |    0 |    0 |      0 |    5 |    2 |    7 |    0 |    0 |    0 |    0 |    4 |    4 |        -20 |               1 | 2022-08-23 17:32:59 | 2022-08-23 17:32:59 |
| 22021     |    203500 | 0022100070 | OCT 28, 2021 | MEM @ GSW   | W    |   21 |    4 |    6 |  0.667 |    0 |    0 |       0 |    4 |    4 |      1 |    3 |    4 |    7 |    2 |    2 |    1 |    3 |    0 |   12 |         -5 |               1 | 2022-08-23 17:32:59 | 2022-08-23 17:32:59 |
| 22021     |    203500 | 0022100084 | OCT 30, 2021 | MEM vs. MIA | L    |   19 |    1 |    1 |      1 |    0 |    0 |       0 |    4 |    4 |      1 |    1 |    4 |    5 |    2 |    0 |    0 |    0 |    1 |    6 |        -12 |               1 | 2022-08-23 17:32:59 | 2022-08-23 17:32:59 |
| 22021     |    203500 | 0022100100 | NOV 01, 2021 | MEM vs. DEN | W    |   31 |    3 |    8 |  0.375 |    0 |    0 |       0 |    0 |    0 |      0 |    1 |    6 |    7 |    1 |    1 |    2 |    1 |    1 |    6 |          2 |               1 | 2022-08-23 17:32:59 | 2022-08-23 17:32:59 |
| 22021     |    203500 | 0022100114 | NOV 03, 2021 | MEM vs. DEN | W    |   30 |    3 |    5 |    0.6 |    0 |    0 |       0 |    2 |    2 |      1 |    1 |    7 |    8 |    4 |    1 |    0 |    1 |    2 |    8 |          9 |               1 | 2022-08-23 17:32:59 | 2022-08-23 17:32:59 |
| 22021     |    203500 | 0022100126 | NOV 05, 2021 | MEM @ WAS   | L    |   20 |    2 |    5 |    0.4 |    0 |    0 |       0 |    1 |    2 |    0.5 |    3 |    3 |    6 |    2 |    0 |    0 |    0 |    1 |    5 |        -20 |               1 | 2022-08-23 17:32:59 | 2022-08-23 17:32:59 |
| 22021     |    203500 | 0022100149 | NOV 08, 2021 | MEM vs. MIN | W    |   19 |    1 |    4 |   0.25 |    0 |    0 |       0 |    1 |    1 |      1 |    2 |    1 |    3 |    1 |    0 |    1 |    2 |    2 |    3 |        -17 |               1 | 2022-08-23 17:32:59 | 2022-08-23 17:32:59 |
+-----------+-----------+------------+--------------+-------------+------+------+------+------+--------+------+------+---------+------+------+--------+------+------+------+------+------+------+------+------+------+------------+-----------------+---------------------+---------------------+
10 rows in set (0.00 sec)
```

### exit
```sh
$ docker compose down
```

### trouble shooting
```sh
$ sudo service docker restart
```


### model auto creation
+ execute nba-api from python script like [this]() 
+ copy result and paste origin_table.txt like [this]()
+ execute create_table script and check [tables.py]()
