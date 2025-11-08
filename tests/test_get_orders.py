import allure
from helpers.api_helpers import ApiClient


@allure.epic("Order API")
@allure.feature("Get orders")
class TestGetOrders:

    @allure.title("Получение списка заказов возвращает orders")
    def test_get_orders_list_returns_orders(self):
        response = ApiClient.get_orders()
        assert response.status_code == 200
        assert "orders" in response.json()