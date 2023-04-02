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

    def test_contact_form(self, get_web_url):
        data = {
            "name": "Test User",
            "email": "testuser@gmail.com",
            "message": "This is a test message."
        }
        response = requests.post(get_web_url, data=data)
        assert response.status_code == 200



"""
This code contains a TestAPI class for testing the API, and a TestWeb class for testing the website. The tests are parameterized, and fixtures are used to obtain the URL and other data that may be needed for the tests. 

You can modify this code as per your specific requirements, and add more tests and classes as needed. Good luck with your project!
"""
"""
Here is an example of positive and negative tests for logging in to https://reqres.in/:
"""

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

"""
The test_successful_login method sends a valid payload to the login endpoint and checks if the response status code is 200 and if the token key is present in the response JSON.

The test_unsuccessful_login method is a parametrized test that sends a series of invalid payloads to the login endpoint and checks if the response status code is 400 and if the expected error message is present in the response JSON. The different invalid payloads represent various error conditions, such as missing email, missing password and user not found.

These tests can be used as a reference when writing your own tests for logging in to https://reqres.in/.
"""