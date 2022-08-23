import time
from typing import Any

from nba_api.stats import endpoints as ep
from nba_api.stats.static import players, teams

from src.db import ActivePlayers, AllPlayers, InactivePlayers, Teams, create_tables, db
from src.tables import PlayerGameLog


def sleep(seconds: int) -> None:
    time.sleep(seconds)


# def initialize(): にしてmainからオプションで実行できるようにする
def initialize(args):
    """
    create database
    initialize player, team table
    """
    # wait MySQL start-up
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

    initialize_stats()


def initialize_stats():
    """initialize stats tables"""

    # each player's stats by season
    # db.db_session.bulk_save_objects(
    #     [PlayerGameLog(**game_log_by_season_player[0]) for game_log_by_season_player in filter(lambda x: x is not [], map(lambda p: ep.playergamelog.PlayerGameLog(player_id=p["id"]).get_normalized_dict()["PlayerGameLog"], players.get_active_players()[:3]))]
    # )

    a = []
    for player_id in map(lambda p: p["id"], players.get_active_players()[:3]):
        player_game_log: list[dict[str, Any]] = ep.playergamelog.PlayerGameLog(
            player_id=player_id
        ).get_normalized_dict()["PlayerGameLog"]
        if not player_game_log:
            continue
        for player_game_log_dict in player_game_log:
            a.append(PlayerGameLog(**player_game_log_dict))
    if a:
        db.db_session.bulk_save_objects(a)
        db.db_session.commit()
