from nba_api.stats.static import players, teams

from src.db import db
from src.nbadata import get_player_game_log_dicts, get_team_game_log_dicts
from src.tables import (
    ActivePlayers,
    AllPlayers,
    InactivePlayers,
    PlayerGameLog,
    TeamGameLog,
    Teams,
)
from src.utils import display_func_name, bulk_insert


@display_func_name
def initialize_teams():
    """initialize team table"""
    # try
    bulk_insert([Teams(**t) for t in teams.get_teams()])


@display_func_name
def initialize_all_players():
    bulk_insert([AllPlayers(**p) for p in players.get_players()])


@display_func_name
def initialize_active_players():
    bulk_insert([ActivePlayers(**p) for p in players.get_active_players()])


@display_func_name
def initialize_inactive_players():
    bulk_insert([InactivePlayers(**p) for p in players.get_active_players()])


@display_func_name
def initialize_player_game_log():
    # FIXME:
    #  現状, active_playerのみ, current_seasonのみが対象
    #  season引数を取れるようにする
    bulk_insert(PlayerGameLog(**pgl) for pgl in get_player_game_log_dicts())


@display_func_name
def initialize_team_game_log():
    # FIXME:
    #  現状, active_playerのみ, current_seasonのみが対象
    #  season引数を取れるようにする
    bulk_insert(TeamGameLog(**tgl) for tgl in get_team_game_log_dicts())
