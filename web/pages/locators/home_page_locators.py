from selenium.webdriver.common.by import By


class HomePageLocators:
    USER_LIST = (By.CSS_SELECTOR, "li[data-id='users']")
    SINGLE_USER = (By.CSS_SELECTOR, "li[data-id='users-single']")
    SINGLE_USER_NOT_FOUND = (By.CSS_SELECTOR, "li[data-id='users-single-not-found']")
    LIST_RESOURCE = (By.CSS_SELECTOR, "li[data-id='unknown']")
    SINGLE_RESOURCE = (By.CSS_SELECTOR, "li[data-id='unknown-single']")
    SINGLE_RESOURCE_NOT_FOUND = (By.CSS_SELECTOR, "li[data-id='unknown-single']")
    CREATE = (By.CSS_SELECTOR, "li[data-id='post']")
    PUT_UPDATE = (By.CSS_SELECTOR, "li[data-id='put']")
    PATCH_UPDATE = (By.CSS_SELECTOR, "li[data-id='patch']")
    DELETE = (By.CSS_SELECTOR, "li[data-id='delete']")
    REGISTER_SUCCESSFUL = (By.CSS_SELECTOR, "li[data-id='register-successful']")
    REGISTER_UNSUCCESSFUL = (By.CSS_SELECTOR, "li[data-id='register-unsuccessful']")
    LOGIN_SUCCESSFUL = (By.CSS_SELECTOR, "li[data-id='login-successful']")
    LOGIN_UNSUCCESSFUL = (By.CSS_SELECTOR, "li[data-id='login-unsuccessful']")
    DELAYED_RESPONSE = (By.CSS_SELECTOR, "li[data-id='delay']")
    TITLE = (By.XPATH, "//*[contains(text(), 'real API')]")
    RESPONSE_CODE = (By.CSS_SELECTOR, ".response-code")
    RESPONSE_BODY = (By.XPATH, "//*[@data-key='output-response']")
    SUPPORT_REQRES_BUTTON = (By.XPATH, "//button[contains(text(),'Support ReqRes')]")