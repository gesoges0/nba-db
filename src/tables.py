from sqlalchemy import Boolean, Column, Float, Integer, String, Text

from src.db import Base


class PlayerGameLog(Base):
    """
    player's stats by each season
    """

    __tablename__ = "player_game_log"

    SEASON_ID = Column(String(16), primary_key=True, autoincrement=False)
    Player_ID = Column(Integer, primary_key=True, autoincrement=False)
    Game_ID = Column(String(16), primary_key=True, autoincrement=False)
    GAME_DATE = Column(String(16), primary_key=True, autoincrement=False)
    MATCHUP = Column(Text)
    WL = Column(Text)
    MIN = Column(Integer)
    FGM = Column(Integer)
    FGA = Column(Integer)
    FG_PCT = Column(Float)
    FG3M = Column(Integer)
    FG3A = Column(Integer)
    FG3_PCT = Column(Float)
    FTM = Column(Integer)
    FTA = Column(Integer)
    FT_PCT = Column(Float)
    OREB = Column(Integer)
    DREB = Column(Integer)
    REB = Column(Integer)
    AST = Column(Integer)
    STL = Column(Integer)
    BLK = Column(Integer)
    TOV = Column(Integer)
    PF = Column(Integer)
    PTS = Column(Integer)
    PLUS_MINUS = Column(Integer)
    VIDEO_AVAILABLE = Column(Boolean)
