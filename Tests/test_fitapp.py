import pytest
from app.app import app
@pytest.fixture
def client():
    app.testing = True
    return app.test_client()

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200

def test_health(client):
    response = client.get('/health')
    assert response.status_code == 200

def test_programs(client):
    response = client.get('/programs')
    assert response.status_code == 200

def test_calories(client):
    response = client.post('/calories', json={
        "weight_kg": 70,
        "program_code": "FL"
    })
    assert response.status_code == 200
