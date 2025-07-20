import pandas as pd
import os

# Load Excel data
current_directory = os.getcwd()
print(current_directory)
df = pd.read_excel("api/hitters.xlsx")
df = df.query("savant_id>0")


from sqlalchemy.orm import declarative_base, Session
from sqlalchemy import create_engine, MetaData, Table, select, Column, Integer, String
engine = create_engine("sqlite:///api/mlb_api.db")

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
    df_db = pd.DataFrame(
    session.execute(
        select(Hitters.savant_id, Hitters.mlb_name, Hitters.mlb_team)
    ).all(),
    columns=["savant_id", "mlb_name", "mlb_team"]
    )

    # Merge on the 3 target columns to find matching rows
    merged = df.merge(df_db, on=["savant_id", "mlb_name", "mlb_team"], how="left", indicator=True)

    # Keep only rows not present in SQL table
    df_filtered = merged[merged["_merge"] == "left_only"].drop(columns=["_merge"])


    for _, row in df_filtered.iterrows():
        existing = session.get(Hitters, row["savant_id"])
        if existing:
            #checks if there was a change in team and only writes if there was a change
            if existing.mlb_team != row['mlb_team']:
                existing.mlb_team = row['mlb_team']

            # You can update more if needed
        else:
        	# Checks what columns are allowed to be included and then adds only those columns
            allowed_keys = {column.name for column in Hitters.__table__.columns}
            row_dict = {k: v for k, v in row.items() if k in allowed_keys}
            new_hitter = Hitters(**row_dict)

            session.add(new_hitter)

    session.commit()
