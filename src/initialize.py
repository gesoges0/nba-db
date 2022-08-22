import time

from nba_api.stats.static import players, teams

from src.db import ActivePlayers, AllPlayers, InactivePlayers, Teams, create_tables, db


def sleep(seconds: int) -> None:
    time.sleep(seconds)


# def initialize(): にしてmainからオプションで実行できるようにする
def initialize(args):
    # MySQLの起動を待つ
    sleep(10)

    # db
    create_tables()

    # insert all players records
    db.db_session.bulk_save_objects([AllPlayers(**p) for p in players.get_players()])
    db.db_session.commit()

    # insert active players records
    db.db_session.bulk_save_objects(
        [ActivePlayers(**p) for p in players.get_active_players()]
    )
    db.db_session.commit()

    # insert inactive players records
    db.db_session.bulk_save_objects(
        [InactivePlayers(**p) for p in players.get_inactive_players()]
    )
    db.db_session.commit()

    # insert teams
    db.db_session.bulk_save_objects([Teams(**t) for t in teams.get_teams()])
    db.db_session.commit()
