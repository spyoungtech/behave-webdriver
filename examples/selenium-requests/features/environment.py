from selenium import webdriver
from behave_webdriver.driver import BehaveDriverMixin
from seleniumrequests import RequestMixin

class BehaveRequestDriver(BehaveDriverMixin, RequestMixin, webdriver.Chrome):
    pass

def before_all(context):
    context.behave_driver = BehaveRequestDriver()

def after_all(context):
    context.behave_driver.quit()
