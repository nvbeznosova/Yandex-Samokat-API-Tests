import pytest
import requests
import allure
from helpers.courier_helper import BASE_URL

@allure.epic("Order API")
@allure.feature("Create order")
class TestCreateOrder:

    @allure.title("Создание заказа с разными вариантами цветов возвращает track")
    @pytest.mark.parametrize("color", [[], ["BLACK"], ["GREY"], ["BLACK", "GREY"]])
    def test_create_order_with_colors_returns_track(self, color):
        payload = {
            "firstName": "Иван",
            "lastName": "Иванов",
            "address": "Москва",
            "metroStation": 4,
            "phone": "+79999999999",
            "rentTime": 5,
            "deliveryDate": "2025-11-04",
            "comment": "Тестовый заказ",
            "color": color
        }
        response = requests.post(f"{BASE_URL}/orders", json=payload)
        assert response.status_code == 201
        assert "track" in response.json()