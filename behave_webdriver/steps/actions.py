import string
from behave import *
try:
    from urllib.parse import urljoin
except ImportError:
    from urlparse import urljoin  # Python 2


use_step_matcher('transform-parse')


@when('I pause for {milliseconds:d}ms')
def sleep_ms(context, milliseconds):
    context.behave_driver.pause(milliseconds)


@when('I click on the element "{element}"')
def click_element(context, element):
    context.behave_driver.click_element(element)


@when('I doubleclick on the element "{element}"')
def doubleclick_element(context, element):
    context.behave_driver.doubleclick_element(element)


@when('I click on the link "{link_text}"')
def click_link(context, link_text):
    context.behave_driver.click_link_text(link_text)


@when('I click on the button "{element}"')
def click_button(context, element):
    context.behave_driver.click_element(element)


@when('I set "{value}" to the inputfield "{element}"')
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


@when('I delete the cookie "{cookie_key}"')
def delete_cookie(context, cookie_key):
    context.behave_driver.delete_cookie(cookie_key)


@when('I press "{key}"')
def press_button(context, key):
    context.behave_driver.press_button(key)


@when('I scroll to element "{element}"')
def scroll_to(context, element):
    context.behave_driver.scroll_to_element(element)


@when('I select the {nth} option for element "{element}"')
def select_nth_option(context, nth, element):
    index = int(''.join(char for char in nth if char in string.digits))
    context.behave_driver.select_option(element,
                                        by='index',
                                        by_arg=index)


@when('I move to element "{element}" with an offset of {x_offset:d},{y_offset:d}')
def move_to_element_offset(context, element, x_offset, y_offset):
    context.behave_driver.move_to_element(element, (x_offset, y_offset))


@when('I move to element "{element}"')
def move_to_element(context, element):
    context.behave_driver.move_to_element(element)


use_step_matcher('transform-re')


@when('I close the last opened (tab|window)')
def close_last_tab(context, _):
    context.behave_driver.switch_to_window(context.behave_driver.last_opened_handle)
    context.behave_driver.close()
    context.behave_driver.switch_to_window(context.behave_driver.primary_handle)


@when('I focus the last opened (tab|window)')
def focus_last_tab(context, _):
    context.behave_driver.switch_to_window(context.behave_driver.last_opened_handle)


@when('I select the option with the (text|value|name) "([^"]*)?" for element "([^"]*)?"')
def select_option_by(context, attr, attr_value, element):
    attr_map = {'text': 'visible_text'}
    attr = attr_map.get(attr, attr)
    context.behave_driver.select_option(select_element=element,
                                        by=attr,
                                        by_arg=attr_value)


@when('I accept the (alertbox|confirmbox|prompt)')
def accept_alert(context, modal_type):
    context.behave_driver.alert.accept()


@when('I dismiss the (alertbox|confirmbox|prompt)')
def dismiss_alert(context, modal_type):
    context.behave_driver.alert.dismiss()


@when('I enter "([^"]*)?" into the (alertbox|confirmbox|prompt)')
def handle_prompt(context, text, modal_type):
    context.behave_driver.alert.send_keys(text)


@given('I have closed all but the first (window|tab)')
def close_secondary_windows(context, window_or_tab):
    if len(context.behave_driver.window_handles) > 1:
        for handle in context.behave_driver.window_handles[1:]:
            context.behave_driver.switch_to_window(handle)
            context.behave_driver.close()
    context.behave_driver.switch_to_window(context.behave_driver.primary_handle)


@step('I open the url "([^"]*)?"')
def open_url(context, url):
    context.behave_driver.open_url(url)


@step('I open the site "([^"]*)?"')
def open_site(context, url):
    base_url = getattr(context, 'base_url', 'http://localhost:8000')
    destination = urljoin(base_url, url)
    context.behave_driver.open_url(destination)


@given('the base url is "([^"]*)?"')
def set_base_url(context, url):
    if url.endswith('/'):
        url = url[:-1]
    context.base_url = url


@given('I pause for (\d+)*ms')
def pause(context, milliseconds):
    milliseconds = int(milliseconds)
    context.behave_driver.pause(milliseconds)


@given('I have a screen that is ([\d]+) by ([\d]+) pixels')
def set_screen_size(context, x, y):
    context.behave_driver.screen_size = (x, y)


@given('I have a screen that is ([\d]+) pixels (broad|tall)')
def set_screen_dimension(context, size, how):
    size = int(size)
    if how == 'tall':
        context.behave_driver.screen_size = (None, size)
    else:
        context.behave_driver.screen_size = (size, None)


use_step_matcher('parse')
