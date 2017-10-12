from behave import *

use_step_matcher('re')
@then('I expect that the title is( not)* "([^"]*)?"')
def step_impl(context, negative, title):
    raise NotImplementedError('step not implemented')


@then('I expect that element "([^"]*)?" is( not)* visible')
def step_impl(context, element, negative):
    raise NotImplementedError('step not implemented')


@then('I expect that element "([^"]*)?" becomes( not)* visible')
def step_impl(context, element, negative):
    raise NotImplementedError('step not implemented')


@then('I expect that element "([^"]*)?" is( not)* within the viewport')
def step_impl(context, element, negative):
    raise NotImplementedError('step not implemented')


@then('I expect that element "([^"]*)?" does( not)* exist')
def step_impl(context, element, negative):
    raise NotImplementedError('step not implemented')


@then('I expect that element "([^"]*)?"( not)* contains the same text as element "([^"]*)?"')
def step_impl(context, first_element, negative, second_element):
    raise NotImplementedError('step not implemented')


@then('I expect that element "([^"]*)?"( not)* matches the text "([^"]*)?"')
def step_impl(context, element, negative, text):
    raise NotImplementedError('step not implemented')


@then('I expect that element "([^"]*)?"( not)* contains the text "([^"]*)?"')
def step_impl(context, element, negative, text):
    raise NotImplementedError('step not implemented')


@then('I expect that element "([^"]*)?"( not)* contains any text')
def step_impl(context, element, negative):
    raise NotImplementedError('step not implemented')


@then('I expect that element "([^"]*)?" is( not)* empty')
def step_impl(context, element, negative):
    raise NotImplementedError('step not implemented')


@then('I expect that the url is( not)* "([^"]*)?"')
def step_impl(context, negative, value):
    current_url = context.behave_driver.current_url
    if negative:
        assert current_url != value
    else:
        assert current_url == value




@then('I expect that the path is( not)* "([^"]*)?"')
def step_impl(context, negative, value):
    raise NotImplementedError('step not implemented')


@then('I expect the url to( not)* contain "([^"]*)?"')
def step_impl(context, negative, value):
    raise NotImplementedError('step not implemented')


@then('I expect that the( css)* attribute "([^"]*)?" from element "([^"]*)?" is( not)* "([^"]*)?"')
def step_impl(context, is_css, attr, element, negative, value):
    raise NotImplementedError('step not implemented')


@then('I expect that checkbox "([^"]*)?" is( not)* checked')
def step_impl(context, element, negative):
    raise NotImplementedError('step not implemented')


@then('I expect that element "([^"]*)?" is( not)* selected')
def step_impl(context, element, negative):
    raise NotImplementedError('step not implemented')


@then('I expect that element "([^"]*)?" is( not)* enabled')
def step_impl(context, element, negative):
    raise NotImplementedError('step not implemented')


@then('I expect that cookie "([^"]*)?"( not)* contains "([^"]*)?"')
def step_impl(context, element, negative, value):
    raise NotImplementedError('step not implemented')


@then('I expect that cookie "([^"]*)?"( not)* exists')
def step_impl(context, cookie_key, negative):
    raise NotImplementedError('step not implemented')


@then('I expect that element "([^"]*)?" is( not)* ([\d]+)px (broad|tall)')
def step_impl(context, element, negative, pixels, axis):
    raise NotImplementedError('step not implemented')


@then('I expect that element "([^"]*)?" is( not)* positioned at ([\d]+)px on the (x|y) axis')
def step_impl(context, element, negative, pos, axis):
    raise NotImplementedError('step not implemented')


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
def step_impl(context, element, miliseconds, negative, condition):
    raise NotImplementedError('step not implemented')


@then('I expect that a (alertbox|confirmbox|prompt) is( not)* opened')
def step_impl(context, modal, negative):
    raise NotImplementedError('step not implemented')


@then('I expect that a (alertbox|confirmbox|prompt)( not)* contains the text "([^"]*)?"')
def step_impl(context, modal, negative, text):
    raise NotImplementedError('step not implemented')

