import pytest
from datetime import date
import crud
from database import SessionLocal

@pytest.fixture(scope="function")
def db_session():
    """This starts a database session and closes it when done."""
    session = SessionLocal()
    yield session
    session.close()

def test_get_player(db_session):
    """Tests that you can return Aaron Judge"""
    player = crud.get_player(db_session, savant_id=592450)
    print(response.json())
    #assert player.savant_id==592450

def test_get_logs(db_session):
    """Tests that you can get the game logs for Aaron Judge"""
    performances = crud.get_logs(db_session, name="Aaron Judge")
    assert performances.count()==49

def test_get_player_counts(db_session):
    player_count = crud.get_player_counts(db_session)
    assert player_count!=0