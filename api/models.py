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
    __tablename__ = 'game_logs'
    name = Column(String)
    age = Column(Integer)
    tm = Column(String)
    home_or_away = Column(String, nullable=True)
    opponent = Column(String)
    PA = Column(Integer)
    AB = Column(Integer)
    R = Column(Integer)
    H = Column(Integer)
    DOUBLES = Column(Integer)
    TRIPLES = Column(Integer)
    HR = Column(Integer)
    RBI = Column(Integer)
    BB = Column(Integer)
    IBB = Column(Integer)
    SO = Column(Integer)
    HBP = Column(Integer)
    SH = Column(Integer)
    SF = Column(Integer)
    GDP = Column(Integer)
    SB = Column(Integer)
    CS = Column(Integer)
    Hit_Flag = Column(Integer)
    Multi_Hit_Flag = Column(Integer)
    K_Flag = Column(Integer)
    Multi_K_Flag = Column(Integer)
    HR_Flag = Column(Integer)
    date = Column(String)
    date_player = Column(String, primary_key=True)
    
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
