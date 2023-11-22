from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseSteps:

    def __init__(self, driver):
        self.driver = driver

    def open_page(self, url):
        return self.driver.get(url)

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    def click_element(self, locator):
        element = self.find_element(locator)
        element.click()

    def get_element_text(self, locator):
        element = self.find_element(locator)
        return element.text

    def get_element_property(self, locator, property_name):
        element = self.find_element(locator)
        return element.get_attribute(property_name)


