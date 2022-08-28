# nba-db
NBA stats DB api

### build
```sh
$ docker compose build
```

### run containers
```
$ docker compose up
```

### mysql 
another window
```sh
$ docker container exec -it mysql_host bash -c "mysql test_database -uroot -proot"
mysql> SELECT * FROM inactive_players LIMIT 3;
+----+-----------------+------------+------------+-----------+---------------------+---------------------+
| id | full_name       | first_name | last_name  | is_active | created_at          | updated_at          |
+----+-----------------+------------+------------+-----------+---------------------+---------------------+
|  2 | Byron Scott     | Byron      | Scott      |         0 | 2022-08-19 13:41:37 | 2022-08-19 13:41:37 |
|  3 | Grant Long      | Grant      | Long       |         0 | 2022-08-19 13:41:37 | 2022-08-19 13:41:37 |
|  7 | Dan Schayes     | Dan        | Schayes    |         0 | 2022-08-19 13:41:37 | 2022-08-19 13:41:37 |
+----+-----------------+------------+------------+-----------+---------------------+---------------------+
3 rows in set (0.00 sec)


mysql> SELECT * FROM player_game_log LIMIT 3;
+-----------+-----------+------------+--------------+-------------+------+------+------+------+--------+------+------+---------+------+------+--------+------+------+------+------+------+------+------+------+------+------------+-----------------+---------------------+---------------------+
| SEASON_ID | Player_ID | Game_ID    | GAME_DATE    | MATCHUP     | WL   | MIN  | FGM  | FGA  | FG_PCT | FG3M | FG3A | FG3_PCT | FTM  | FTA  | FT_PCT | OREB | DREB | REB  | AST  | STL  | BLK  | TOV  | PF   | PTS  | PLUS_MINUS | VIDEO_AVAILABLE | created_at          | updated_at          |
+-----------+-----------+------------+--------------+-------------+------+------+------+------+--------+------+------+---------+------+------+--------+------+------+------+------+------+------+------+------+------+------------+-----------------+---------------------+---------------------+
| 22021     |    203500 | 0022100007 | OCT 20, 2021 | MEM vs. CLE | W    |   32 |    4 |    7 |  0.571 |    0 |    0 |       0 |    0 |    0 |      0 |    6 |    8 |   14 |    3 |    1 |    1 |    2 |    0 |    8 |          1 |               1 | 2022-08-23 17:32:59 | 2022-08-23 17:32:59 |
| 22021     |    203500 | 0022100034 | OCT 23, 2021 | MEM @ LAC   | W    |   27 |    6 |    9 |  0.667 |    0 |    0 |       0 |    5 |    5 |      1 |    5 |    4 |    9 |    5 |    2 |    0 |    1 |    0 |   17 |         17 |               1 | 2022-08-23 17:32:59 | 2022-08-23 17:32:59 |
| 22021     |    203500 | 0022100040 | OCT 24, 2021 | MEM @ LAL   | L    |   34 |    7 |   11 |  0.636 |    0 |    0 |       0 |    0 |    0 |      0 |    8 |    8 |   16 |    6 |    0 |    0 |    4 |    5 |   14 |         15 |               1 | 2022-08-23 17:32:59 | 2022-08-23 17:32:59 |
+-----------+-----------+------------+--------------+-------------+------+------+------+------+--------+------+------+---------+------+------+--------+------+------+------+------+------+------+------+------+------+------------+-----------------+---------------------+---------------------+
3 rows in set (0.00 sec)

mysql> SELECT * FROM team_game_log LIMIT 3;
+------------+------------+--------------+-------------+------+------+------+-------+------+------+------+--------+------+------+---------+------+------+--------+------+------+------+------+------+------+------+------+------+---------------------+---------------------+
| Team_ID    | Game_ID    | GAME_DATE    | MATCHUP     | WL   | W    | L    | W_PCT | MIN  | FGM  | FGA  | FG_PCT | FG3M | FG3A | FG3_PCT | FTM  | FTA  | FT_PCT | OREB | DREB | REB  | AST  | STL  | BLK  | TOV  | PF   | PTS  | created_at          | updated_at          |
+------------+------------+--------------+-------------+------+------+------+-------+------+------+------+--------+------+------+---------+------+------+--------+------+------+------+------+------+------+------+------+------+---------------------+---------------------+
| 1610612737 | 0022100014 | OCT 21, 2021 | ATL vs. DAL | W    |    1 |    0 |     1 |  240 |   45 |   94 |  0.479 |   15 |   35 |   0.429 |    8 |    9 |  0.889 |    6 |   49 |   55 |   31 |    8 |    9 |   13 |   16 |  113 | 2022-08-27 11:40:01 | 2022-08-27 11:40:01 |
| 1610612737 | 0022100027 | OCT 23, 2021 | ATL @ CLE   | L    |    1 |    1 |   0.5 |  240 |   38 |   99 |  0.384 |   10 |   34 |   0.294 |    9 |   15 |    0.6 |   17 |   37 |   54 |   20 |    5 |    3 |    9 |   23 |   95 | 2022-08-27 11:40:01 | 2022-08-27 11:40:01 |
| 1610612737 | 0022100043 | OCT 25, 2021 | ATL vs. DET | W    |    2 |    1 | 0.667 |  240 |   46 |   90 |  0.511 |   12 |   32 |   0.375 |   18 |   21 |  0.857 |   10 |   39 |   49 |   24 |   11 |    3 |   13 |   19 |  122 | 2022-08-27 11:40:01 | 2022-08-27 11:40:01 |
+------------+------------+--------------+-------------+------+------+------+-------+------+------+------+--------+------+------+---------+------+------+--------+------+------+------+------+------+------+------+------+------+---------------------+---------------------+
3 rows in set (0.00 sec)

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
