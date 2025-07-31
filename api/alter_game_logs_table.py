import pandas as pd
import os
import logging

logging.basicConfig(filename="alter_table_log.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


# Load Excel data
current_directory = os.getcwd()
logger.info(current_directory)
print(current_directory)
if current_directory == "/workspaces/api-project/api":
    df = pd.read_excel("game_log.xlsx")
    logger.info("Succesffully read game logs file.")
else:
    df = pd.read_excel("api/game_log.xlsx")
    


from sqlalchemy.orm import declarative_base, Session
from sqlalchemy import create_engine, MetaData, Table, select, Column, Integer, String
if current_directory == "/workspaces/api-project/api":
    engine = create_engine("sqlite:///mlb_api.db")
    logger.info("Successfully created sql engine")
else:
    print('In here')
    engine = create_engine("sqlite:///api/mlb_api.db")
Base = declarative_base()

class Logs(Base):
    __tablename__ = 'game_logs'
    name = Column(String)
    age = Column(Integer)
    tm = Column(String)
    home_or_away = Column(String, nullable=True)
    opponent = Column(String)
    PA = Column(Integer)
    AB = Column(Integer)
    R = Column(Integer)
    H = Column(Integer)
    DOUBLES = Column(Integer)
    TRIPLES = Column(Integer)
    HR = Column(Integer)
    RBI = Column(Integer)
    BB = Column(Integer)
    IBB = Column(Integer)
    SO = Column(Integer)
    HBP = Column(Integer)
    SH = Column(Integer)
    SF = Column(Integer)
    GDP = Column(Integer)
    SB = Column(Integer)
    CS = Column(Integer)
    Hit_Flag = Column(Integer)
    Multi_Hit_Flag = Column(Integer)
    K_Flag = Column(Integer)
    Multi_K_Flag = Column(Integer)
    HR_Flag = Column(Integer)
    date = Column(String)
    date_player = Column(String, primary_key=True)

with Session(engine) as session:
    # Step 1: Get existing IDs in the table
    df_db = pd.DataFrame(
    session.execute(select(*Logs.__table__.columns)).all(),
    columns=[column.name for column in Logs.__table__.columns]
)

    logger.info("Successfully executed session.execute")
    logger.info(df_db.shape)
    # Merge on the 3 target columns to find matching rows
    merged = df.merge(df_db, on=["date_player"], how="left", indicator=True)

    # Keep only rows not present in SQL table
    df_filtered = merged[merged["_merge"] == "left_only"].drop(columns=["_merge"])
    print(df_filtered.shape)

    for _, row in df_filtered.iterrows():
        existing = session.get(Logs, row["date_player"])
        if existing:
           pass

            # You can update more if needed
        else:
        	# Checks what columns are allowed to be included and then adds only those columns
            allowed_keys = {column.name for column in Logs.__table__.columns}
            row_dict = {k: v for k, v in row.items() if k in allowed_keys}
            new_game_logs = Logs(**row_dict)

            session.add(new_game_logs)
            logger.info("Succesfully added new hitter")

    session.commit()
