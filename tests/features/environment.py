import os
import sys
import shutil
import behave_webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from functools import partial

def before_all(context):
    kwargs = {}

    Driver = behave_webdriver._from_env(default_driver=behave_webdriver.Chrome.headless)
    if Driver == behave_webdriver.Chrome.headless:
        opts = ChromeOptions()
        opts.add_argument('--no-sandbox')  # for travis build
        kwargs['chrome_options'] = opts
        pwd_chrome_path = os.path.abspath(os.path.join(os.getcwd(), 'chromedriver'))
        if sys.version_info[0] < 3:
            ex_path = pwd_chrome_path
        else:
            ex_path = shutil.which('chromedriver') or pwd_chrome_path
        kwargs['executable_path'] = ex_path
    context.BehaveDriver = partial(Driver, **kwargs)
    context.behave_driver = context.BehaveDriver()
    context.behave_driver.default_wait = 5

def after_all(context):
    context.behave_driver.quit()


def before_feature(context, feature):
    if "fresh_driver" in feature.tags:
        context.behave_driver.quit()
        context.behave_driver = context.BehaveDriver()
        context.behave_driver.default_wait = 5
