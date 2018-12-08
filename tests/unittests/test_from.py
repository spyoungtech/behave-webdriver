import pytest
import mock
import sys
import os
present_dir = os.path.dirname(os.path.realpath(__file__))
root_dir = os.path.abspath(os.path.join(present_dir, '..', '..'))
sys.path.insert(0, root_dir)
import behave_webdriver.utils

driver_names = ['Chrome', 'Firefox', 'Ie', 'Edge', 'Opera', 'Safari', 'BlackBerry', 'PhantomJS', 'Android', 'Remote']


@pytest.mark.parametrize("driver_name", driver_names)
def test_browser_from_string(driver_name):
    driver_qual_name = 'behave_webdriver.utils.' + driver_name
    with mock.patch(driver_qual_name) as mock_driver:
        mock_driver.__name__ = driver_name
        driver = behave_webdriver.utils.from_string(driver_name)
        assert mock_driver.called


@pytest.mark.parametrize("driver_name", driver_names)
def test_browser_from_env(driver_name):
    driver_qual_name = 'behave_webdriver.utils.' + driver_name
    with mock.patch.dict(os.environ, {'BEHAVE_WEBDRIVER': driver_name}), mock.patch(driver_qual_name) as mock_driver:
        mock_driver.__name__ = driver_name
        driver = behave_webdriver.utils.from_env()
        assert mock_driver.called


def test_default_from_env_driver_as_driver():
    with mock.patch.dict(os.environ, clear=True):
        def_driver = behave_webdriver.utils.Chrome
        Driver = behave_webdriver.utils._from_env(default_driver=def_driver)
    assert Driver is def_driver


def test_default_from_env_driver_as_string():
    with mock.patch.dict(os.environ, clear=True):
        expected_driver = behave_webdriver.utils.Chrome
        Driver = behave_webdriver.utils._from_env(default_driver='Chrome')
    assert Driver is expected_driver


def test_env_raises_for_absent_drivername():

    with pytest.raises(ValueError) as excinfo, mock.patch.dict(os.environ, clear=True):
        driver = behave_webdriver.utils._from_env()
    assert "No driver found in environment variables and no default" in str(excinfo.value)


def test_string_raises_for_invalid_drivername_and_contains_options():
    with pytest.raises(ValueError) as excinfo:
        driver = behave_webdriver.utils._from_string('foo')
    assert 'No such driver "foo"' in str(excinfo.value)
    assert all(dname.upper() in str(excinfo.value) for dname in driver_names)
