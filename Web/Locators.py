from selenium.webdriver.common.by import By


class MainLocators:
    """
    Данный класс объединяет локаторы главной страницы.
    """
    # Центральная кнопка на странице
    REQUEST_BTN: tuple = (By.XPATH, '//*[@id="console"]/div[2]/div[1]/p/strong/a/span')
    SUPPORT_BTN: tuple = (By.XPATH, '/html/body/div[2]/div/div/div[1]/button/a')
    RESPONCE_FORM: tuple = (By.XPATH, '//*[@id="console"]/div[2]/div[2]/pre')
    REQUEST_SINGLE_USER_BTN: tuple = (By.XPATH, '//*[@id="console"]/div[1]/ul/li[2]')
