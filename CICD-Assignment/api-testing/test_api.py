import requests

BASE_URL = "http://127.0.0.1:5000"

def test_hello():
    response = requests.get(f"{BASE_URL}/hello")
    assert response.status_code == 200

def test_add():
    response = requests.get(f"{BASE_URL}/add/3/5")
    data = response.json()
    assert data["result"] == 8