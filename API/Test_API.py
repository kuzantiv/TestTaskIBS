import pytest
import requests

api_url_base = 'https://reqres.in/api/'


class TestAPI:

    @pytest.mark.parametrize("user_id, expected_response_code", [(1, 200), (2, 200)])
    def test_get_user(self, user_id, expected_response_code):
        api_url = '{}users/{}'.format(api_url_base, user_id)
        response = requests.get(api_url)
        assert response.status_code == expected_response_code

    @pytest.mark.parametrize("user_id, expected_response_code", [(0, 404), (100, 404)])
    def test_get_user_negative(self, user_id, expected_response_code):
        api_url = '{}users/{}'.format(api_url_base, user_id)
        response = requests.get(api_url)
        assert response.status_code == expected_response_code


class TestWeb:

    @pytest.fixture(scope="class")
    def get_web_url(self):
        return "https://reqres.in/"

    def test_homepage(self, get_web_url):
        response = requests.get(get_web_url)
        print(response.text)
        assert response.status_code == 200


API_BASE_URL = 'https://reqres.in/api/'


class TestAuthentication:

    def test_successful_login(self):
        endpoint = f'{API_BASE_URL}login'
        payload = {"email": "eve.holt@reqres.in", "password": "pistol"}
        response = requests.post(endpoint, data=payload)
        assert response.status_code == 200
        assert 'token' in response.json()

    @pytest.mark.parametrize(
        "invalid_payload, expected_error_message",
        [
            (
                    {"email": "example@example.com"},
                    "Missing password",
            ),
            (
                    {"password": "123456"},
                    "Missing email or username",
            ),
            (
                    {"email": "example@example.com", "password": "123456"},
                    "user not found",
            ),
        ],
    )
    def test_unsuccessful_login(self, invalid_payload, expected_error_message):
        endpoint = f'{API_BASE_URL}login'
        response = requests.post(endpoint, data=invalid_payload)
        assert response.status_code == 400
        assert expected_error_message in str(response.json())
