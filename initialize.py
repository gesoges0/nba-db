import time
from typing import Any
from dataclasses import dataclass, field

import MySQLdb


def sleep(seconds: int) -> None:
    time.sleep(seconds)


@dataclass
class DB:
    host: str
    user: str
    passwd: str
    db: str

    def __post_init__(self):
       self.connection = MySQLdb.connect(
            host=self.host, user=self.user, passwd=self.passwd, db=self.db
        )

    def _execute(self, query: str):
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute(query)
            return cursor.fetchall()

if __name__ == "__main__":
    # MySQLの起動を5秒待つ
    sleep(10)

    # DBを初期化
    db: DB = DB(host="db", user="docker", passwd="docker", db="test_database")
    records = db._execute("SHOW CREATE DATABASE test_database;")
    for i, record in enumerate(records):
        print(i, record)
