import os
from selenium import webdriver


from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains
import time

from behave_webdriver import BehaveDriver

def before_all(context):
    context.behave_driver = BehaveDriver.headless_chrome()

def after_all(context):
    context.behave_driver.quit()