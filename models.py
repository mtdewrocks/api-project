from sqlalchemy import Column, ForeignKey, Integer, String, Float, Date
from sqlalchemy.orm import relationship

from database import Base

class Hitters(Base):
    __tablename__ = "hitters"

    mlb_name = Column(String, nullable=False)
    mlb_team = column(String, nullable=False)
    bats = Column(String, nullable=False)
    fg_id = Column(Integer, nullable=False)
    fg_name = Column(String, nullable=False)
    savant_name = Column(String, nullable=False)
    savant_id = Column(Integer, nullable=False, primary_key=True, index=True)
    baseball_reference_name = Column(String, nullable=False)
    props_name = Column(String, nullable=False)
    tm = Column(String, nullable=False)


class Logs(Base):
    __tablename__ = "game_logs"

    name = Column(String, nullable=False)
    tm = Column(String, nullable=False)
    away_flag = Column(String)
    mlb_team = column(String, nullable=False)
    opp = Column(String)
    ab = Column(Integer, nullable=False)
    h = Column(Integer, nullable=False)
    hr = Column(Integer, nullable=False)
    so = Column(Integer, nullable=False)
    date = Column(Date, nullable=False)
    player_name = Column(String, ForeignKey("hitters.baseball_reference_name"))
    