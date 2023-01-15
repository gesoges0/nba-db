import time

from src.api import (
    initialize_active_players,
    initialize_all_players,
    initialize_inactive_players,
    initialize_player_game_log,
    initialize_team_game_log,
    initialize_teams,
)
from src.db import create_tables


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

    # get today's date info
    # today: str =

    # db
    create_tables()

    # player tables
    initialize_active_players()
    initialize_inactive_players()
    initialize_all_players()

    # team tables
    initialize_teams()

    # game log by player
    initialize_player_game_log()

    # game log by team
    initialize_team_game_log()


# def initialize_stats():
#     """initialize stats tables"""
#     # current_season
#     _update_current_season_player_game_log_table()
#     _update_current_season_team_game_log_table()
#
#
# def _update_current_season_player_game_log_table() -> None:
#
#     # ------------------------------------------------------------------------------------------
#     # debug
#     with open("/app/src/debug/player.txt", "w") as f:
#         for i, player_game_log_dict in enumerate(_get_player_game_log_dicts()):
#             f.write(f"{player_game_log_dict}\n")
#     # ------------------------------------------------------------------------------------------
#
#     db.db_session.bulk_save_objects(
#         [
#             PlayerGameLog(**player_game_log_dict)
#             for player_game_log_dict in _get_player_game_log_dicts()
#         ]
#     )
#     db.db_session.commit()
#
#
# def _get_team_game_log_dicts() -> Iterator[GAMELOG]:
#     for i, t in enumerate(teams.get_teams()[:20]):
#         team_game_log: list[GAMELOG] = ep.teamgamelog.TeamGameLog(
#             team_id=t["id"]
#         ).get_normalized_dict()["TeamGameLog"]
#         print(i, t)
#         time.sleep(1)
#         for team_game_log_dict in team_game_log:
#             yield team_game_log_dict
#
#
# def _update_current_season_team_game_log_table() -> None:
#
#     # ------------------------------------------------------------------------------------------
#     # debug
#     with open("/app/src/debug/teams.txt", "w") as f:
#         for i, team_game_log_dict in enumerate(_get_team_game_log_dicts()):
#             f.write(f"{team_game_log_dict}\n")
#     # ------------------------------------------------------------------------------------------
#
#     db.db_session.bulk_save_objects(
#         [
#             TeamGameLog(**team_game_log_dict)
#             for team_game_log_dict in _get_team_game_log_dicts()
#         ]
#     )
#     db.db_session.commit()
#
#
# def get_current_season_all_game_logs() -> list[GAMELOG]:
#     """今シーズンの全ゲームログ"""
#     return [
#         player_game_log_dict
#         for player_game_log_dicts in (
#             ep.playergamelog.PlayerGameLog(
#                 player_id=p["id"],
#             ).get_normalized_dict()["PlayerGameLog"]
#             for p in players.get_active_players()
#         )
#         for player_game_log_dict in player_game_log_dicts
#     ]
