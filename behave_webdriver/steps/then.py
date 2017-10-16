from behave import *
try:
    from urllib.parse import urlparse
except ImportError:
    from urlparse import urlparse

use_step_matcher('re')
@then('I expect that the title is( not)* "([^"]*)?"')
def step_impl(context, negative, title):
    if negative:
        assert title != context.behave_driver.title
    else:
        assert title == context.behave_driver.title


@then('I expect that element "([^"]*)?" is( not)* visible')
def step_impl(context, element, negative):
    element_is_visible = context.behave_driver.element_visible(element)
    if negative:
        assert not element_is_visible
    else:
        assert element_is_visible


@then('I expect that element "([^"]*)?" becomes( not)* visible')
def step_impl(context, element, negative):
    element_is_visible = context.behave_driver.element_visible(element)
    if negative:
        assert not element_is_visible
    else:
        assert element_is_visible


@then('I expect that element "([^"]*)?" is( not)* within the viewport')
def step_impl(context, element, negative):
    element_is_visible = context.behave_driver.element_visible(element)
    if negative:
        assert not element_is_visible
    else:
        assert element_is_visible


@then('I expect that element "([^"]*)?" does( not)* exist')
def step_impl(context, element, negative):
    element_exists = context.behave_driver.element_exists(element)
    if negative:
        assert not element_exists
    else:
        assert element_exists


@then('I expect that element "([^"]*)?"( not)* contains the same text as element "([^"]*)?"')
def step_impl(context, first_element, negative, second_element):
    first_elem_text = context.behave_driver.get_element_text(first_element)
    second_elem_text = context.behave_driver.get_element_text(second_element)
    same =  first_elem_text == second_elem_text
    if negative:
        assert not same
    else:
        assert same

@then('I expect that element "([^"]*)?"( not)* matches the text "([^"]*)?"')
def step_impl(context, element, negative, text):
    matches = context.behave_driver.get_element_text(element) == text
    if negative:
        assert not matches
    else:
        assert matches


@then('I expect that element "([^"]*)?"( not)* contains the text "([^"]*)?"')
def step_impl(context, element, negative, text):
    contains = context.behave_driver.element_contains(element, text)
    if negative:
        assert not contains
    else:
        assert contains

@then('I expect that element "([^"]*)?"( not)* contains any text')
def step_impl(context, element, negative):
    any_text = bool(context.behave_driver.get_element_text(element))
    if negative:
        assert not any_text
    else:
        assert any_text


@then('I expect that element "([^"]*)?" is( not)* empty')
def step_impl(context, element, negative):
    any_text = bool(context.behave_driver.get_element_text(element))
    if negative:
        assert not any_text
    else:
        assert any_text


@then('I expect that the url is( not)* "([^"]*)?"')
def step_impl(context, negative, value):
    current_url = context.behave_driver.current_url
    if negative:
        assert current_url != value
    else:
        assert current_url == value



@then('I expect that the path is( not)* "([^"]*)?"')
def step_impl(context, negative, value):
    current_url = context.behave_driver.current_url
    path = urlparse(current_url).path
    if negative:
        assert path != value
    else:
        assert path == value


@then('I expect the url to( not)* contain "([^"]*)?"')
def step_impl(context, negative, value):
    current_url = context.behave_driver.current_url
    if negative:
        assert value not in current_url
    else:
        assert value in current_url


@then('I expect that the( css)* attribute "([^"]*)?" from element "([^"]*)?" is( not)* "([^"]*)?"')
def step_impl(context, is_css, attr, element, negative, value):
    attribute_value = context.behave_driver.get_element_attribute(element, attr, is_css)
    if negative:
        assert attribute_value != value
    else:
        assert attribute_value == value


@then('I expect that checkbox "([^"]*)?" is( not)* checked')
def step_impl(context, element, negative):
    # should this check that the element is, in fact, a checkbox?
    checked = context.behave_driver.element_selected(element)
    if negative:
        assert not checked
    else:
        assert checked


@then('I expect that element "([^"]*)?" is( not)* selected')
def step_impl(context, element, negative):
    selected = context.behave_driver.element_selected(element)
    if negative:
        assert not selected
    else:
        assert selected


@then('I expect that element "([^"]*)?" is( not)* enabled')
def step_impl(context, element, negative):
    enabled = context.behave_driver.element_enabled(element)
    if negative:
        assert not enabled
    else:
        assert enabled


@then('I expect that cookie "([^"]*)?"( not)* contains "([^"]*)?"')
def step_impl(context, cookie_key, negative, value):
    cookie = context.behave_driver.get_cookie(cookie_key)
    cookie_value = cookie.get('value')
    if negative:
        assert cookie_value != value
    else:
        assert cookie_value == value


@then('I expect that cookie "([^"]*)?"( not)* exists')
def step_impl(context, cookie_key, negative):
    cookie = context.behave_driver.get_cookie(cookie_key)
    if negative:
        assert cookie is None, u'Cookie was present: {}'.format(cookie)
    else:
        assert cookie is not None


@then('I expect that element "([^"]*)?" is( not)* ([\d]+)px (broad|tall)')
def step_impl(context, element, negative, pixels, how):
    elem_size = context.behave_driver.get_element_size(element)
    if how == 'tall':
        axis = 'height'
    else:
        axis = 'width'
    if negative:
        assert elem_size[axis] != int(pixels)
    else:
        assert elem_size[axis] == int(pixels)


@then('I expect that element "([^"]*)?" is( not)* positioned at ([\d]+)px on the (x|y) axis')
def step_impl(context, element, negative, pos, axis):
    element_position = context.behave_driver.get_element_location(element)
    if negative:
        assert element_position[axis] != int(pos)
    else:
        assert element_position[axis] == int(pos)


@then('I expect that element "([^"]*)?" (has|does not have) the class "([^"]*)?"')
def step_impl(context, element, has, classname):
    raise NotImplementedError('step not implemented')


@then('I expect a new (window|tab) has( not)* been opened')
def step_impl(context, window_or_tab, negative):
    raise NotImplementedError('step not implemented')


@then('I expect the url "([^"]*)?" is opened in a new (tab|window)')
def step_impl(context, url, tab_or_window):
    raise NotImplementedError('step not implemented')


@then('I expect that element "([^"]*)?" is( not)* focused')
def step_impl(context, element, negative):
    raise NotImplementedError('step not implemented')


@then('I wait on element "([^"]*)?"(?: for (\d+)ms)*(?: to( not)* (be checked|be enabled|be selected|be visible|contain a text|contain a value|exist))*')
def step_impl(context, element, milliseconds, negative, condition):
    if milliseconds:
        digits = ''.join(char for char in milliseconds if char.isdigit())
        milliseconds = int(digits)
    else:
        milliseconds = 5000 # default wait time
    result = context.behave_driver.wait_for_element_condition(element, milliseconds, condition)
    if negative:
        assert not result
    else:
        assert result


@then('I expect that a (alertbox|confirmbox|prompt) is( not)* opened')
def step_impl(context, modal, negative):
    if negative:
        assert context.behave_driver.has_alert is False
    else:
        assert context.behave_driver.has_alert is True


@then('I expect that a (alertbox|confirmbox|prompt)( not)* contains the text "([^"]*)?"')
def step_impl(context, modal, negative, text):
    raise NotImplementedError('step not implemented')

use_step_matcher('parse')