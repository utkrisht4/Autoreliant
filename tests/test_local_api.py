import requests

BASE_URL = "http://127.0.0.1:8000"

def test_health():
    r = requests.get(BASE_URL + "/")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"

def test_get_user():
    r = requests.get(BASE_URL + "/users/1")
    assert r.status_code == 200
    assert r.json()["id"] == 1

def test_invalid_user():
    r = requests.get(BASE_URL + "/users/0")
    assert r.status_code == 400

def test_create_user():
    r = requests.post(BASE_URL + "/users", json={"name": "Utkrisht"})
    assert r.status_code == 200