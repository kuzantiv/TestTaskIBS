import json
import time

from Web.BaseClass import BaseClass
from Web.Data import Data


class MainPage(BaseClass, Data):

    def open_main_page(self):
        self.open_url(self.BASE_URL)
        return self

    def assert_responce_data_in_form(self, response_data):
        time.sleep(1)
        text_in_form = self.driver.find_element(*self.RESPONCE_FORM).text
        text_in_form = json.loads(text_in_form)
        assert text_in_form == response_data, \
            f'\n{text_in_form}\n{response_data}'
