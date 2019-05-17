from behave import *
from behave_webdriver.transformers import matcher_mapping
try:
    from urllib.parse import urljoin
except ImportError:
    from urlparse import urljoin  # Python 2


if 'transform-parse' not in matcher_mapping:
    use_step_matcher('re')
else:
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
