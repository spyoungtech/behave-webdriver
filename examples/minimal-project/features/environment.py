from behave_webdriver import Chrome

def before_all(context):
    context.behave_driver = Chrome()

def after_all(context):
    context.behave_driver.quit()
