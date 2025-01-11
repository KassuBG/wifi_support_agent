# Test the API endpoints

from fastapi.testclient import TestClient
from api.app import app

client = TestClient(app)

def test_support_endpoint():
    # Test a valid request
    response = client.post("/support", json={"message": "My internet is not working"})
    assert response.status_code == 200
    assert "response" in response.json()
    print(response.json())

    # Test a follow-up request
    response = client.post("/support", json={"message": "no"})
    assert response.status_code == 200
    assert "response" in response.json()
    print(response.json())

    # Test another follow-up request
    response = client.post("/support", json={"message": "no"})
    assert response.status_code == 200
    assert "response" in response.json()
    print(response.json())