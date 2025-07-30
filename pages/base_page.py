from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


PAGE_TITLE = (By.CSS_SELECTOR, "span[data-test='title']")


class BasePage:
    def __init__(self, browser, timeout=10, url=None):
        self.browser = browser
        self.domain = "https://www.saucedemo.com/"
        self.url = url
        self.page_title = None

    def open(self):
        self.browser.get(self.url)

    def element_is_presence(self, find_by, locator, element_name='element', timeout=5):
        try:
            self.browser.implicitly_wait(timeout)
            return WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((find_by, locator)))
        except TimeoutException:
            raise AssertionError(f"Can't find '{element_name}' on the page '{self.page_title}'")

    def set_value(self, find_by, locator, value, element_name='', timeout=5):
        element = self.element_is_presence(find_by, locator, element_name, timeout)
        element.send_keys(value)

    def click_element(self, find_by, locator, element_name='', timeout=15):
        try:
            self.browser.implicitly_wait(timeout)
            element = WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((find_by, locator)))
            element.click()
        except TimeoutException:
            raise AssertionError(f"Can't find '{element_name}' on the page '{self.page_title}'")

    def get_text(self, find_by, locator, element_name='', timeout=5):
        element = self.element_is_presence(find_by, locator, element_name, timeout)
        return element.text

    def validate_page_title(self, expected_page_title):
        actual_page_title = self.get_text(*PAGE_TITLE, element_name="Page title", timeout=25)
        assert expected_page_title == actual_page_title, \
            "Page titles dont match. {expected_page_title} != {actual_page_title}"
