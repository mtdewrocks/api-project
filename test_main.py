from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code ==200
    assert response.json() == {"message":"API health check successful"}

def test_read_players():
    response = client.get("/v0/players/?savant_id=592450")
    assert response.status_code==200
    assert response.json().get("savant_id")==592450

def test_get_logs():
    response = client.get("/v0/performances/")
    assert response.status_code==200
    

def test_counts():
    response = client.get("/v0/counts")
    response_data = response.json()
    assert response.status_code==200
    assert response_data["player_count"]>0
