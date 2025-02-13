import pytest
from app.routes import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_submit_data(client):
    response = client.post('/submitData', json={
        "name": "Эльбрус",
        "height": 5642,
        "location": "Кавказ",
        "user_id": 1
    })
    assert response.status_code == 201
    assert response.json == {"status": "success", "message": "Pass added successfully"}