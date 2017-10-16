from behave import *
import time
@when('I pause for {miliseconds:d}ms')
def sleep_ms(context, miliseconds):
    # TODO: webdriver wait instead
    time.sleep(miliseconds/1000)

@when('I click on the element "{element}"')
def click_element(context, element):
    context.behave_driver.click_element(element)

@when('I doubleclick on the element "{element}"')
def doubleclick_element(context, element):
    context.behave_driver.click_element(element, n=2)

@when('I click on the link "{link_text}"')
def click_link(context, link_text):
    context.behave_driver.click_link_text(link_text)

@when('I click on the button "{element}"')
def click_button(context, element):
    context.behave_driver.click_element(element)

@when('I set "{value}" to the inputfield "{element}"')
def set_input(context, element, value):
    elem = context.behave_driver.get_element(element)
    elem.clear()
    elem.send_keys(value)

@when('I set {value} to the inputfield "{element}"')
def set_input(context, value, element):

    elem = context.behave_driver.get_element(element)
    elem.clear()
    elem.send_keys(value)

@when('I add "{value}" to the inputfield "{element}"')
def add_input(context, value, element):
    elem = context.behave_driver.get_element(element)
    elem.send_keys(value)

@when('I clear the inputfield "{element}"')
def clear_input(context, element):
    elem = context.behave_driver.get_element(element)
    elem.clear()

@when('I drag element "{from_element}" to element "{to_element}"')
def drag_element(context, from_element, to_element):
    context.behave_driver.drag_element(from_element, to_element)

@when('I submit the form "{element}"')
def submit_form(context, element):
    context.behave_driver.submit(element)


@when('I set a cookie "{cookie_key}" with the content "{value}"')
def set_cookie(context, cookie_key, value):
    context.behave_driver.add_cookie({'name': cookie_key, 'value': value})

@when('I delete the cookie "{cookie_key}')
def delete_cookie(context, cookie_key):
    context.behave_driver.delete_cookie(cookie_key)

@when('I press "{key}"')
def press_button(context, key):
    context.behave_driver.send_keys(key)

@when('I accept the alert')
def accept_alert(context):
    context.behave_driver.alert.accept()

@when('I dismiss the alert')
def dismiss_alert(context):
    context.behave_driver.alert.dismiss()

@when('I enter {text} into the prompt')
def handle_prompt(context, text):
    context.behave_driver.alert.send_keys(text)

@when('I scroll to element {element}')
def scroll_to(context, element):
    context.behave_driver.scroll_to_element(element)

@when('I close the last opened tab')
def close_last_tab(context):
    context.behave_driver.window_handles[-1].close()

@when('I close the last opened window')
def close_last_window(context):
    raise NotImplementedError('This step has not been implemented yet')

@when('I select the {nth:d} option for element "{element}"')
def select_nth_option(context, n, element):
    raise NotImplementedError('This step has not been implemented yet')

@when('I select the option with the text {text} for element {element}')
def select_option_by_text(context, text, element):
    raise NotImplementedError('This step has not been implemented yet')

@when('I select the option with the value {value} for element {element}')
def select_option_by_text(context, value, element):
    raise NotImplementedError('This step has not been implemented yet')

@when('I move to element "{element}" with an offset of ({x_offset:d},{y_offset:d})')
def move_to_element_offset(context, element, x_offset, y_offset):
    raise NotImplementedError('This step has not been implemented yet')

@when('I move to element "{element}"')
def move_to_element(context, element):
    raise NotImplementedError('This step has not been implemented yet')