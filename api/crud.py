from sqlalchemy.orm import Session
from sqlalchemy.orm import joinedload
from datetime import date

#Changed line below
import models

def get_player(db: Session, savant_id:int=None, mlb_name:str=None,fg_id:int=None,baseball_reference_name:str=None):
    query = db.query(models.Hitters)
    if savant_id:
        query = query.filter(models.Hitters.savant_id==savant_id)
    if mlb_name:
        query = query.filter(models.Hitters.mlb_name==mlb_name)
    if fg_id:
        query = query.filter(models.Hitters.fg_id==fg_id)
    if baseball_reference_name:
        query = query.filter(models.Hitters.baseball_reference_name==baseball_reference_name)
    return query.first()

def get_pitcher(db: Session, savant_id:int=None, mlb_name:str=None,fg_id:int=None,baseball_reference_name:str=None):
    query = db.query(models.Pitchers)
    if savant_id:
        query = query.filter(models.Pitchers.savant_id==savant_id)
    if mlb_name:
        query = query.filter(models.Pitchers.mlb_name==mlb_name)
    if fg_id:
        query = query.filter(models.Pitchers.fg_id==fg_id)
    if baseball_reference_name:
        query = query.filter(models.Pitchers.baseball_reference_name==baseball_reference_name)
    return query.first()


def get_logs(db: Session, name:str, date:str=None, tm:str=None):
    query = db.query(models.Logs)
    if name:
        query = query.filter(models.Logs.name==name)
    if date:
        query = query.filter(models.Logs.date==date)
    if tm:
        query = query.filter(models.Logs.tm==tm)
    return query


def get_player_counts(db: Session):
    query = db.query(models.Hitters)
    return query.count()
