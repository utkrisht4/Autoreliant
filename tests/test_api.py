from utils.api_client import get_users, create_user
from utils.logger import log_failure
import pytest
@pytest.fixture
def users_response():
    return get_users()

def test_get_users_status(users_response):
    assert users_response.status_code == 200

def test_get_users_data(users_response):
    data = users_response.json()
    assert isinstance(data, list)

def test_create_user():
    response = create_user("Utkrisht", "Engineer")
    data = response.json()

    assert response.status_code == 201
    assert data["name"] == "Utkrisht"
    assert data["job"] == "Engineer"

def test_get_users_invalid_endpoint():
    import requests
    response = requests.get("https://jsonplaceholder.typicode.com/invalid")
    assert response.status_code == 404

def test_user_object_structure():
    response = get_users()
    user = response.json()[0]

    assert "id" in user
    assert "name" in user
    assert "email" in user

def test_response_time():
    import time
    from config import TIMEOUT_THRESHOLD
    start = time.perf_counter()
    response = get_users()
    end = time.perf_counter()

    assert response.status_code == 200
    assert (end - start) < TIMEOUT_THRESHOLD  # Response should be under 2 seconds

import pytest
@pytest.mark.parametrize("user_id", [1, 2, 3, 4])
def test_multiple_users(user_id):
    import requests
    response = requests.get(f"https://jsonplaceholder.typicode.com/users/{user_id}")
    assert response.status_code == 200
