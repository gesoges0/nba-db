import time
from dataclasses import dataclass

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
        connection = MySQLdb.connect(
            host=self.host, user=self.user, passwd=self.passwd, db=self.db
        )

    def execute(self, query):
        self.cursor.execute(query)

    def fetchall(self):
        return self.cursor.fetchall()

    def close(self):
        self.connection.close()

    @property
    def cursor(self):
        return self.connection.cursor()


if __name__ == "__main__":
    # MySQLの起動を5秒待つ
    sleep(5)

    # DBを初期化
    db: DB = DB(host="db", user="docker", passwd="docker", db="test_database")
    db.execute("SHOW CREATE DATABASE test_database;")
    for i, row in enumerate(db.fetchall()):
        print(i, row)
    db.close()
