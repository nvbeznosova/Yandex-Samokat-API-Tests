import requests
import allure
from helpers.courier_helper import BASE_URL, register_new_courier

@allure.epic("Courier API")
@allure.feature("Create courier")
class TestCreateCourier:

    @allure.title("Успешное создание курьера возвращает 201 и ok:true")
    def test_create_courier_success_returns_201(self):
        response, _ = register_new_courier()
        assert response.status_code == 201
        assert response.json()["ok"] is True

    @allure.title("Нельзя создать двух одинаковых курьеров (409)")
    def test_create_duplicate_courier_returns_409(self):
        _, payload = register_new_courier()
        response = requests.post(f"{BASE_URL}/courier", json=payload)
        assert response.status_code == 409
        assert "Этот логин уже используется" in response.text

    @allure.title("Создание курьера без обязательного поля возвращает 400")
    def test_create_courier_without_required_field_returns_400(self):
        payload = {"login": "test_login"}
        response = requests.post(f"{BASE_URL}/courier", json=payload)
        assert response.status_code == 400