from sqlalchemy import Column, ForeignKey, Integer, String, Float, Date
from sqlalchemy.orm import relationship

from database import Base

class Hitters(Base):
    __tablename__ = "hitters"

    mlb_name = Column(String)
    mlb_team = column(String)
    mlb_team_long = Column(String)
    bats = Column(String)
    fg_id = Column(Integer)
    fg_name = Column(String)
    fg_pos = Column(String)
    rotowire_name = 