import pytest
from selenium import webdriver
from web.pages.home_page import HomePage
from api.tests.conftest import api_client_v1


@pytest.fixture(scope="session")
def chrome_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope="module")
def home_page():
    home_page = HomePage(chrome_driver)
    home_page.open_home_page()
    return home_page
