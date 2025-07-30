from behave import then
from pages.base_page import BasePage


@then(u'The user should be navigated to {page_title} page')
def verify_user_was_navigated_to_page(context, page_title):
    base_page = BasePage(context.browser)
    base_page.validate_page_title(page_title)
