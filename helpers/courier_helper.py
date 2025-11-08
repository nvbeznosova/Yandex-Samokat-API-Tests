import random
import string
from helpers.api_helpers import ApiClient


def generate_random_string(length=8):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))


def register_new_courier():
    login = generate_random_string()
    password = generate_random_string()
    first_name = generate_random_string()

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }
    response = ApiClient.create_courier(payload)
    return response, payload