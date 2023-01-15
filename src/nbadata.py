# nab-apiとやり取りをして, nba-apiで得られたデータを使いやすい形に加工し返す
# api.pyから呼ばれ, api.pyで返したデータがDBに保存される


from typing import Iterator, Union

from nba_api.stats.endpoints import playergamelog, teamgamelog
from nba_api.stats.static import players, teams

from src.utils import iterate_and_wait

GAMELOG = dict[str, Union[str, int, float]]


def get_player_game_log_dicts() -> Iterator[GAMELOG]:
    """current_season player's all game stats in this season"""
    # FIXME:
    #  season引数を取れるようにする
    #  seasonごとにactiveな選手一覧を作り, その選手に対して seasonで引く
    for i, p in enumerate(iterate_and_wait(players.get_active_players())):
        player_game_log: list[GAMELOG] = playergamelog.PlayerGameLog(
            player_id=p["id"]
        ).get_normalized_dict()["PlayerGameLog"]
        for player_game_log_dict in player_game_log:
            yield player_game_log_dict


def get_team_game_log_dicts() -> Iterator[GAMELOG]:
    # FIXME: season引数を取れるようにする
    for i, t in enumerate(iterate_and_wait(teams.get_teams())):
        team_game_log: list[GAMELOG] = teamgamelog.TeamGameLog(
            team_id=t["id"]
        ).get_normalized_dict()["TeamGameLog"]
        for team_game_log_dict in team_game_log:
            yield team_game_log_dict
