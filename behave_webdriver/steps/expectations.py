from behave import *
from behave_webdriver.transformers import matcher_mapping
try:
    from urllib.parse import urlparse
except ImportError:
    from urlparse import urlparse

if 'transform-parse' not in matcher_mapping:
    use_step_matcher('re')
else:
    use_step_matcher('transform-re')


@given('the element "([^"]*)?" is( not)* visible')
@then('I expect that element "([^"]*)?" becomes( not)* visible')
@then('I expect that element "([^"]*)?" is( not)* visible')
def check_element_visibility(context, element, negative):
    element_is_visible = context.behave_driver.element_visible(element)
    if negative:
        assert not element_is_visible, 'Expected element to not be visible, but it was'
    else:
        assert element_is_visible, 'Expected element to be visible, but it was not visible'


@given('the title is( not)* "([^"]*)?"')
@then('I expect that the title is( not)* "([^"]*)?"')
def title(context, negative, value):
    if negative:
        assert context.behave_driver.title != value, 'Title was "{}"'.format(context.behave_driver.title)
    else:
        assert context.behave_driver.title == value, 'Title was "{}"'.format(context.behave_driver.title)


@then('I expect that element "([^"]*)?" is( not)* within the viewport')
def check_element_within_viewport(context, element, negative):
    element_in_viewport = context.behave_driver.element_in_viewport(element)
    if negative:
        assert not element_in_viewport, 'Element was completely within the viewport'
    else:
        assert element_in_viewport, 'Element was not completely within viewport'


@given('the element "([^"]*)?" is( not)* enabled')
@then('I expect that element "([^"]*)?" is( not)* enabled')
def element_enabled(context, element, negative):
    enabled = context.behave_driver.element_enabled(element)
    if negative:
        assert not enabled
    else:
        assert enabled


@given('the element "([^"]*)?" is( not)* selected')
@then('I expect that element "([^"]*)?" is( not)* selected')
def element_selected(context, element, negative):
    selected = context.behave_driver.element_selected(element)
    if negative:
        assert not selected
    else:
        assert selected


@given('the checkbox "([^"]*)?" is( not)* checked')
@then('I expect that checkbox "([^"]*)?" is( not)* checked')
def element_checked(context, element, negative):
    checked = context.behave_driver.element_selected(element)
    if negative:
        assert not checked
    else:
        assert checked


@given('there is (an|no) element "([^"]*)?" on the page')
def element_exists(context, an_no, element):
    negative = an_no == 'no'
    exists = context.behave_driver.element_exists(element)
    if negative:
        assert not exists
    else:
        assert exists


@then('I expect that element "([^"]*)?" does( not)* exist')
def check_element_exists(context, element, negative):
    exists = context.behave_driver.element_exists(element)
    if negative:
        assert not exists, 'Expected the element does not exist, but element "{}" was located'.format(element)
    else:
        assert exists, 'Expected element to exist, but no element "{}" was located'.format(element)


@given('the element "([^"]*)?" contains( not)* the same text as element "([^"]*)?"')
@then('I expect that element "([^"]*)?"( not)* contains the same text as element "([^"]*)?"')
def elements_same_text(context, first_element, negative, second_element):
    first_elem_text = context.behave_driver.get_element_text(first_element)
    second_elem_text = context.behave_driver.get_element_text(second_element)
    same = first_elem_text == second_elem_text
    if negative:
        assert not same, 'Element "{}" text "{}" is same as element "{}"'.format(first_element,
                                                                                 first_elem_text,
                                                                                 second_element)
    else:
        assert same, 'Element "{}" text "{}" is not same as element "{}" text "{}"'.format(first_element,
                                                                                           first_elem_text,
                                                                                           second_element,
                                                                                           second_elem_text)


@given('the element "([^"]*)?"( not)* matches the text "([^"]*)?"')
@then('I expect that element "([^"]*)?"( not)* matches the text "([^"]*)?"')
def element_matches_text(context, element, negative, text):
    elem_text = context.behave_driver.get_element_text(element)
    matches = elem_text == text
    if negative:
        assert not matches, 'Element "{}" text matches "{}"'.format(element,
                                                                    text)
    else:
        assert matches, 'The text "{}" did not match the element text "{}"'.format(text, elem_text)


@given('the element "([^"]*)?"( not)* contains the text "([^"]*)?"')
@then('I expect that element "([^"]*)?"( not)* contains the text "([^"]*)?"')
def check_element_contains_text(context, element, negative, text):
    contains = context.behave_driver.element_contains(element, text)
    if negative:
        assert not contains, 'Element text does contain "{}"'.format(text)
    else:
        assert contains, 'Element text does not contain "{}"'.format(text)


@given('the element "([^"]*)?"( not)* contains any text')
@then('I expect that element "([^"]*)?"( not)* contains any text')
def element_any_text(context, element, negative):
    any_text = bool(context.behave_driver.get_element_text(element))
    if negative:
        assert not any_text
    else:
        assert any_text


@given('the element "([^"]*)?" is( not)* empty')
@then('I expect that element "([^"]*)?" is( not)* empty')
def check_element_empty(context, element, negative):
    elem_text = context.behave_driver.get_element_text(element)
    any_text = bool(elem_text)
    if negative:
        assert any_text is True
    else:
        assert any_text is False


@given('the page url is( not)* "([^"]*)?"')
@then('I expect that the url is( not)* "([^"]*)?"')
def check_url(context, negative, value):
    current_url = context.behave_driver.current_url
    if negative:
        assert current_url != value, 'The url was "{}"'.format(current_url)
    else:
        assert current_url == value, 'Expected url to be "{}", but saw the url was "{}"'.format(value, current_url)


@then('I expect the url to( not)* contain "([^"]*)?"')
def check_url_contains(context, negative, value):
    current_url = context.behave_driver.current_url
    if negative:
        assert value not in current_url, 'url was "{}"'.format(current_url)
    else:
        assert value in current_url, 'url was "{}"'.format(current_url)


@given('the( css)* attribute "([^"]*)?" from element "([^"]*)?" is( not)* "([^"]*)?"')
@then('I expect that the( css)* attribute "([^"]*)?" from element "([^"]*)?" is( not)* "([^"]*)?"')
def check_element_attribute(context, is_css, attr, element, negative, value):
    if is_css:
        attribute_value, value = context.behave_driver.get_element_attribute(element, attr, is_css, value)
    else:
        attribute_value = context.behave_driver.get_element_attribute(element, attr)

    if negative:
        assert attribute_value != value, 'Attribute value was "{}"'.format(attribute_value)
    else:
        assert attribute_value == value, 'Attribute value was "{}"'.format(attribute_value)


@given('the cookie "([^"]*)?" contains( not)* the value "([^"]*)?"')
@then('I expect that cookie "([^"]*)?"( not)* contains "([^"]*)?"')
def check_cookie_value(context, cookie_key, negative, value):
    cookie = context.behave_driver.get_cookie(cookie_key)
    cookie_value = cookie.get('value')
    if negative:
        assert cookie_value != value, 'Cookie value was "{}"'.format(cookie_value)
    else:
        assert cookie_value == value, 'Cookie value was "{}"'.format(cookie_value)


@given('the cookie "([^"]*)?" does( not)* exist')
def cookie_exists(context, cookie_key, negative):
    cookie = context.behave_driver.get_cookie(cookie_key)
    if negative:
        assert cookie is None, 'Cookie exists: {}'.format(cookie)
    else:
        assert cookie is not None


@then('I expect that cookie "([^"]*)?"( not)* exists')
def check_cookie_exists(context, cookie_key, negative):
    cookie = context.behave_driver.get_cookie(cookie_key)
    if negative:
        assert cookie is None, u'Cookie was present: "{}"'.format(cookie)
    else:
        assert cookie is not None, 'Cookie was not found'


@given('the element "([^"]*)?" is( not)* ([\d]+)px (broad|tall)')
@then('I expect that element "([^"]*)?" is( not)* ([\d]+)px (broad|tall)')
def check_element_size(context, element, negative, pixels, how):
    elem_size = context.behave_driver.get_element_size(element)
    if how == 'tall':
        axis = 'height'
    else:
        axis = 'width'
    if negative:
        assert elem_size[axis] != int(pixels), 'Element size was "{}"'.format(elem_size)
    else:
        assert elem_size[axis] == int(pixels), 'Element size was "{}"'.format(elem_size)


@given('the element "([^"]*)?" is( not)* positioned at ([\d]+)px on the (x|y) axis')
@then('I expect that element "([^"]*)?" is( not)* positioned at ([\d]+)px on the (x|y) axis')
def check_element_position(context, element, negative, pos, axis):
    element_position = context.behave_driver.get_element_location(element)
    if negative:
        assert element_position[axis] != int(pos), 'Position was {} on the {} axis'.format(element_position[axis], axis)
    else:
        assert element_position[axis] == int(pos), 'Position was {} on the {} axis'.format(element_position[axis], axis)


@given('a (alertbox|confirmbox|prompt) is( not)* opened')
@then('I expect that a (alertbox|confirmbox|prompt) is( not)* opened')
def check_modal(context, modal, negative):
    if negative:
        assert context.behave_driver.has_alert is False
    else:
        assert context.behave_driver.has_alert is True


@then('I expect that the path is( not)* "([^"]*)?"')
def check_path(context, negative, value):
    current_url = context.behave_driver.current_url
    path = urlparse(current_url).path
    if negative:
        assert path != value, 'The path was "{}"'.format(path)
    else:
        assert path == value, 'Expected the path to be "{}", but saw the path "{}"'.format(value, path)


@then('I expect that element "([^"]*)?" (has|does not have) the class "([^"]*)?"')
def check_element_has_class(context, element, has, classname):
    if 'not' in has:
        negative = True
    else:
        negative = False

    has_class = context.behave_driver.element_has_class(element, classname)
    if negative:
        assert not has_class, 'Classes were {}'.format(context.behave_driver.get_element_attribute(element, 'class'))
    else:
        assert has_class, 'Classes were {}'.format(context.behave_driver.get_element_attribute(element, 'class'))


@then('I expect a new (window|tab) has( not)* been opened')
def check_window_opened(context, _, negative):
    if negative:
        assert not context.behave_driver.secondary_handles
    else:
        assert bool(context.behave_driver.secondary_handles)


@then('I expect the url "([^"]*)?" is opened in a new (tab|window)')
def check_url_new_window(context, url, _):
    current_handle = context.behave_driver.primary_handle
    for handle in context.behave_driver.secondary_handles:
        context.behave_driver.switch_to_window(handle)
        if context.behave_driver.current_url == url:
            context.behave_driver.switch_to_window(current_handle)
            break
    else:
        context.behave_driver.switch_to_window(current_handle)
        if len(context.behave_driver.secondary_handles) < 1:
            raise AssertionError('No secondary handles found!')
        raise AssertionError("The url '{}' was not found in any handle")


@then('I expect that element "([^"]*)?" is( not)* focused')
def check_element_focused(context, element, negative):
    element_focused = context.behave_driver.element_focused(element)
    if negative:
        assert not element_focused
    else:
        assert element_focused


@then('I expect that a (alertbox|confirmbox|prompt)( not)* contains the text "([^"]*)?"')
def check_modal_text_contains(context, modal_type, negative, text):
    alert_text = context.behave_driver.alert.text
    if negative:
        assert not text in alert_text
    else:
        assert text in alert_text


@then('I wait on element "([^"]*)?"(?: for (\d+)ms)*(?: to( not)* (be checked|be enabled|be selected|be visible|contain a text|contain a value|exist))*')
def wait_for_element_condition(context, element, milliseconds, negative, condition):
    if milliseconds:
        digits = ''.join(char for char in milliseconds if char.isdigit())
        milliseconds = int(digits)

    result = context.behave_driver.wait_for_element_condition(element, milliseconds, negative, condition)
    if not negative:
        negative = ''
    assert result, 'was expecting element "{element}" to {negative} {condition}, but the result was {result}'.format(
                    element=element,
                    negative=negative,
                    condition=condition,
                    result=result)


@then("I expect the screen is ([\d]+) by ([\d]+) pixels")
def check_screen_size(context, x, y):
    screen_x, screen_y = context.behave_driver.screen_size


use_step_matcher('parse')

