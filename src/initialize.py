import time

from nba_api.stats.static import players

from db import ActivePlayers, AllPlayers, InactivePlayers, create_tables, db


def sleep(seconds: int) -> None:
    time.sleep(seconds)


# def initialize(): にしてmainからオプションで実行できるようにする
def initialize():
    # MySQLの起動を待つ
    sleep(10)

    # db
    create_tables()

    # insert all players records
    db.db_session.bulk_save_objects(
        [
            AllPlayers(
                id=p["id"],
                full_name=p["full_name"],
                first_name=p["first_name"],
                last_name=p["last_name"],
                is_active=p["is_active"],
            )
            for p in players.get_players()
        ]
    )
    db.db_session.commit()

    # insert active players records
    db.db_session.bulk_save_objects(
        [
            ActivePlayers(
                id=p["id"],
                full_name=p["full_name"],
                first_name=p["first_name"],
                last_name=p["last_name"],
                is_active=p["is_active"],
            )
            for p in players.get_active_players()
        ]
    )
    db.db_session.commit()

    # insert inactive players records
    db.db_session.bulk_save_objects(
        [
            InactivePlayers(
                id=p["id"],
                full_name=p["full_name"],
                first_name=p["first_name"],
                last_name=p["last_name"],
                is_active=p["is_active"],
            )
            for p in players.get_inactive_players()
        ]
    )
    db.db_session.commit()


if __name__ == "__main__":
    initialize()
