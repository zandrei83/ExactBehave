from pages.base_page import BasePage
from selenium.webdriver.common.by import By

USER_NAME_INPUT = (By.ID, "user-name")
USER_PASSWORD_INPUT = (By.ID, "password")
LOGIN_BUTTON = (By.ID, "login-button")
ERROR_MESSAGE_TEXT = (By.CSS_SELECTOR, "h3[data-test='error']")


class LoginPage(BasePage):

    def __init__(self, *args, **kwargs):
        super(LoginPage, self).__init__(*args, **kwargs)
        self.url = self.domain
        self.page_title = "Swag Labs"

    def complete_form(self, user_name, user_password):
        self.set_value(*USER_NAME_INPUT, user_name, "User Name", timeout=25)
        self.set_value(*USER_PASSWORD_INPUT, user_password, "User Name")

    def click_login_button(self):
        self.click_element(*LOGIN_BUTTON, element_name="Login Button")

    def verify_error_message(self, expected_error_text):
        actual_error_text = self.get_text(*ERROR_MESSAGE_TEXT, element_name="Login error text", timeout=25)
        assert expected_error_text == actual_error_text, \
            "Page titles dont match. {expected_error_text} != {actual_error_text}"
