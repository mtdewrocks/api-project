from sqlalchemy.orm import Session
from sqlalchemy.orm import joinedload
from datetime import date

import models

def get_player(db: Session, savant_id:int):
    return db.query(models.Hitters).filter(models.Hitters.savant_id==savant_id).first()


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