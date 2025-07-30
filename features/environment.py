import os
from selenium import webdriver
from behave import fixture, use_fixture


@fixture
def browser_chrome(context):
    from selenium.webdriver.chrome.service import Service as ChromeService
    from webdriver_manager.chrome import ChromeDriverManager
    from selenium.webdriver.chrome.options import Options

    options = Options()
    options.add_argument("--disable-search-engine-choice-screen")

    prefs = {
        "credentials_enable_service": False,  # Disables the "credentials_enable_service" setting
        "profile.password_manager_enabled": False,  # Disables the password manager
        "profile.password_manager_leak_detection": False  # Disables password leak detection
    }
    options.add_experimental_option("prefs", prefs)

    chrome_install = ChromeDriverManager().install()

    folder = os.path.dirname(chrome_install)
    chromedriver_path = os.path.join(folder, "chromedriver.exe")

    browser = webdriver.Chrome(service=ChromeService(chromedriver_path), options=options)
    browser.maximize_window()

    context.browser = browser

    yield context.browser

    context.browser.quit()


def before_all(context):
    """
    Hook to run before all features. Uses the browser fixture.
    """
    use_fixture(browser_chrome, context)
