import time

from selenium.webdriver.support.wait import WebDriverWait
from web.pages.base_steps import BaseSteps
from selenium.webdriver.support import expected_conditions as EC

from web.pages.locators.home_page_locators import HomePageLocators

HOME_URL = "https://reqres.in/"


class HomePage(BaseSteps):

    def __init__(self, driver):
        super().__init__(driver)

    def open_home_page(self, time=10):
        self.driver.get(HOME_URL)
        WebDriverWait(self.driver, time).until(
            EC.url_to_be(HOME_URL),
            message=f"Failed to open home page. Current URL: {self.driver.current_url}"
        )

    def call_request(self, request_locator):
        self.click_element(request_locator)
        time.sleep(3)

    def get_status_code(self):
        return self.get_element_text(HomePageLocators.RESPONSE_CODE)

    def get_response_body(self):
        return self.get_element_text(HomePageLocators.RESPONSE_BODY)
