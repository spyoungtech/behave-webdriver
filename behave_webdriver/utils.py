from os import getenv
import six
from behave_webdriver.driver import (Chrome,
                                     Firefox,
                                     Ie,
                                     Edge,
                                     Opera,
                                     Safari,
                                     BlackBerry,
                                     PhantomJS,
                                     Android,
                                     Remote)


def _from_string(webdriver_string):
    def get_driver_name(driver):
        return driver.__name__.upper()
    drivers = [Chrome, Firefox, Ie, Edge, Opera, Safari, BlackBerry, PhantomJS, Android, Remote]
    driver_map = {get_driver_name(d): d for d in drivers}
    driver_map['CHROME.HEADLESS'] = Chrome.headless
    Driver = driver_map.get(webdriver_string.upper(), None)
    if Driver is None:
        raise ValueError('No such driver "{}". Valid options are: {}'.format(webdriver_string,
                                                                             ', '.join(driver_map.keys())))
    return Driver


def from_string(webdriver_string, *args, **kwargs):
    Driver = _from_string(webdriver_string)
    return Driver(*args, **kwargs)


def _from_env(default_driver=None):
    browser_env = getenv('BEHAVE_WEBDRIVER', default_driver)
    if browser_env is None:
        raise ValueError('No driver found in environment variables and no default driver selection')
    if isinstance(browser_env, six.string_types):
        Driver = _from_string(browser_env)
    else:
        # if not a string, assume we have a webdriver instance
        Driver = browser_env
    return Driver


def from_env(*args, **kwargs):
    default_driver = kwargs.pop('default_driver', None)
    if default_driver is None:
        default_driver = 'Chrome.headless'
    Driver = _from_env(default_driver=default_driver)

    return Driver(*args, **kwargs)
