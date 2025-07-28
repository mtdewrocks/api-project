from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from datetime import date
from typing import List
#changed import below
import crud, schemas
from database import SessionLocal

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
async def root():
    return {"message":"API health check successful"}

@app.get("/v0/players/", response_model=schemas.Hitters)
def read_player(savant_id:int=None,fg_id:int=None,baseball_reference_name:str=None, mlb_name:str=None,db: Session = Depends(get_db)):
    player = crud.get_player(db, savant_id=savant_id,baseball_reference_name=baseball_reference_name,fg_id=fg_id,mlb_name=mlb_name)
    if player is None:
        raise HTTPException(status_code=404, detail="Player not found")
    return player

@app.get("/v0/pitchers/", response_model=schemas.Pitchers)
def read_pitcher(savant_id:int=None,fg_id:int=None,baseball_reference_name:str=None, mlb_name:str=None,db: Session = Depends(get_db)):
    pitcher = crud.get_pitcher(db, savant_id=savant_id,baseball_reference_name=baseball_reference_name,fg_id=fg_id,mlb_name=mlb_name)
    if pitcher is None:
        raise HTTPException(status_code=404, detail="Player not found")
    return pitcher


@app.get("/v0/game_logs/", response_model=list[schemas.Logs])
def get_logs(name: str, date: str=None, tm: str=None, db: Session=Depends(get_db)):
    logs = crud.get_logs(db, name=name, date=date, tm=tm).all()
    return logs
    
@app.get("/v0/counts/", response_model=schemas.Counts)
def get_counts(db: Session=Depends(get_db)):
    counts = schemas.Counts(player_count = crud.get_player_counts(db))
    return counts
