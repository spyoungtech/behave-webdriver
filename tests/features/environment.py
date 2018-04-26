from os import getcwd
from os.path import abspath, join
from sys import version_info
from behave_webdriver import before_all_factory
from behave_webdriver.driver import Chrome, ChromeOptions
from functools import partial


def get_driver_args(context, Driver):
    args = []
    kwargs = {'default_wait': 5}
    if Driver == Chrome.headless:
        opts = ChromeOptions()
        opts.add_argument('--no-sandbox')  # for travis build
        kwargs['chrome_options'] = opts
        pwd_chrome_path = abspath(join(getcwd(), 'chromedriver'))
        if version_info[0] < 3:
            ex_path = pwd_chrome_path
        else:
            from shutil import which
            ex_path = which('chromedriver') or pwd_chrome_path
        kwargs['executable_path'] = ex_path
    context.BehaveDriver = partial(Driver, **kwargs)
    return (args, kwargs)


before_all = before_all_factory(webdriver_args=get_driver_args, default_driver=Chrome.headless)


def before_feature(context, feature):
    if "fresh_driver" in feature.tags:
        context.behave_driver.quit()
        context.behave_driver = context.BehaveDriver()
        context.behave_driver.default_wait = 5
