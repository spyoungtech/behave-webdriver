import pytest
import mock
import sys
import os
present_dir = os.path.dirname(os.path.realpath(__file__))
root_dir = os.path.abspath(os.path.join(present_dir, '..', '..'))
sys.path.insert(0, root_dir)
import behave_webdriver.fixtures


def test_driver_with_custom_arguments():
    class CustomDriver(behave_webdriver.fixtures.BehaveDriverMixin):
        def __init__(self, *args, **kwargs):
            self._args = args
            self._kwargs = kwargs
            self._quit = False

        def quit(self):
            self._quit = True
    ctx = mock.MagicMock()
    gen = behave_webdriver.fixtures.fixture_browser(ctx, 4, True, "test", webdriver=CustomDriver, options={'param': 'value'})
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
