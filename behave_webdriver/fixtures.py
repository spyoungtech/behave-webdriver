"""
Provides fixtures to initialize the web driver.
"""
from behave import fixture, use_fixture
from behave_webdriver.utils import _from_string, _from_env
from behave_webdriver.driver import BehaveDriverMixin
from functools import partial
from behave_webdriver import transformers
_env_webdriver_name = 'env'


@fixture
def fixture_browser(ctx, *args, **kwargs):
    """
    Provide a web driver browser as `ctx.behave_driver`.
    
    Can raise ValueError in case of bad parameters.

    Will destroy the driver at the end of this fixture usage.

    :param webdriver_name: the name of the webdriver.
                           Special 'env' name is to tell to get the name from `BEHAVE_WEBDRIVER` environment variable.
                           Default to 'env'.
    :param webdriver_class: the class to use instead of using a name. The class must both inherit from
                            - `behave_webdriver.driver.BehaveDriverMixin`
                            - a driver from `selenium.webdriver`
                            or be a subclass of a driver from `behave_webdriver.driver`.
                            Default to None.
    :param webdriver_args: function that takes a context and a `webdriver_class` and returns a tuple of
                           - list of positional arguments
                           - dictionary of keyword arguments
                            Default to None.
    :param default_driver: used for `from_env` method in `webdriver_name` is 'env'.
                           Default to None.
    :param args: arguments that will be passed as is to the driver constructor.
                 They will be added to those from `webdriver_args`.
    :param kwargs: keywords arguments that will be passed as is to the driver constructor.
                   They will be added to those from `webdriver_args`.
    :return: web driver initialized

    Use it like this:

    >>> from behave import use_fixture
    >>> from behave_webdriver import fixture_browser
    >>> def before_all(ctx):
    ...     use_fixture(fixture_browser, ctx)

    It will try to instantiate a `Chrome` driver (the default).

    You can specify it in a environment variable:

    >>> from os import environ
    >>> from behave import use_fixture
    >>> from behave_webdriver import fixture_browser
    >>> def before_all(ctx):
    ...     assert environ['BEHAVE_WEBDRIVER'] == 'firefox'
    ...     use_fixture(fixture_browser, ctx)

    It will try to instantiate a `Firefox` driver.

    You could also provide the name:

    >>> from behave import use_fixture
    >>> from behave_webdriver import fixture_browser
    >>> def before_all(ctx):
    ...     use_fixture(fixture_browser, ctx, webdriver_name='firefox')

    You could direcly provide webdriver class:

    >>> from behave import use_fixture
    >>> from behave_webdriver import fixture_browser
    >>> from behave_webdriver.driver import BehaveDriverMixin
    >>> from selenium.driver import Firefox
    >>> class FirefoxDriver(BehaveDriverMixin, Firefox):
    ...     pass
    >>> def before_all(ctx):
    ...     use_fixture(fixture_browser, ctx, webdriver_class=FirefoxDriver)

    You could pass constructor parameters to the webdriver:

    >>> from behave import use_fixture
    >>> from behave_webdriver import fixture_browser
    >>> from behave_webdriver.driver import ChromeOptions
    >>> def before_all(ctx):
    ...     options = ChromeOptions()
    ...     options.add_argument('--ignore-gpu-blacklist')
    ...     use_fixture(fixture_browser, ctx, webdriver_name='chrome', options=options)

    You could also use a function to pass constructor parameters to the webdriver:

    >>> from behave import use_fixture
    >>> from behave_webdriver import fixture_browser
    >>> from behave_webdriver.driver import Chrome, ChromeOptions
    >>> def get_driver_args(ctx, driver):
    ...     if driver == Chrome:
    ...         options = ChromeOptions()
    ...         options.add_argument('--ignore-gpu-blacklist')
    ...         return ([], {'options': options}
    ...     else:
    ...         return ([], {})
    >>> def before_all(ctx):
    ...     use_fixture(fixture_browser, ctx, webdriver_args=get_driver_args)
    """
    webdriver_name = kwargs.pop('webdriver_name', _env_webdriver_name)
    webdriver_class = kwargs.pop('webdriver_class', None)
    webdriver_args = kwargs.pop('webdriver_args', None)
    if webdriver_class is not None:
        if BehaveDriverMixin not in webdriver_class.mro():
            raise ValueError('The driver "{}" does not inherit from BehaveDriverMixin.'.format(webdriver_class.__name__))
    elif webdriver_name == _env_webdriver_name:
        if 'default_driver' in kwargs:
            default_driver = kwargs.pop('default_driver')
        else:
            default_driver = None
        # can raise a ValueError
        webdriver_class = _from_env(default_driver=default_driver)
    else:
        # can raise a ValueError
        webdriver_class = _from_string(webdriver_name)
    if callable(webdriver_args):
        wd_args, wd_kwargs = webdriver_args(ctx, webdriver_class)
        args = tuple(wd_args) + tuple(args)
        kwargs = dict(list(wd_kwargs.items()) + list(kwargs.items()))
    ctx.behave_driver = webdriver_class(*args, **kwargs)
    yield ctx.behave_driver
    ctx.behave_driver.quit()
    del ctx.behave_driver


def before_all_factory(*args, **kwargs):
    """
    Create and return a `before_all` function that use the `fixture_browser` fixture with the corresponding arguments
    :param args: positional arguments of `fixture_browser` function
    :param kwargs: keywords arguments of `fixture_browser` function, including `webdriver_name`, `webdriver_class` and `webdriver_args` arguments

    >>> from behave_webdriver import before_all_factory
    >>> before_all = before_all_factory(webdriver_name='firefox')
    """
    def before_all(ctx):
        use_fixture(fixture_browser, ctx, *args, **kwargs)
    return before_all


def before_feature_factory(*args, **kwargs):
    """
    Create and return a `before_feature` function that use the `fixture_browser` fixture with the corresponding arguments
    :param args: positional arguments of `fixture_browser` function
    :param kwargs: keywords arguments of `fixture_browser` function, including `webdriver_name`, `webdriver_class` and `webdriver_args` arguments

    >>> from behave_webdriver import before_feature_factory
    >>> before_feature = before_feature_factory(webdriver_name='firefox')
    """
    def before_feature(ctx, feature):
        use_fixture(fixture_browser, ctx, *args, **kwargs)
    return before_feature


def before_scenario_factory(*args, **kwargs):
    """
    Create and return a `before_scenario` function that use the `fixture_browser` fixture with the corresponding arguments
    :param args: positional arguments of `fixture_browser` function
    :param kwargs: keywords arguments of `fixture_browser` function, including `webdriver_name`, `webdriver_class` and `webdriver_args` arguments

    >>> from behave_webdriver import before_scenario_factory
    >>> before_scenario = before_scenario_factory(webdriver_name='firefox')
    """
    def before_scenario(ctx, scenario):
        use_fixture(fixture_browser, ctx, *args, **kwargs)
    return before_scenario


class TransformerNotSet:
    pass



@fixture
def transformation_fixture(context, transformer_class, *args, **kwargs):
    old_transformer = context.transformer_class if 'transformer_class' in context else TransformerNotSet
    #transformer_class = partial(transformer_class, *args, **kwargs)

    class TransformerClass(transformer_class):
        def __init__(self, *more_args, **more_kwargs):
            nonlocal args, kwargs
            args += more_args
            kwargs.update(more_kwargs)
            super().__init__(*args, **kwargs)

    context.transformer_class = TransformerClass
    def cleanup(context, old):
        if old is TransformerNotSet:
            del context.transformer_class
        else:
            context.transformer_class = old
    cleanup_transformer = partial(cleanup, context, old_transformer)
    context.add_cleanup(cleanup_transformer)


def use_fixture_tag(context, tag, *args, **kwargs):
    if not tag.startswith('fixture'):
        return
    if tag.startswith('fixture.webdriver'):
        browser_name = tag.split('.')[-1]
        if browser_name == 'browser':
            browser_name = 'chrome'
        use_fixture(fixture_browser, context, *args, **kwargs)

    elif tag.startswith('fixture.transformer'):
        transformer_name = tag.split('.')[-1]
        transformer_class = getattr(transformers, transformer_name)
        use_fixture(transformation_fixture, context, transformer_class, **kwargs)

