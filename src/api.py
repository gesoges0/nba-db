from nba_api.stats.static import players, teams

from src.db import db
from src.tables import (
    ActivePlayers,
    # AllPlayers,
    # InactivePlayers,
    # PlayerGameLog,
    # TeamGameLog,
    Teams,
)


def initialize_teams():
    """initialize team table"""
    # try
    db.db_session.bulk_save_objects([Teams(**t) for t in teams.get_teams()])
    db.db_session.commit()


def initialize_active_players():
    db.db_session.bulk_save_objects(
        [ActivePlayers(**p) for p in players.get_active_players()]
    )
    db.db_session.commit()
