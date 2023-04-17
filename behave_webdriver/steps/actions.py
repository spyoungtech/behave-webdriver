import string
from behave import *
from behave_webdriver.transformers import matcher_mapping
try:
    from urllib.parse import urljoin
except ImportError:
    from urlparse import urljoin  # Python 2


if 'transform-parse' not in matcher_mapping:
    use_step_matcher('parse')
else:
    use_step_matcher('transform-parse')


@step('I pause for {milliseconds:d}ms')
def sleep_ms(context, milliseconds):
    context.behave_driver.pause(milliseconds)


@step('I click on the element "{element}"')
def click_element(context, element):
    context.behave_driver.click_element(element)


@step('I doubleclick on the element "{element}"')
def doubleclick_element(context, element):
    context.behave_driver.doubleclick_element(element)


@step('I click on the link "{link_text}"')
def click_link(context, link_text):
    context.behave_driver.click_link_text(link_text)


@step('I click on the button "{element}"')
def click_button(context, element):
    context.behave_driver.click_element(element)


@step('I set "{value}" to the inputfield "{element}"')
def set_input(context, value, element):
    elem = context.behave_driver.get_element(element)
    elem.clear()
    elem.send_keys(value)


@step('I add "{value}" to the inputfield "{element}"')
def add_input(context, value, element):
    elem = context.behave_driver.get_element(element)
    elem.send_keys(value)


@step('I clear the inputfield "{element}"')
def clear_input(context, element):
    elem = context.behave_driver.get_element(element)
    elem.clear()


@step('I drag element "{from_element}" to element "{to_element}"')
def drag_element(context, from_element, to_element):
    context.behave_driver.drag_element(from_element, to_element)


@step('I submit the form "{element}"')
def submit_form(context, element):
    context.behave_driver.submit(element)


@step('I set a cookie "{cookie_key}" with the content "{value}"')
def set_cookie(context, cookie_key, value):
    context.behave_driver.add_cookie({'name': cookie_key, 'value': value})


@step('I delete the cookie "{cookie_key}"')
def delete_cookie(context, cookie_key):
    context.behave_driver.delete_cookie(cookie_key)


@step('I press "{key}"')
def press_button(context, key):
    context.behave_driver.press_button(key)


@step('I scroll to element "{element}"')
def scroll_to(context, element):
    context.behave_driver.scroll_to_element(element)


@step('I select the {nth} option for element "{element}"')
def select_nth_option(context, nth, element):
    index = int(''.join(char for char in nth if char in string.digits))
    context.behave_driver.select_option(element,
                                        by='index',
                                        by_arg=index)


@step('I move to element "{element}" with an offset of {x_offset:d},{y_offset:d}')
def move_to_element_offset(context, element, x_offset, y_offset):
    context.behave_driver.move_to_element(element, (x_offset, y_offset))


@step('I move to element "{element}"')
def move_to_element(context, element):
    context.behave_driver.move_to_element(element)


use_step_matcher('parse')
