import requests
from helpers.endpoints import Endpoints


class ApiClient:
    @staticmethod
    def create_courier(payload):
        return requests.post(Endpoints.COURIER, json=payload)

    @staticmethod
    def login_courier(payload):
        return requests.post(Endpoints.COURIER_LOGIN, json=payload)

    @staticmethod
    def delete_courier(courier_id):
        return requests.delete(f"{Endpoints.COURIER}/{courier_id}")

    @staticmethod
    def create_order(payload):
        return requests.post(Endpoints.ORDERS, json=payload)

    @staticmethod
    def get_orders():
        return requests.get(Endpoints.ORDERS)