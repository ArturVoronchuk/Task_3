import random
import string
import requests

from urls import USER_REGISTER_ENDPOINT, LOGIN_PAGE_URL, USER_DELETE_ENDPOINT

class UserGenerator:
    @staticmethod
    def random_string(length=10):
        return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))

    @staticmethod
    def generate_user_payload():
        email = f"test_{UserGenerator.random_string()}@gmail.ru"
        password = UserGenerator.random_string()
        name = "Artur Voronchuk"
        return {
            "email": email,
            "password": password,
            "name": name,
        }

    @classmethod
    def register_user(cls, payload=None):
        if payload is None:
            payload = cls.generate_user_payload()

        response = requests.post(
            f"{USER_REGISTER_ENDPOINT}",
            json=payload
        )
        response.raise_for_status()
        return payload

    @staticmethod
    def delete_user(email, password):

        login_resp = requests.post(
            f"{LOGIN_PAGE_URL}",
            json={"email": email, "password": password}
        )

        if login_resp.status_code != 200:
            return False

        data = login_resp.json()
        token = data.get("accessToken")

        if not token:
            return False

        delete_resp = requests.delete(
            f"{USER_DELETE_ENDPOINT}",
            headers={"Authorization": token}
        )

        return delete_resp.ok or delete_resp.status_code == 404