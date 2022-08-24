import time
from typing import Any, Union

import nba_api.stats.library.parameters
from nba_api.stats import endpoints as ep
from nba_api.stats.static import players, teams

from src.db import ActivePlayers, AllPlayers, InactivePlayers, Teams, create_tables, db
from src.tables import PlayerGameLog

GAMELOG = dict[str, Any]


def sleep(seconds: int) -> None:
    time.sleep(seconds)


all_players: list[dict[str, Union[int, str]]] = players.get_players()
active_players: list[dict[str, Union[int, str]]] = players.get_players()
inactive_players: list[dict[str, Union[int, str]]] = players.get_players()


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

    # 今シーズンの全ゲームログ

    # 副作用あり
    # a = []
    # for p in players.get_players()[:20]:
    #     player_game_log: list[dict[str, Any]] = ep.playergamelog.PlayerGameLog(
    #         player_id=p["id"]
    #     ).get_normalized_dict()["PlayerGameLog"]
    #     # if not player_game_log:
    #     #     continue
    #     for player_game_log_dict in player_game_log:
    #         a.append(PlayerGameLog(**player_game_log_dict))
    # if a:
    #     db.db_session.bulk_save_objects(a)
    #     db.db_session.commit()

    # 副作用なし
    db.db_session.bulk_save_objects(
        [
            PlayerGameLog(**player_game_log_dict)
            for player_game_log_dicts in (
                ep.playergamelog.PlayerGameLog(player_id=p["id"]).get_normalized_dict()[
                    "PlayerGameLog"
                ]
                for p in active_players[10:20]
            )
            for player_game_log_dict in player_game_log_dicts
        ]
    )
    db.db_session.commit()


def get_all_season_all_game_logs(season_id: str) -> list[GAMELOG]:
    return inactive_players


def get_current_season_all_game_logs() -> list[GAMELOG]:
    """今シーズンの全ゲームログ"""
    return [
        player_game_log_dict
        for player_game_log_dicts in (
            ep.playergamelog.PlayerGameLog(
                player_id=p["id"],
            ).get_normalized_dict()["PlayerGameLog"]
            for p in active_players
        )
        for player_game_log_dict in player_game_log_dicts
    ]
