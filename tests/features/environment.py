import os
import sys
import shutil
import behave_webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from functools import partial

def before_all(context):
    kwargs = {'default_wait': 5}

    Driver = behave_webdriver._from_env()
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
    context.BehaveDriver = partial(Driver, **kwargs)
    context.behave_driver = context.BehaveDriver()

def after_all(context):
    context.behave_driver.quit()


def before_feature(context, feature):
    if "fresh_driver" in feature.tags:
        context.behave_driver.quit()
        context.behave_driver = context.BehaveDriver()
        context.behave_driver.default_wait = 5

def before_scenario(context, scenario):
    if "skip_firefox" in scenario.effective_tags:
        scenario.skip("Skipping because @skip_firefox tag (usually this is because of a known-issue with firefox)")
        return