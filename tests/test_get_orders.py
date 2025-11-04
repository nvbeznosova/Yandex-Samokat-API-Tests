import requests
import allure
from helpers.courier_helper import BASE_URL

@allure.epic("Order API")
@allure.feature("Get orders")
class TestGetOrders:

    @allure.title("Получение списка заказов возвращает orders")
    def test_get_orders_list_returns_orders(self):
        response = requests.get(f"{BASE_URL}/orders")
        assert response.status_code == 200
        assert "orders" in response.json()