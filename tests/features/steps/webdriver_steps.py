from behave import *
from behave_webdriver.steps import *

use_step_matcher('re')

@then("""I expect that executing the step '([^']*)?' raises an exception""")
def test_step_raises_exception(context, step_text):
    try:
        context.execute_steps(step_text)
    except Exception as e:
        print(e)
    else:
        raise AssertionError('Step did not raise exception')
