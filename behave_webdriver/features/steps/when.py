from behave import *

@when('I click on the element "{element}"')
def click_element(context, element):
    pass

@when('I doubleclick on the element "{element}"')
def doubleclick_element(context, element):
    pass

@when('I click on the link "{link_text}"')
def click_link(context, link_text):
    pass

@when('I set the inputfield "{element}" to "{value}"')
def set_input(context, element, value):
    pass

@when('I clear the inputfield "{element}"')
def clear_input(context, element):
    pass

@when('I drag element "{from_element}" to element "{to_element}"')
def drag_element(context, from_element, to_element):
    pass

@when('I submit the form "{element}"')
def submit_form(context, element):
    pass

@when('I set a cookie "{cookie_key}" with the content "{value}"')
def set_cookie(context, cookie_key, value):
    pass

@when('I delete the cookie "{cookie_key}')
def delete_cookie(context, cookie_key):
    pass

@when('I press "{button_element}"')
def press_button(context, button_element):
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

@when('I scroll to element {element}')
def scroll_to(context, element):
    pass

@when('I close the last opened tab')
def close_last_tab(context):
    pass

@when('I close the last opened window')
def close_last_window(context):
    pass

@when('I select the {nth:d} option for element "{element}"')
def select_nth_option(context, n, element):
    pass

@when('I select the option with the text {text} for element {element}')
def select_option_by_text(context, text, element):
    pass

@when('I select the option with the value {value} for element {element}')
def select_option_by_text(context, value, element):
    pass

@when('I move to element "{element}" with an offset of ({x_offset:d},{y_offset:d})')
def move_to_element_offset(context, element, x_offset, y_offset):
    pass

@when('I move to element "{element}"')
def move_to_element(context, element):
    pass