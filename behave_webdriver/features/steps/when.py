from behave import *
from behave_webdriver import utils

@when('I click on the element "{selector}"')
def click_element(context, selector):
    pass

@when('I click on the link "{link_text}"')
def click_link(context, link_text):
    pass

@when('I set the inputfield "{selector}" to "{value}"')
def set_input(context, selector, value):
    pass

@when('I clear the inputfield "{selector}"')
def clear_input(context, selector):
    pass

@when('I drag element "{from_selector}" to element "{to_selector}"')
def drag_element(context, from_selector, to_selector):
    pass

@when('I submit the form "{selector}"')
def submit_form(context, selector):
    pass

@when('I set a cookie "{cookie_key}" with the content "{value}"')
def set_cookie(context, cookie_key, value):
    pass

@when('I delete the cookie "{cookie_key}')
def delete_cookie(context, cookie_key):
    pass

@when('I press "{button_selector}"')
def press_button(context, button_selector):
    pass

@when('I accept the alert')
def accept_alert(context):
    pass

@when('I dismiss the alert')
def dismiss_alert(context):
    pass

@when('I enter {text} into the prompt')
def handle_prompt(context, text):
    pass

@when('I scroll to element {selector}')
def scroll_to(context, selector):
    pass

@when('I close the last opened tab')
def close_last_tab(context):
    pass

@when('I close the last opened window')
def close_last_window(context):
    pass

@when('I select the {nth:d} option for element "{selector}"')
def select_nth_option(context, n, selector):
    pass

@when('I select the option with the text {text} for element {selector}')
def select_option_by_text(context, text, selector):
    pass

@when('I select the option with the value {value} for element {selector}')
def select_option_by_text(context, value, selector):
    pass

@when('I move to element "{selector}" with an offset of ({x_offset:d},{y_offset:d})')
def move_to_element_offset(context, selector, x_offset, y_offset):
    pass

@when('I move to element "{selector}"')
def move_to_element(context, selector):
    pass