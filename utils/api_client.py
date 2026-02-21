import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def get_users():
    return requests.get(f"{BASE_URL}/users?page=2")

def create_user(name, job):
    return requests.post(
        f"{BASE_URL}/users",
        json={"name": name, "job": job}
    )