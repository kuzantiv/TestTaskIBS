# Selenium imports
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from Web.Constants import CommonConstants
from Web.Locators import MainLocators


class BaseClass(MainLocators, CommonConstants):
    """Данный класс объединяет функции участвующие в большинстве тестов."""

    def __init__(self, driver):
        self.driver = driver

    wait = WebDriverWait

    def open_url(self, url: str):
        """Открывает в браузере указанную страницу."""
        self.driver.get(url)
        return self

    def click_the_button(self, locator: tuple, timeout: float = 10):
        """Нажимает кнопку по указанному локатору."""
        self.wait_until_element_is_visible(locator)
        self.wait(self.driver, timeout).until(ec.element_to_be_clickable(locator),
                                              f'Кнопка не найдена {locator[1]}').click()
        return self

    def check_current_page_url(self, page: str = None):
        """Сверяет текущий адрес страницы с указанным в параметре"""
        self.wait(self.driver, 3) \
            .until(lambda _: self.driver.current_url == f'{page}',
                   f'Не произошел переход на {page} в течении 3 сек.')
        return self

    def wait_until_element_is_visible(self,
                                      locator: tuple,
                                      msg: str = "Элемент не видим",
                                      timeout: float = 10):
        """
        Проверяет то, что элемент присутствует в DOM страницы и виден.
        Видимость означает, что элемент не только отображается,
        но также имеет высоту и ширину больше 0.
        """
        self.wait(self.driver, timeout) \
            .until(ec.visibility_of_element_located(locator), msg)
        return self

    def wait_until_element_is_clickable(self, locator: tuple, timeout: float = 10):
        """Проверяет видимость элемента, и его кликабельность."""
        self.wait_until_element_is_visible(locator)
        self.wait(self.driver, timeout).until(ec.element_to_be_clickable(locator))
        return self

    def type_text(self, locator: tuple, text: str):
        """Печатает текст в элемент для ввода текста."""
        self.driver.find_element(*locator).send_keys(text)
        return self

    def find_element(self, locator: tuple):
        """Находит Web элемент."""
        self.driver.find_element(*locator)
        return self

    def wait_until_disappears(self, element: tuple, timeout: float = 10):
        """Ожидает исчезновения элемента."""
        self.wait(self.driver, timeout) \
            .until(ec.invisibility_of_element_located(element))
        return self

    def assert_error_message(self, error_locator: tuple, expected_text: str):
        """Проверяет текст окна или элемента уведомляющего об ошибке."""
        self.wait_until_element_is_visible(error_locator, 'Элемент оповещения об ошибке не найден')
        assert self.driver.find_element(*error_locator).text == expected_text
        return self

    def assert_alert_message(self, error_locator: tuple, expected_text: str):
        """Проверяет текст окна или элемента уведомления."""
        self.wait_until_element_is_visible(error_locator, 'Элемент оповещения не найден')
        assert self.driver.find_element(*error_locator).text == expected_text
        return self
