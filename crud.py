from sqlalchemy.orm import Session
from sqlalchemy.orm import joinedload
from datetime import date

import models

def get_player(db: Session, player_id:int):
    return db.query(models.Hitters).filter(models.Hitters.player_id==player_id).first()

def get_logs(db: Session, player:str):
    return db.query(models.Logs).filter(models.Logs.name==player)

def get_player_counts(db: Session):
    query = db.query(models.Player)
    return query.count()