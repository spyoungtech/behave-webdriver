import os
from behave_webdriver import BehaveDriver

def before_all(context):
    browser_env = os.getenv('BEHAVE_WEBDRIVER', 'headless_chrome').lower()
    driver = getattr(BehaveDriver, browser_env, BehaveDriver.headless_chrome)
    context.behave_driver = driver()
    print("DRIVER: {}".format(context.behave_driver.name))
def after_all(context):
    context.behave_driver.quit()