from behave_webdriver import BehaveDriver

def before_all(context):
    context.behave_driver = BehaveDriver.headless_chrome()
def after_all(context):
    context.behave_driver.quit()
