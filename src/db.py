from dataclasses import dataclass
from datetime import datetime
from typing import Any

from sqlalchemy import Boolean, Column, DateTime, Integer, Text, create_engine
from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy.orm import scoped_session, sessionmaker


@dataclass
class DB:
    host: str
    user: str
    passwd: str
    db: str

    def __post_init__(self):
        # engine の設定
        self.engine = create_engine(
            f"mysql+mysqlconnector://{self.user}:{self.passwd}@{self.host}/{self.db}"
        )

        # session の作成
        self.db_session = scoped_session(
            sessionmaker(
                autocommit=False,
                autoflush=False,
                bind=self.engine,
            )
        )


db = DB(host="db", user="docker", passwd="docker", db="test_database")
Base = declarative_base()  # type: Any
Base.query = db.db_session.query_property()


def create_tables():
    Base.metadata.create_all(bind=db.engine)


class Timestamp:
    @declared_attr
    def created_at(cls):
        return Column(DateTime, default=datetime.now(), nullable=False)

    @declared_attr
    def updated_at(cls):
        return Column(
            DateTime, default=datetime.now(), onupdate=datetime.now(), nullable=False
        )


class Players(Timestamp):
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


class Teams(Base, Timestamp):
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
