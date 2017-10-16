from behave import *
try:
    from urllib.parse import urljoin
except ImportError:
    from urlparse import urljoin  # Python 2

use_step_matcher('re')


@given('I open the url "([^"]*)?"')
def open_url(context, url):
    context.behave_driver.open_url(url)


@given('I open the site "([^"]*)?"')
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

@given('the element "([^"]*)?" is( not)* visible')
def element_visible(context, element, negative):
    visible = context.behave_driver.element_visible(element)
    if negative:
        assert not visible
    else:
        assert visible


@given('the element "([^"]*)?" is( not)* enabled')
def element_enabled(context, element, negative):
    enabled = context.behave_driver.element_enabled(element)
    if negative:
        assert not enabled
    else:
        assert enabled


@given('the element "([^"]*)?" is( not)* selected')
def element_selected(context, element, negative):
    selected = context.behave_driver.element_selected(element)
    if negative:
        assert not selected
    else:
        assert selected


@given('the checkbox "([^"]*)?" is( not)* checked')
def element_checked(context, element, negative):
    # should this check that the element is, in fact, a checkbox?
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


@given('the title is( not)* "([^"]*)?"')
def title(context, negative, value):
    if negative:
        assert context.behave_driver.title != value
    else:
        assert context.behave_driver.title == value


@given('the element "([^"]*)?" contains( not)* the same text as element "([^"]*)?"')
def elements_same_text(context, first_element, negative, second_element):
    first_elem_text = context.behave_driver.get_element_text(first_element)
    second_elem_text = context.behave_driver.get_element_text(second_element)
    same = first_elem_text == second_elem_text
    if negative:
        assert not same
    else:
        assert same


@given('the element "([^"]*)?"( not)* matches the text "([^"]*)?"')
def element_matches_text(context, element, negative, text):
    matches = context.behave_driver.get_element_text(element) == text
    if negative:
        assert not matches
    else:
        assert matches


@given('the element "([^"]*)?"( not)* contains the text "([^"]*)?"')
def element_contains_text(context, element, negative, text):
    contains = context.behave_driver.element_contains(element, text)
    if negative:
        assert not contains
    else:
        assert contains


@given('the element "([^"]*)?"( not)* contains any text')
def element_any_text(context, element, negative):
    any_text = bool(context.behave_driver.get_element_text(element))
    if negative:
        assert not any_text
    else:
        assert any_text


@given('the element "([^"]*)?" is( not)* empty')
def step_impl(context, element, negative):
    any_text = bool(context.behave_driver.get_element_text(element))
    if negative:
        assert not any_text
    else:
        assert any_text


@given('the page url is( not)* "([^"]*)?"')
def step_impl(context, negative, value):
    page_url = context.behave_driver.current_url
    if negative:
        assert page_url != value
    else:
        assert page_url == value


@given('the( css)* attribute "([^"]*)?" from element "([^"]*)?" is( not)* "([^"]*)?"')
def element_attribute(context, is_css, attr, element, negative, value):
    attribute_value = context.behave_driver.get_element_attribute(element, attr, is_css)
    if negative:
        assert attribute_value != value
    else:
        assert attribute_value == value


@given('the cookie "([^"]*)?" contains( not)* the value "([^"]*)?"')
def step_impl(context, cookie_key, negative, value):
    cookie = context.behave_driver.get_cookie(cookie_key)
    cookie_value = cookie.get('value')
    if negative:
        assert cookie_value != value
    else:
        assert cookie_value == value


@given('the cookie "([^"]*)?" does( not)* exist')
def step_impl(context, cookie_key, negative):
    cookie = context.behave_driver.get_cookie(cookie_key)
    if cookie and negative:
        context.behave_driver.delete_cookie(cookie_key)
    cookie = context.behave_driver.get_cookie(cookie_key)

    if negative:
        assert cookie is None
    else:
        assert cookie is not None


@given('the element "([^"]*)?" is( not)* ([\d]+)px (broad|tall)')
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


@given('the element "([^"]*)?" is( not)* positioned at ([\d]+)px on the (x|y) axis')
def step_impl(context, element, negative, pos, axis):
    element_position = context.behave_driver.get_element_location(element)
    if negative:
        assert element_position[axis] != int(pos)
    else:
        assert element_position[axis] == int(pos)


@given('I have a screen that is ([\d]+) by ([\d]+) pixels')
def step_impl(context, x, y):
    context.behave_driver.screen_size = (x, y)


@given('I have closed all but the first (window|tab)')
def step_impl(context, window_or_tab):
    raise NotImplementedError('step not implemented')


@given('a (alertbox|confirmbox|prompt) is( not)* opened')
def step_impl(context, modal, negative):
    if negative:
        assert context.behave_driver.has_alert is False
    else:
        assert context.behave_driver.has_alert is True

use_step_matcher('parse')
