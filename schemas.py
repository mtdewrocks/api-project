from pydantic import BaseModel, ConfigDict
from datetime import date

class Hitters(BaseModel):
    model_config = ConfigDict(from_attributes = True)
    mlb_name : str 
    mlb_team : str
    bats : str
    fg_id : int
    savant_name : str
    savant_id : int
    baseball_reference_name : str
    props_name : str
    tm : str

class Logs(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    date_player : str
    name : str
    tm : str
    away_flag : str
    opp : str
    ab : int
    h : int
    hr : int
    so : int
    date : str

class Counts(BaseModel):
    player_count : int