try:
    from urllib.parse import urljoin
except ImportError:
    from urlparse import urljoin

from behave import *
from behave_webdriver.steps import *


@given('I send a {method} request to the url "{url}"')
def send_request(context, method, url):
    context.response = context.behave_driver.request(method, url)


@given('I send a {method} request to the page "{page}"')
def send_request_page(context, method, page):
    url = urljoin(context.base_url, page)
    context.response = context.behave_driver.request(method, url)


@then('I expect the response text contains "{text}"')
def check_response_text_contains(context, text):
    assert text in context.response.text
