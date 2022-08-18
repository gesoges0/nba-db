from dataclasses import dataclass, field
from typing import Any

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Text, Boolean


@dataclass
class DB:
    host: str
    user: str
    passwd: str
    db: str

    def __post_init__(self):
        # engine の設定
        self.engine = create_engine(f"mysql+mysqlconnector://{self.user}:{self.passwd}@{self.host}/{self.db}")

        # session の作成
        self.db_session = scoped_session(
            sessionmaker(
                autocommit=False,
                autoflush=False,
                bind=self.engine,
            )
        )


db = DB(host="db", user="docker", passwd="docker", db="test_database")
Base = declarative_base()
Base.query = db.db_session.query_property()


def create_tables():
    Base.metadata.create_all(bind=db.engine)


class Players:
    id = Column(Integer, primary_key=True)
    full_name = Column(Text)
    first_name = Column(Text)
    last_name = Column(Text)
    is_active = Column(Boolean)


class AllPlayers(Base, Players):
    """
    +------------+------------+------+-----+---------+----------------+
    | Field      | Type       | Null | Key | Default | Extra          |
    +------------+------------+------+-----+---------+----------------+
    | id         | int(11)    | NO   | PRI | NULL    | auto_increment |
    | full_name  | text       | YES  |     | NULL    |                |
    | first_name | text       | YES  |     | NULL    |                |
    | last_name  | text       | YES  |     | NULL    |                |
    | is_active  | tinyint(1) | YES  |     | NULL    |                |
    +------------+------------+------+-----+---------+----------------+
    """
    __tablename__ = 'all_players'


class ActivePlayers(Base, Players):
    __tablename__ = "active_players"


class InactivePlayers(Base, Players):
    __tablename__ = "inactive_players"
