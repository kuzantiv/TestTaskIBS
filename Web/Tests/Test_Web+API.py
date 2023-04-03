import json

import pytest
from selenium.webdriver.common.by import By
from seleniumwire import webdriver
from seleniumwire.utils import decode


@pytest.fixture(scope="session")
def driver():
    driver = webdriver.Chrome()
    driver.get('https://reqres.in/')
    driver.delete_all_cookies()
    yield driver
    driver.quit()


@pytest.mark.parametrize(
    'data_id',
    [
        "users",
        "users-single",
        "users-single-not-found",
        "unknown",
        "unknown-single",
        "unknown-single-not-found",
        "post",
        "put",
        "patch",
        "delete",
        "register-successful",
        "register-unsuccessful",
        "login-successful",
        "login-unsuccessful",
        "delay"
    ]

)
def test_api_responce_body(data_id: str, driver):
    """
    Проверяет статус код и тело ответа отображаемый на форме
    при нажатии на кнопку с перехваченным ответом от API.
    """
    element = driver.find_element(By.XPATH,
                                  f'//section[@id="console"]//li[@data-id="{data_id}"]')
    method = element.get_attribute('data-http').upper()
    endpoint = element.find_element('xpath',
                                    ".//*").get_attribute('href')
    element.click()
    resp = driver.wait_for_request(endpoint, 10)
    body = decode(resp.response.body,
                  resp.response.headers.get('Content-Encoding', 'identity'))
    body = json.loads(body)

    resp_code_on_web = driver.find_element(By.XPATH,
                                           '//span[@data-key="response-code"]').text
    resp_body_on_web = driver.find_element(By.XPATH,
                                           '//pre[@data-key="output-response"]').text
    resp_body_on_web = json.loads(resp_body_on_web)
    assert int(resp_code_on_web) == resp.response.status_code
    assert resp_body_on_web == body, \
        f'\n{resp_body_on_web}'
