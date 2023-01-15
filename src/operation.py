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
