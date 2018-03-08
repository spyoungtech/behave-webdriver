import pytest
import mock
import sys
import os
present_dir = os.path.dirname(os.path.realpath(__file__))
root_dir = os.path.abspath(os.path.join(present_dir, '..', '..'))
sys.path.insert(0, root_dir)
import behave_webdriver

driver_names = ['Chrome', 'Firefox', 'Ie', 'Edge', 'Opera', 'Safari', 'BlackBerry', 'PhantomJS', 'Android', 'Remote']
# drivers = [behave_webdriver.Chrome,
#            behave_webdriver.Firefox,
#            behave_webdriver.Ie,
#            behave_webdriver.Edge,
#            behave_webdriver.Opera,
#            behave_webdriver.Safari,
#            behave_webdriver.BlackBerry,
#            behave_webdriver.PhantomJS,
#            behave_webdriver.Android,
#            behave_webdriver.Remote]
#driver_map = [(driver_name, driver) for driver_name, driver in zip(driver_names, drivers)]

@pytest.mark.parametrize("driver_name", driver_names)
def test_browser_from_string(driver_name):
    driver_qual_name = 'behave_webdriver.' + driver_name
    with mock.patch(driver_qual_name) as mock_driver:
        driver = behave_webdriver.from_string(driver_name)
        assert mock_driver.called

@pytest.mark.parametrize("driver_name", driver_names)
def test_browser_from_env(driver_name):
    os.environ['BEHAVE_WEBDRIVER'] = driver_name
    driver_qual_name = 'behave_webdriver.' + driver_name
    with mock.patch(driver_qual_name) as mock_driver:
        driver = behave_webdriver.from_string(driver_name)
        assert mock_driver.called