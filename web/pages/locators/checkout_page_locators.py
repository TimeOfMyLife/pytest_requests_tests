from selenium.webdriver.common.by import By


class CheckoutPageLocators:
    CREDIT_CARD_INPUT_FIELD = (By.CSS_SELECTOR, "input[id='cardNumber']")