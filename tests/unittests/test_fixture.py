import pytest
import mock
import sys
import os
present_dir = os.path.dirname(os.path.realpath(__file__))
root_dir = os.path.abspath(os.path.join(present_dir, '..', '..'))
sys.path.insert(0, root_dir)
import behave_webdriver.fixtures


def test_driver_from_env():
    with mock.patch('behave_webdriver.fixtures._from_env') as mock_from_env:
        chrome = mock.MagicMock(name='chrome')
        Chrome = mock.MagicMock(name='Chrome', return_value=chrome)
        mock_from_env.return_value = Chrome
        ctx = mock.MagicMock()
        gen = behave_webdriver.fixtures.fixture_browser(ctx)
        driver = next(gen)
        assert driver is chrome
        assert ctx.behave_driver is chrome
        assert mock_from_env.called
        try:
            next(gen)
            pytest.fail('StopIteration expected')
        except StopIteration:
            pass
        assert chrome.quit.called
        assert 'behave_driver' not in ctx


def test_driver_from_name():
    with mock.patch('behave_webdriver.fixtures._from_string') as mock_from_string:
        chrome = mock.MagicMock(name='chrome')
        Chrome = mock.MagicMock(name='Chrome', return_value=chrome)
        mock_from_string.return_value = Chrome
        ctx = mock.MagicMock()
        gen = behave_webdriver.fixtures.fixture_browser(ctx, webdriver_name='chrome')
        driver = next(gen)
        assert driver is chrome
        assert ctx.behave_driver is chrome
        assert mock_from_string.called_with('chrome')
        try:
            next(gen)
            pytest.fail('StopIteration expected')
        except StopIteration:
            pass
        assert chrome.quit.called
        assert 'behave_driver' not in ctx


def test_driver_from_bad_class():
    class CustomDriver(object):
        pass
    ctx = mock.MagicMock()
    with pytest.raises(ValueError) as excinfo:
        gen = behave_webdriver.fixtures.fixture_browser(ctx, webdriver_class=CustomDriver)
        driver = next(gen)
    assert 'The driver "CustomDriver" does not inherit from BehaveDriverMixin.' in str(excinfo.value)


def test_driver_from_good_class():
    class CustomDriver(behave_webdriver.fixtures.BehaveDriverMixin):
        def __init__(self, *args, **kwargs):
            self._args = args
            self._kwargs = kwargs
            self._quit = False

        def quit(self):
            self._quit = True
    ctx = mock.MagicMock()
    gen = behave_webdriver.fixtures.fixture_browser(ctx, webdriver_class=CustomDriver)
    driver = next(gen)
    assert isinstance(driver, CustomDriver)
    assert ctx.behave_driver is driver
    try:
        next(gen)
        pytest.fail('StopIteration expected')
    except StopIteration:
        pass
    assert driver._quit is True
    assert 'behave_driver' not in ctx


def test_driver_with_custom_arguments():
    class CustomDriver(behave_webdriver.fixtures.BehaveDriverMixin):
        def __init__(self, *args, **kwargs):
            self._args = args
            self._kwargs = kwargs
            self._quit = False

        def quit(self):
            self._quit = True
    ctx = mock.MagicMock()
    gen = behave_webdriver.fixtures.fixture_browser(ctx, 4, True, "test", webdriver_class=CustomDriver, options={'param': 'value'})
    driver = next(gen)
    assert isinstance(driver, CustomDriver)
    assert ctx.behave_driver is driver
    assert driver._quit is False
    assert driver._args == (4, True, "test")
    assert driver._kwargs == {'options': {'param': 'value'}}
    try:
        next(gen)
        pytest.fail('StopIteration expected')
    except StopIteration:
        pass
    assert driver._quit is True
    assert 'behave_driver' not in ctx


def test_driver_with_lamda_arguments():
    class CustomDriver(behave_webdriver.fixtures.BehaveDriverMixin):
        def __init__(self, *args, **kwargs):
            self._args = args
            self._kwargs = kwargs
            self._quit = False

        def quit(self):
            self._quit = True

    def get_driver_args(ctx, webdriver_class):
        if webdriver_class == CustomDriver:
            return ([42], {'special_arg': 13})
        else:
            return ([], {})
    ctx = mock.MagicMock()
    gen = behave_webdriver.fixtures.fixture_browser(ctx, 4, True, "test", webdriver_class=CustomDriver, webdriver_args=get_driver_args, options={'param': 'value'})
    driver = next(gen)
    assert isinstance(driver, CustomDriver)
    assert ctx.behave_driver is driver
    assert driver._quit is False
    assert driver._args == (42, 4, True, "test")
    assert driver._kwargs == {'options': {'param': 'value'}, 'special_arg': 13}
    try:
        next(gen)
        pytest.fail('StopIteration expected')
    except StopIteration:
        pass
    assert driver._quit is True
    assert 'behave_driver' not in ctx


def test_before_all_factory():
    with mock.patch('behave_webdriver.fixtures.use_fixture') as mock_use_fixture:
        args = (4, True, "test")
        kwargs = {
            'webdriver_name': 'Firefox',
            'options': {'param': 'value'},
        }
        before_all = behave_webdriver.fixtures.before_all_factory(*args, **kwargs)
        ctx = mock.MagicMock()
        before_all(ctx)
        assert mock_use_fixture.called_with(ctx, *args, **kwargs)


def test_before_feature_factory():
    with mock.patch('behave_webdriver.fixtures.use_fixture') as mock_use_fixture:
        args = (4, True, "test")
        kwargs = {
            'webdriver_name': 'Firefox',
            'options': {'param': 'value'},
        }
        before_feature = behave_webdriver.fixtures.before_feature_factory(*args, **kwargs)
        ctx = mock.MagicMock()
        feature = mock.MagicMock()
        before_feature(ctx, feature)
        assert mock_use_fixture.called_with(ctx, *args, **kwargs)


def test_before_scenario_factory():
    with mock.patch('behave_webdriver.fixtures.use_fixture') as mock_use_fixture:
        args = (4, True, "test")
        kwargs = {
            'webdriver_name': 'Firefox',
            'options': {'param': 'value'},
        }
        before_scenario = behave_webdriver.fixtures.before_scenario_factory(*args, **kwargs)
        ctx = mock.MagicMock()
        scenario = mock.MagicMock()
        before_scenario(ctx, scenario)
        assert mock_use_fixture.called_with(ctx, *args, **kwargs)
