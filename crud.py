from sqlalchemy.orm import Session
from sqlalchemy.orm import joinedload
from datetime import date

import models

def get_player(db: Session, savant_id:int):
    return db.query(models.Hitters).filter(models.Hitters.savant_id==savant_id).first()

def get_logs(db: Session, name:str):
    if name:
        return db.query(models.Logs).filter(models.Logs.name==name)
    else:
        return db.query(models.Logs)


def get_player_counts(db: Session):
    query = db.query(models.Hitters)
    return query.count()