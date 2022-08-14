import time
from dataclasses import dataclass, field
from typing import Any

import MySQLdb


def sleep(seconds: int) -> None:
    time.sleep(seconds)


@dataclass
class DatabaseManager:
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

    def create_table(self, table_name: str, columns: dict[str, str]):
        """create table"""
        columns_with_types = [
            f"{column_name} {data_type}" for column_name, data_type in columns.items()
        ]
        self._execute(
            f"""
            CREATE TABLE IF NOT EXISTS {table_name}
            ({', '.join(columns_with_types)});
            """
        )

    def add(self, table_name: str, data: dict[str, str]):
        """insert records"""
        placeholders = ", ".join("?" * len(data))
        column_names = ", ".join(data.keys())
        column_values = tuple(data.values())

        self._execute(
            f"""
            INSERT INTO {table_name}
            ({column_names})
            VALUES ({placeholders});
            """,
            column_values,
        )

    def select(self, table_name: str, criteria: dict[str, str] = None, order_by=None):
        """select"""
        criteria = criteria or {}
        query = f"SELECT * FROM {table_name}"

        if criteria:
            placeholders = [f"{column} = ?" for column in criteria.keys()]
            select_criteria = " AND ".join(placeholders)
            query += f" WHERE {select_criteria}"

        return self._execute(query, tuple(criteria.values()))


if __name__ == "__main__":
    # MySQLの起動を待つ
    sleep(10)

    # DBを初期化
    db_manager: DatabaseManager = DatabaseManager(
        host="db", user="docker", passwd="docker", db="test_database"
    )
    records = db_manager._execute("SHOW CREATE DATABASE test_database;")
    for i, record in enumerate(records):
        print(i, record)
