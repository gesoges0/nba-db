from dataclasses import dataclass
from datetime import datetime
from typing import cast

from sqlalchemy import Column, DateTime, create_engine  # Integer, Text, Boolean
from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.orm.decl_api import DeclarativeMeta


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


class Timestamp:
    @declared_attr
    def created_at(cls):
        return Column(DateTime, default=datetime.now(), nullable=False)

    @declared_attr
    def updated_at(cls):
        return Column(
            DateTime, default=datetime.now(), onupdate=datetime.now(), nullable=False
        )


def create_tables():
    Base.metadata.create_all(bind=db.engine)


db = DB(host="db", user="docker", passwd="docker", db="test_database")
Base: DeclarativeMeta = cast(DeclarativeMeta, declarative_base(cls=Timestamp))
Base.query = db.db_session.query_property()
