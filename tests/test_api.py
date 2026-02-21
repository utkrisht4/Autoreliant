from utils.api_client import get_users, create_user

def test_get_users_status():
    response = get_users()
    assert response.status_code == 200

def test_get_users_data():
    response = get_users()
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0

def test_create_user():
    response = create_user("Utkrisht", "Engineer")
    data = response.json()

    assert response.status_code == 201
    assert data["name"] == "Utkrisht"
    assert data["job"] == "Engineer"