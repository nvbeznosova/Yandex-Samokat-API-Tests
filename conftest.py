import pytest
from helpers.courier_helper import register_new_courier
from helpers.api_helpers import ApiClient


@pytest.fixture
def new_courier():
    response, payload = register_new_courier()
    login_payload = {
        "login": payload["login"],
        "password": payload["password"]
    }
    login_response = ApiClient.login_courier(login_payload)
    courier_id = login_response.json().get("id")

    yield payload, courier_id

    if courier_id:
        ApiClient.delete_courier(courier_id)