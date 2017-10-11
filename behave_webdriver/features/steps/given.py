from behave import *
from behave_webdriver import utils

@given('I open the url "{url}"')
def open_url(context, url):
    pass


@given('the element "{selector}" is visible')
def element_visible(context, selector):
    pass


@given('the element "{selector}" is not visible')
def element_not_visible(context, selector):
    pass


@given('the element "([^"]*)?" is( not)* enabled$/')
def step_impl(context, selector, negative):
    pass


@given('the element "([^"]*)?" is( not)* selected$/')
def step_impl(context, selector, negative):
    pass


@given('the checkbox "([^"]*)?" is( not)* checked$/')
def step_impl(context, selector, negative):
    pass


@given('there is (an|no) element "([^"]*)?" on the page$/')
def step_impl(context, an_no, selector):
    pass


@given('the title is( not)* "([^"]*)?"$/')
def step_impl(context, negative, value):
    pass


@given('the element "([^"]*)?" contains( not)* the same text as element "([^"]*)?"$/')
def step_impl(context, first_selector, negative, second_selector):
    pass


@given('the element "([^"]*)?"( not)* matches the text "([^"]*)?"$/')
def step_impl(context, selector, negative, text):
    pass


@given('the element "([^"]*)?"( not)* contains the text "([^"]*)?"$/')
def step_impl(context, selector, negative, text):
    pass


@given('the element "([^"]*)?"( not)* contains any text$/')
def step_impl(context, selector, negative):
    pass


@given('the element "([^"]*)?" is( not)* empty$/')
def step_impl(context, selector, negative):
    pass


@given('the page url is( not)* "([^"]*)?"$/')
def step_impl(context, negative, value):
    pass


@given('the( css)* attribute "([^"]*)?" from element "([^"]*)?" is( not)* "([^"]*)?"$/')
def step_impl(context, is_css, attr, selector, negative, value):
    pass


@given('the cookie "([^"]*)?" contains( not)* the value "([^"]*)?"$/')
def step_impl(context, cookie_key, negative, value):
    pass


@given('the cookie "([^"]*)?" does( not)* exist$/')
def step_impl(context, cookie_key, negative):
    pass


@given('the element "([^"]*)?" is( not)* ([\d]+)px (broad|tall)$/')
def step_impl(context, selector, negative, pixels, axis):
    pass


@given('the element "([^"]*)?" is( not)* positioned at ([\d]+)px on the (x|y) axis$/')
def step_impl(context, selector, negative, pos, axis):
    pass


@given('I have a screen that is ([\d]+) by ([\d]+) pixels$/')
def step_impl(context, x, y):
    pass


@given('I have closed all but the first (window|tab)$/')
def step_impl(context, window_or_tab):
    pass


@given('a (alertbox|confirmbox|prompt) is( not)* opened$/')
def step_impl(context, modal, negative):
    pass
