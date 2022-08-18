import time
from db import create_tables
from nba_api.stats.static import players


def sleep(seconds: int) -> None:
    time.sleep(seconds)


# def initialize(): にしてmainからオプションで実行できるようにする
if __name__ == "__main__":
    # MySQLの起動を待つ
    sleep(10)

    # db
    create_tables()

    # DBを初期化
    # db_manager: DatabaseManager = DatabaseManager(
    #     host="db", user="docker", passwd="docker", db="test_database"
    # )
    # records = db_manager._execute("SHOW CREATE DATABASE test_database;")
    # for i, record in enumerate(records):
    #     print(i, record)

    # tableを作成
    # db_manager.create_table(
    #     table_name='all_players',
    #     columns={
    #         'id': 'INTEGER',
    #         'full_name': 'TINYTEXT',
    #         'first_name': 'TINYTEXT',
    #         'last_name': 'TINYTEXT',
    #         'is_active': 'BOOLEAN',
    #     }
    # )

    # データを取得してtableにデータを挿入
    # players = players.get_players()
    # player = players[0]
    # db_manager.add(
    #     table_name='all_players',
    #     data={
    #         'id': player['id'],
    #         'full_name': player['full_name'],
    #         'first_name': player['first_name'],
    #         'is_activate': player['is_active'],
    #     }
    # )
