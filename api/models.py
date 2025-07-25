from sqlalchemy import Column, ForeignKey, Integer, String, Float, Date
from sqlalchemy.orm import relationship
from typing import Optional

#Changed line below
from database import Base

class Hitters(Base):
    __tablename__ = "hitters"

    mlb_name = Column(String, nullable=False)
    mlb_team = Column(String, nullable=False)
    mlb_team_long = Column(String, nullable=False)
    bats = Column(String, nullable=False)
    fg_id = Column(Integer, nullable=False)
    fg_name = Column(String, nullable=False)
    savant_name = Column(String, nullable=False)
    savant_id = Column(Integer, nullable=False, primary_key=True, index=True)
    baseball_reference_name = Column(String, nullable=False)
    props_name = Column(String, nullable=False)
    tm = Column(String, nullable=False)

    #game_logs = relationship("Logs", back_populates="hitters")


class PitcherSeasonStats(Base):
    __tablename__ = "pitcher_season_stats"

    savant_id = Column(Integer, nullable=False, primary_key=True, index=True)
    name = Column(String, nullable=False)
    tm = Column(String, nullable=False)
    age = Column(Integer)
    games = Column(Integer, nullable=False)
    

class Logs(Base):
    __tablename__ = "game_logs"
    
    date_player = Column(String, nullable=False, primary_key=True, index=True)
    name = Column(String, nullable=False)
    tm = Column(String, nullable=False)
    away_flag = Column(String)
    opp = Column(String)
    ab = Column(Integer, nullable=False)
    h = Column(Integer, nullable=False)
    hr = Column(Integer, nullable=False)
    so = Column(Integer, nullable=False)
    date = Column(String, nullable=False)
    #player_name = Column(String, ForeignKey("hitters.baseball_reference_name"))
    
class Pitchers(Base):
    __tablename__ = "pitchers"

    mlb_name = Column(String, nullable=False)
    mlb_team = Column(String, nullable=False)
    mlb_team_long = Column(String, nullable=False)
    throws = Column(String, nullable=False)
    fg_id = Column(Integer, nullable=False)
    fg_name = Column(String, nullable=False)
    rotowire_name = Column(String, nullable=False)
    savant_name = Column(String, nullable=False)
    savant_id = Column(Integer, nullable=False, primary_key=True, index=True)
    baseball_reference_name = Column(String, nullable=False)
    props_name = Column(String, nullable=False)
    tm = Column(String, nullable=False)
