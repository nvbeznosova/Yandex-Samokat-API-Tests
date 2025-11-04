import pytest
import requests
from helpers.courier_helper import BASE_URL, register_new_courier

@pytest.fixture
def new_courier():
    response, payload = register_new_courier()
    assert response.status_code == 201, "Не удалось создать курьера"
    
    login_payload = {
        "login": payload["login"],
        "password": payload["password"]
    }
    login_response = requests.post(f"{BASE_URL}/courier/login", json=login_payload)
    courier_id = login_response.json().get("id")

    yield payload, courier_id

    if courier_id:
        requests.delete(f"{BASE_URL}/courier/{courier_id}")