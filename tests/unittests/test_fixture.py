import pytest
import mock
import sys
import os
present_dir = os.path.dirname(os.path.realpath(__file__))
root_dir = os.path.abspath(os.path.join(present_dir, '..', '..'))
sys.path.insert(0, root_dir)
import behave_webdriver.fixtures


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
