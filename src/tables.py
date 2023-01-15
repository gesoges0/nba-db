from sqlalchemy import Boolean, Column, Float, Integer, String, Text

from src.db import Base


class Players:
    """
    +------------+------------+------+-----+---------+-------+
    | Field      | Type       | Null | Key | Default | Extra |
    +------------+------------+------+-----+---------+-------+
    | id         | int(11)    | NO   | PRI | NULL    |       |
    | full_name  | text       | YES  |     | NULL    |       |
    | first_name | text       | YES  |     | NULL    |       |
    | last_name  | text       | YES  |     | NULL    |       |
    | is_active  | tinyint(1) | YES  |     | NULL    |       |
    | created_at | datetime   | NO   |     | NULL    |       |
    | updated_at | datetime   | NO   |     | NULL    |       |
    +------------+------------+------+-----+---------+-------+
    """

    id = Column(Integer, primary_key=True, autoincrement=False)
    full_name = Column(Text)
    first_name = Column(Text)
    last_name = Column(Text)
    is_active = Column(Boolean)


class AllPlayers(Base, Players):
    __tablename__ = "all_players"


class ActivePlayers(Base, Players):
    __tablename__ = "active_players"


class InactivePlayers(Base, Players):
    __tablename__ = "inactive_players"


class Teams(Base):
    """
    +--------------+----------+------+-----+---------+-------+
    | Field        | Type     | Null | Key | Default | Extra |
    +--------------+----------+------+-----+---------+-------+
    | id           | int(11)  | NO   | PRI | NULL    |       |
    | full_name    | text     | YES  |     | NULL    |       |
    | abbreviation | text     | YES  |     | NULL    |       |
    | nickname     | text     | YES  |     | NULL    |       |
    | city         | text     | YES  |     | NULL    |       |
    | state        | text     | YES  |     | NULL    |       |
    | year_founded | text     | YES  |     | NULL    |       |
    | created_at   | datetime | NO   |     | NULL    |       |
    | updated_at   | datetime | NO   |     | NULL    |       |
    +--------------+----------+------+-----+---------+-------+
    """

    __tablename__ = "teams"
    id = Column(Integer, primary_key=True, autoincrement=False)
    full_name = Column(Text)
    abbreviation = Column(Text)
    nickname = Column(Text)
    city = Column(Text)
    state = Column(Text)
    year_founded = Column(Text)


class PlayerGameLog(Base):
    """
    +-----------------+-------------+------+-----+---------+-------+
    | Field           | Type        | Null | Key | Default | Extra |
    +-----------------+-------------+------+-----+---------+-------+
    | SEASON_ID       | varchar(16) | NO   | PRI | NULL    |       |
    | Player_ID       | int         | NO   | PRI | NULL    |       |
    | Game_ID         | varchar(16) | NO   | PRI | NULL    |       |
    | GAME_DATE       | text        | YES  |     | NULL    |       |
    | MATCHUP         | text        | YES  |     | NULL    |       |
    | WL              | text        | YES  |     | NULL    |       |
    | MIN             | int         | YES  |     | NULL    |       |
    | FGM             | int         | YES  |     | NULL    |       |
    | FGA             | int         | YES  |     | NULL    |       |
    | FG_PCT          | float       | YES  |     | NULL    |       |
    | FG3M            | int         | YES  |     | NULL    |       |
    | FG3A            | int         | YES  |     | NULL    |       |
    | FG3_PCT         | float       | YES  |     | NULL    |       |
    | FTM             | int         | YES  |     | NULL    |       |
    | FTA             | int         | YES  |     | NULL    |       |
    | FT_PCT          | float       | YES  |     | NULL    |       |
    | OREB            | int         | YES  |     | NULL    |       |
    | DREB            | int         | YES  |     | NULL    |       |
    | REB             | int         | YES  |     | NULL    |       |
    | AST             | int         | YES  |     | NULL    |       |
    | STL             | int         | YES  |     | NULL    |       |
    | BLK             | int         | YES  |     | NULL    |       |
    | TOV             | int         | YES  |     | NULL    |       |
    | PF              | int         | YES  |     | NULL    |       |
    | PTS             | int         | YES  |     | NULL    |       |
    | PLUS_MINUS      | int         | YES  |     | NULL    |       |
    | VIDEO_AVAILABLE | tinyint(1)  | YES  |     | NULL    |       |
    | created_at      | datetime    | NO   |     | NULL    |       |
    | updated_at      | datetime    | NO   |     | NULL    |       |
    +-----------------+-------------+------+-----+---------+-------+
    """

    __tablename__ = "player_game_log"

    SEASON_ID = Column(String(16), primary_key=True, autoincrement=False)
    Player_ID = Column(Integer, primary_key=True, autoincrement=False)
    Game_ID = Column(String(16), primary_key=True, autoincrement=False)
    GAME_DATE = Column(Text)
    MATCHUP = Column(Text)
    WL = Column(Text)
    MIN = Column(Integer)
    FGM = Column(Integer)
    FGA = Column(Integer)
    FG_PCT = Column(Float)
    FG3M = Column(Integer)
    FG3A = Column(Integer)
    FG3_PCT = Column(Float)
    FTM = Column(Integer)
    FTA = Column(Integer)
    FT_PCT = Column(Float)
    OREB = Column(Integer)
    DREB = Column(Integer)
    REB = Column(Integer)
    AST = Column(Integer)
    STL = Column(Integer)
    BLK = Column(Integer)
    TOV = Column(Integer)
    PF = Column(Integer)
    PTS = Column(Integer)
    PLUS_MINUS = Column(Integer)
    VIDEO_AVAILABLE = Column(Boolean)


class TeamGameLog(Base):
    __tablename__ = "team_game_log"

    Team_ID = Column(Integer, primary_key=True, autoincrement=False)
    Game_ID = Column(String(16), primary_key=True, autoincrement=False)
    GAME_DATE = Column(Text)
    MATCHUP = Column(Text)
    WL = Column(Text)
    W = Column(Integer)
    L = Column(Integer)
    W_PCT = Column(Float)
    MIN = Column(Integer)
    FGM = Column(Integer)
    FGA = Column(Integer)
    FG_PCT = Column(Float)
    FG3M = Column(Integer)
    FG3A = Column(Integer)
    FG3_PCT = Column(Float)
    FTM = Column(Integer)
    FTA = Column(Integer)
    FT_PCT = Column(Float)
    OREB = Column(Integer)
    DREB = Column(Integer)
    REB = Column(Integer)
    AST = Column(Integer)
    STL = Column(Integer)
    BLK = Column(Integer)
    TOV = Column(Integer)
    PF = Column(Integer)
    PTS = Column(Integer)
