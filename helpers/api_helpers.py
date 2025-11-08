import requests

BASE_URL = "https://qa-scooter.praktikum-services.ru/api/v1"

COURIER_ENDPOINT = f"{BASE_URL}/courier"
COURIER_LOGIN_ENDPOINT = f"{BASE_URL}/courier/login"
ORDER_ENDPOINT = f"{BASE_URL}/orders"


class ApiClient:
    @staticmethod
    def create_courier(payload):
        return requests.post(COURIER_ENDPOINT, json=payload)

    @staticmethod
    def login_courier(payload):
        return requests.post(COURIER_LOGIN_ENDPOINT, json=payload)

    @staticmethod
    def delete_courier(courier_id):
        return requests.delete(f"{COURIER_ENDPOINT}/{courier_id}")

    @staticmethod
    def create_order(payload):
        return requests.post(ORDER_ENDPOINT, json=payload)

    @staticmethod
    def get_orders():
        return requests.get(ORDER_ENDPOINT)