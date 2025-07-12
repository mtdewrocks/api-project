import pandas as pd

# Load Excel data
df = pd.read_excel("hitters.xlsx")

from sqlalchemy.orm import declarative_base, Session
from sqlalchemy import create_engine, MetaData, Table, select, Column, Integer, String
engine = create_engine("sqlite:///mlb_api.db")

Base = declarative_base()

class Hitters(Base):
    __tablename__ = "hitters"

    mlb_name = Column(String, nullable=False)
    mlb_team = Column(String, nullable=False)
    bats = Column(String, nullable=False)
    fg_id = Column(Integer, nullable=False)
    fg_name = Column(String, nullable=False)
    savant_name = Column(String, nullable=False)
    savant_id = Column(Integer, nullable=False, primary_key=True, index=True)
    baseball_reference_name = Column(String, nullable=False)
    props_name = Column(String, nullable=False)
    tm = Column(String, nullable=False)

with Session(engine) as session:
    # Step 1: Get existing IDs in the table
    existing_ids = set(session.scalars(select(Hitters.savant_id)).all())

    # Step 2: Filter DataFrame to only new rows
    new_rows = df[~df['savant_id'].isin(existing_ids)]

    # Step 3: Create ORM objects from new rows
    hitters_to_add = [
        Hitters(mlb_name=row['mlb_name'], mlb_team=row['mlb_team'], bats=row['bats'],
        fg_id=row['fg_id'], fg_name=row['fg_name'], savant_name=row['savant_name'],
        savant_id=row['savant_id'], baseball_reference_name=row['baseball_reference_name'],
        props_name=row["props_name"], tm=row['tm'])  # Add other columns if needed
        for _, row in new_rows.iterrows()
    ]


    # Step 4: Bulk insert
    session.add_all(hitters_to_add)
    session.commit()
