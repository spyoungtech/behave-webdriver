import os
from behave_webdriver import BehaveDriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium import webdriver


def before_all(context):
    browser_env = os.getenv('BEHAVE_WEBDRIVER', 'headless_chrome').lower()
    Driver = getattr(BehaveDriver, browser_env, BehaveDriver.headless_chrome)
    opts = ChromeOptions()
    opts.add_argument('log-level=3')
    context.behave_driver = Driver(chrome_options=opts, default_wait=5)

def after_all(context):
    context.behave_driver.quit()