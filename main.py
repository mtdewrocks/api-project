from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from datetime import date

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
def read_player(savant_id:int, db: Session = Depends(get_db)):
    player = crud.get_player(db, savant_id=savant_id)
    if player is None:
        raise HTTPException(status_code=404, detail="Player not found")
    return player

@app.get("/v0/performances/", response_model=schemas.Logs)
def get_logs(player: str, db: Session=Depends(get_db)):
    logs = crud.get_logs(db, name=player)
    if logs is None:
        raise HTTPException(status_code=404, detail="Player game logs not found")
    return 
    
@app.get("/v0/counts/", response_model=schemas.Counts)
def get_counts(db: Session=Depends(get_db)):
    counts = schemas.Counts(player_count = crud.get_player_counts(db))
    return counts