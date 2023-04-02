import pytest
import requests


class TestAPI:
    @pytest.fixture
    def api_base(self):
        return 'https://reqres.in/api'

    def test_get_users(self, api_base):
        response = requests.get(f'{api_base}/users?page=2')
        assert response.status_code == 200
        assert len(response.json()['data']) == 6

    def test_get_single_user(self, api_base):
        response = requests.get(f'{api_base}/users/2')
        assert response.status_code == 200
        assert response.json()['data']['email'] == 'janet.weaver@reqres.in'

    def test_create_user(self, api_base):
        user_data = {
            'name': 'test user',
            'job': 'tester'
        }
        response = requests.post(f'{api_base}/users', json=user_data)
        assert response.status_code == 201
        assert response.json()['name'] == user_data['name']
        assert response.json()['job'] == user_data['job']

    def test_update_user(self, api_base):
        user_data = {
            'name': 'test user',
            'job': 'tester'
        }
        response = requests.put(f'{api_base}/users/2', json=user_data)
        assert response.status_code == 200
        assert response.json()['name'] == user_data['name']
        assert response.json()['job'] == user_data['job']

    def test_delete_user(self, api_base):
        response = requests.delete(f'{api_base}/users/2')
        assert response.status_code == 204

        # Make sure user is really deleted
        response = requests.get(f'{api_base}/users/2')
        assert response.status_code == 404

    """
    In this example, we use Pytest's `fixture` decorator to define a fixture called `api_base`. This fixture returns just the base URL for the Reqres API, so that we can reuse it in all our tests.
    
    Each test function then sends a request to the API using the requests library, and checks the response status code and content to make sure it's what we expect. For example, `test_get_users` makes a GET request to the `/users` endpoint with the `page` parameter set to 2, and checks that the response code is 200 (OK) and that the JSON response contains exactly 6 users.
    
    Note that this is just a simple example and there are many more things you can do with Pytest to test APIs, such as asserting exact response content, testing error cases, and using fixtures to share setup and cleanup code among tests.
    """
