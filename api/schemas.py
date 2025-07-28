from pydantic import BaseModel, ConfigDict
from datetime import date
from typing import Optional

class Hitters(BaseModel):
    model_config = ConfigDict(from_attributes = True)
    mlb_name : str 
    mlb_team : str
    mlb_team_long : str
    bats : str
    fg_id : int
    savant_name : str
    savant_id : int
    baseball_reference_name : str
    props_name : str
    tm : str

class Pitchers(BaseModel):
    model_config = ConfigDict(from_attributes = True)
    mlb_name : str 
    mlb_team : str
    mlb_team_long : str
    throws : str
    fg_id : int
    rotowire_name : str
    savant_name : str
    savant_id : int
    baseball_reference_name : str
    props_name : str
    tm : str

class Logs(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    name: str
    age: int
    tm: str
    home_or_away: Optional[str]
    opponent: str
    PA: int
    AB: int
    R: int
    H: int
    DOUBLES: int
    TRIPLES: int
    HR: int
    RBI: int
    BB: int
    IBB: int
    SO: int
    HBP: int
    SH: int
    SF: int
    GDP: int
    SB: int
    CS: int
    Hit_Flag: int
    Multi_Hit_Flag: int
    K_Flag: int
    Multi_K_Flag: int
    HR_Flag: int
    date: str
    date_player: str

class Counts(BaseModel):
    player_count : int