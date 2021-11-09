import os
import sys
import shutil
from os import getcwd
from os.path import abspath, join
from sys import version_info
from behave_webdriver import before_all_factory, use_fixture_tag
from behave_webdriver.driver import Chrome, ChromeOptions
from functools import partial
from behave_webdriver.fixtures import transformation_fixture, fixture_browser
from behave_webdriver.transformers import FormatTransformer
from behave.fixture import use_fixture
import behave_webdriver


def get_driver(**kwargs):
    args = []
    kwargs.setdefault('default_wait', 5)
    Driver = behave_webdriver.utils._from_env(default_driver='Chrome')
    if Driver == behave_webdriver.Chrome:
        opts = ChromeOptions()
        opts.add_argument('--no-sandbox')  # for travis build
        kwargs['chrome_options'] = opts

    pwd_driver_path = os.path.abspath(os.path.join(os.getcwd(), Driver._driver_name))
    if sys.version_info[0] < 3:
        ex_path = pwd_driver_path
    else:
        ex_path = shutil.which(Driver._driver_name) or pwd_driver_path
    kwargs['executable_path'] = ex_path
    if os.environ.get('BEHAVE_WEBDRIVER_HEADLESS', None) and hasattr(Driver, 'headless'):
        Driver = Driver.headless
    return Driver, kwargs

    #context.behave_driver = context.BehaveDriver()

def before_all(context):
    driver, kwargs = get_driver()
    context.BehaveDriver = partial(driver, **kwargs)
    use_fixture(fixture_browser, context, webdriver=driver, **kwargs)
    use_fixture(transformation_fixture, context, FormatTransformer, BASE_URL='http://localhost:8000', ALT_BASE_URL='http://127.0.0.1:8000')


def before_tag(context, tag):
    use_fixture_tag(context, tag)


def before_feature(context, feature):
    if "skip_safari" in feature.tags and os.environ.get("BEHAVE_WEBDRIVER", '').lower() == 'safari':
        feature.skip()
        return
    if "fresh_driver" in feature.tags:
        context.behave_driver.quit()
        context.behave_driver = context.BehaveDriver()
        context.behave_driver.default_wait = 5


def before_scenario(context, scenario):
    if "skip_firefox" in scenario.effective_tags and os.environ.get("BEHAVE_WEBDRIVER", '').lower() == 'firefox':
        scenario.skip("Skipping because @skip_firefox tag (usually this is because of a known-issue with firefox)")
        return
    if "skip_safari" in scenario.effective_tags and os.environ.get("BEHAVE_WEBDRIVER", '').lower() == 'safari':
        scenario.skip("Skipping because safari has issues we're not dealing with right now")
        return
