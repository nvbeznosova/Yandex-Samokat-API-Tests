import requests
import allure
from helpers.courier_helper import BASE_URL

@allure.epic("Courier API")
@allure.feature("Login courier")
class TestLoginCourier:

    @allure.title("Успешный логин курьера возвращает id")
    def test_login_success_returns_id(self, new_courier):
        payload, _ = new_courier
        response = requests.post(f"{BASE_URL}/courier/login", json={
            "login": payload["login"],
            "password": payload["password"]
        })
        assert response.status_code == 200
        assert "id" in response.json()

    @allure.title("Логин с неверным паролем возвращает 404")
    def test_login_with_wrong_password_returns_404(self, new_courier):
        payload, _ = new_courier
        response = requests.post(f"{BASE_URL}/courier/login", json={
            "login": payload["login"],
            "password": "wrongpass"
        })
        assert response.status_code == 404

    @allure.title("Логин без пароля возвращает 400")
    def test_login_without_password_returns_400(self, new_courier):
        payload, _ = new_courier
        response = requests.post(f"{BASE_URL}/courier/login", json={
            "login": payload["login"]
        })
        assert response.status_code == 400

    @allure.title("Логин без логина возвращает 400")
    def test_login_without_login_returns_400(self, new_courier):
        payload, _ = new_courier
        response = requests.post(f"{BASE_URL}/courier/login", json={
            "password": payload["password"]
        })
        assert response.status_code == 400

    @allure.title("Логин несуществующего пользователя возвращает 404")
    def test_login_nonexistent_user_returns_404(self):
        response = requests.post(f"{BASE_URL}/courier/login", json={
            "login": "nonexistent_user",
            "password": "fake_password"
        })
        assert response.status_code == 404