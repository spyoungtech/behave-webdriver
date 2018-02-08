import os
from behave_webdriver import BehaveDriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium import webdriver
from functools import partial


def before_all(context):
    browser_env = os.getenv('BEHAVE_WEBDRIVER', 'headless_chrome').lower()
    Driver = getattr(BehaveDriver, browser_env, BehaveDriver.headless_chrome)
    opts = ChromeOptions()
    opts.add_argument('log-level=3')
    context._BehaveDriver = partial(Driver, chrome_options=opts)
    context.behave_driver = context._BehaveDriver()
    context.behave_driver.default_wait = 5

def after_all(context):
    context.behave_driver.quit()


def before_feature(context, feature):
    if "fresh_driver" in feature.tags:
        context.behave_driver.quit()
        context.behave_driver = context._BehaveDriver()
        context.behave_driver.default_wait = 5
