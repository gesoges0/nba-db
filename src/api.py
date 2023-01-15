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
from src.utils import display_func_name


@display_func_name
def initialize_teams():
    """initialize team table"""
    # try
    db.db_session.bulk_save_objects([Teams(**t) for t in teams.get_teams()])
    db.db_session.commit()


@display_func_name
def initialize_all_players():
    db.db_session.bulk_save_objects([AllPlayers(**p) for p in players.get_players()])
    db.db_session.commit()


@display_func_name
def initialize_active_players():
    db.db_session.bulk_save_objects(
        [ActivePlayers(**p) for p in players.get_active_players()]
    )
    db.db_session.commit()


@display_func_name
def initialize_inactive_players():
    db.db_session.bulk_save_objects(
        [InactivePlayers(**p) for p in players.get_active_players()]
    )
    db.db_session.commit()


@display_func_name
def initialize_player_game_log():
    # FIXME:
    #  現状, active_playerのみ, current_seasonのみが対象
    #  season引数を取れるようにする
    db.db_session.bulk_save_objects(
        PlayerGameLog(**pgl) for pgl in get_player_game_log_dicts()
    )
    db.db_session.commit()


@display_func_name
def initialize_team_game_log():
    # FIXME:
    #  現状, active_playerのみ, current_seasonのみが対象
    #  season引数を取れるようにする
    db.db_session.bulk_save_objects(
        TeamGameLog(**tgl) for tgl in get_team_game_log_dicts()
    )
    db.db_session.commit()
