import pandas as pd
import os

# Load Excel data
current_directory = os.getcwd()
print(current_directory)
if current_directory == "/workspaces/api-project/api":
    df = pd.read_excel("pitchers.xlsx")
else:
    df = pd.read_excel("api/pitchers.xlsx")
    df = df.query("savant_id>0")


from sqlalchemy.orm import declarative_base, Session
from sqlalchemy import create_engine, MetaData, Table, select, Column, Integer, String
if current_directory == "/workspaces/api-project/api":
    engine = create_engine("sqlite:///mlb_api.db")
else:
    engine = create_engine("sqlite:///api/mlb_api.db")
Base = declarative_base()

class Pitchers(Base):
    __tablename__ = "pitchers"

    mlb_name = Column(String, nullable=False)
    mlb_team = Column(String, nullable=False)
    mlb_team_long = Column(String, nullable=False)
    throws = Column(String, nullable=False)
    fg_id = Column(Integer, nullable=False)
    fg_name = Column(String, nullable=False)
    rotowire_name = Column(String, nullable=False)
    savant_name = Column(String, nullable=False)
    savant_id = Column(Integer, nullable=False, primary_key=True, index=True)
    baseball_reference_name = Column(String, nullable=False)
    props_name = Column(String, nullable=False)
    tm = Column(String, nullable=False)

with Session(engine) as session:
    # Step 1: Get existing IDs in the table
    df_db = pd.DataFrame(
    session.execute(
        select(Pitchers.savant_id, Pitchers.mlb_name, Pitchers.mlb_team, Pitchers.mlb_team_long)
    ).all(),
    columns=["savant_id", "mlb_name", "mlb_team","mlb_team_long"]
    )

    # Merge on the 3 target columns to find matching rows
    merged = df.merge(df_db, on=["savant_id", "mlb_name", "mlb_team","mlb_team_long"], how="left", indicator=True)

    # Keep only rows not present in SQL table
    df_filtered = merged[merged["_merge"] == "left_only"].drop(columns=["_merge"])


    for _, row in df_filtered.iterrows():
        existing = session.get(Pitchers, row["savant_id"])
        if existing:
            #checks if there was a change in team and only writes if there was a change
            if existing.mlb_team != row['mlb_team']:
                existing.mlb_team = row['mlb_team']

            if existing.mlb_team_long != row['mlb_team_long']:
                existing.mlb_team_long = row['mlb_team_long']
            if existing.tm != row['tm']:
                existing.tm = row['tm']

            # You can update more if needed
        else:
        	# Checks what columns are allowed to be included and then adds only those columns
            allowed_keys = {column.name for column in Pitchers.__table__.columns}
            row_dict = {k: v for k, v in row.items() if k in allowed_keys}
            new_pitcher = Pitchers(**row_dict)

            session.add(new_pitcher)

    session.commit()
