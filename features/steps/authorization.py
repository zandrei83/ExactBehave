from behave import step, given, when, then
from pages.login_page import LoginPage


@given('User is on the page with Login form')
def user_loging(context):
    login_page = LoginPage(context.browser)
    login_page.open()
    context.login_page = login_page


@when('User fill in the login form with user name "{user_name}" and password "{user_password}"')
def user_fill_in_the_login_form(context, user_name, user_password):
    login_page = context.login_page
    login_page.complete_form(user_name, user_password)


@step('Click Login button')
def click_login_button(context):
    login_page = context.login_page
    login_page.click_login_button()


@then(u'The error message "{error_text}" is displayed')
def verify_error_message_text(context, error_text):
    base_page = LoginPage(context.browser)
    base_page.verify_error_message(error_text)
