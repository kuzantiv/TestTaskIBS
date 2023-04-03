from Web.Pages.MainPage import MainPage


class TestMainPage:

    def test_01_open_main_page(self, driver):
        """Проверяет открытие главной страницы."""
        main_page = MainPage(driver)
        main_page \
            .open_main_page() \
            .check_current_page_url(main_page.BASE_URL)
        assert driver.current_url == main_page.BASE_URL, \
            'Не соответствие текущего URL'

    def test_02_click_get_user_and_compare_result(self, driver):
        """
         Проверяет клик по кнопке [get single user],
         и сравнивает ответ пришедший на форму.
         """
        main_page = MainPage(driver)
        main_page \
            .open_main_page() \
            .click_the_button(main_page.REQUEST_SINGLE_USER_BTN) \
            .assert_responce_data_in_form(main_page.SINGLE_USER)
