"""
Provides fixtures to initialize the web driver.
"""

from behave import fixture, use_fixture
from behave_webdriver.utils import _from_string, _from_env
from behave_webdriver.driver import BehaveDriverMixin


@fixture
def fixture_browser(context, *args, **kwargs):
    """
    webdriver setup fixture for behave context; sets ``context.behave_driver``.

    Will destroy the driver at the end of this fixture usage.

    :param webdriver: the webdriver to use -- can be a string (e.g. ``"Chrome"``) or a webdriver class. If omitted, will attempt to use the BEHAVE_WEBDRIVER environment variable

    :param default_driver: a fallback driver if webdriver keyword is not provided AND the BEHAVE_WEBDRIVER environment variable is not set. Defaults to 'Chrome.headless'

    :param args: arguments that will be passed as is to the webdriver.
    :param kwargs: keywords arguments that will be passed as is to the webdriver.

    Basic usage:

    >>> from behave import use_fixture
    >>> from behave_webdriver.fixtures import fixture_browser
    >>> def before_all(context):
    ...     use_fixture(fixture_browser, context, webdriver='firefox')

    You may also provide webdriver class. Just be sure it inherits (or otherwise has method from) BehaveDriverMixin

    >>> from behave import use_fixture
    >>> from behave_webdriver.fixtures import fixture_browser
    >>> from behave_webdriver.driver import BehaveDriverMixin
    >>> from selenium.webdriver import Firefox
    >>> class FirefoxDriver(BehaveDriverMixin, Firefox):
    ...     pass
    >>> def before_all(context):
    ...     use_fixture(fixture_browser, context, webdriver=FirefoxDriver)

    positional arguments and additional keyword arguments are passed to the webdriver init:

    >>> from behave import use_fixture
    >>> from behave_webdriver.fixtures import fixture_browser
    >>> from behave_webdriver.driver import ChromeOptions
    >>> def before_all(context):
    ...     options = ChromeOptions()
    ...     options.add_argument('--ignore-gpu-blacklist')
    ...     use_fixture(fixture_browser, context, webdriver='chrome', options=options)

    If the ``webdriver`` keyword is omitted, will attampt to get the driver from BEHAVE_WEBDRIVER or will use headless chrome as a final fallback if environment is not set and there is no ``default_driver`` specified

    >>> from behave import use_fixture
    >>> from behave_webdriver.fixtures import fixture_browser
    >>> def before_all(context):
    ...     #  try to use driver from BEHAVE_WEBDRIVER environment variable; use firefox as a fallback when env not set
    ...     use_fixture(fixture_browser, context, default_driver='firefox')

    """

    webdriver = kwargs.pop('webdriver', None)
    default_driver = kwargs.pop('default_driver', 'Chrome.headless')
    if isinstance(webdriver, str):
        webdriver = _from_string(webdriver)
    if webdriver is None:
        webdriver = _from_env(default_driver=default_driver)

    context.behave_driver = webdriver(*args, **kwargs)
    yield context.behave_driver
    context.behave_driver.quit()
    del context.behave_driver


def before_all_factory(*args, **kwargs):
    """
    Create and return a ``before_all`` function that use the ``fixture_browser`` fixture with the corresponding arguments
    :param args: positional arguments of ``fixture_browser``
    :param kwargs: keywords arguments of ``fixture_browser``

    >>> from behave_webdriver.fixtures import before_all_factory
    >>> before_all = before_all_factory(webdriver='firefox')
    """
    def before_all(context):
        use_fixture(fixture_browser, context, *args, **kwargs)
    return before_all


def before_feature_factory(*args, **kwargs):
    """
    Create and return a ``before_feature` function that use the ``fixture_browser`` fixture with the corresponding arguments
    :param args: positional arguments of ``fixture_browser``
    :param kwargs: keywords arguments of ``fixture_browser``

    >>> from behave_webdriver.fixtures import before_feature_factory
    >>> before_feature = before_feature_factory(webdriver='firefox')
    """
    def before_feature(context, feature):
        use_fixture(fixture_browser, context, *args, **kwargs)
    return before_feature


def before_scenario_factory(*args, **kwargs):
    """
    Create and return a ``before_scenario`` function that use the ``fixture_browser`` fixture with the corresponding arguments
    :param args: positional arguments of ``fixture_browser``
    :param kwargs: keywords arguments of ``fixture_browser``

    >>> from behave_webdriver.fixtures import before_scenario_factory
    >>> before_scenario = before_scenario_factory(webdriver='firefox')
    """
    def before_scenario(context, scenario):
        use_fixture(fixture_browser, context, *args, **kwargs)
    return before_scenario
