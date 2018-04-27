import pytest
import mock
import sys
import os
present_dir = os.path.dirname(os.path.realpath(__file__))
root_dir = os.path.abspath(os.path.join(present_dir, '..', '..'))
sys.path.insert(0, root_dir)
from behave_webdriver.driver import BehaveDriverMixin
from selenium.webdriver.common.by import By


def _init_get_element_mocks():
    class DriverTest(BehaveDriverMixin):
        pass
    mock_el = mock.MagicMock(name='Html element')
    DriverTest.find_element = mock.MagicMock(name='find_element', return_value=mock_el)
    DriverTest.find_element_by_xpath = mock.MagicMock(name='find_element_by_xpath', return_value=mock_el)
    DriverTest.find_element_by_css_selector = mock.MagicMock(name='find_element_by_css_selector', return_value=mock_el)
    return DriverTest, mock_el


def test_get_element_with_by():
    DriverTest, mock_el = _init_get_element_mocks()
    el = DriverTest().get_element('/my_weird_id', by=By.ID)
    assert el is mock_el
    assert DriverTest.find_element.called
    assert DriverTest.find_element_by_xpath.not_called
    assert DriverTest.find_element_by_css_selector.not_called


def test_get_element_with_xpath_expression():
    DriverTest, mock_el = _init_get_element_mocks()
    el = DriverTest().get_element('/my_xpath/expression')
    assert el is mock_el
    assert DriverTest.find_element.not_called
    assert DriverTest.find_element_by_xpath.called
    assert DriverTest.find_element_by_css_selector.not_called


def test_get_element_with_css_selector():
    DriverTest, mock_el = _init_get_element_mocks()
    el = DriverTest().get_element('div.specific-class[title="tooltip"]')
    assert el is mock_el
    assert DriverTest.find_element.not_called
    assert DriverTest.find_element_by_xpath.not_called
    assert DriverTest.find_element_by_css_selector.called


def _init_wait_for_element_condition_mocks():
    with mock.patch('behave_webdriver.driver.element_is_present') as mock_element_is_present:
        with mock.patch('behave_webdriver.driver.WebDriverWait') as mock_WebDriverWait:
            mock_el = mock.MagicMock(name='Html element')
            mock_web_driver_wait = mock.MagicMock(name='web_driver_wait')
            mock_web_driver_wait.until.return_value = mock_el
            mock_WebDriverWait.return_value = mock_web_driver_wait
            class DriverTest(BehaveDriverMixin):
                pass
            yield DriverTest, mock_el, mock_WebDriverWait, mock_web_driver_wait, mock_element_is_present


def test_wait_for_element_condition_with_xpath_expression():
    for DriverTest, mock_el, mock_WebDriverWait, mock_web_driver_wait, mock_element_is_present \
        in _init_wait_for_element_condition_mocks():
        driver_test = DriverTest()
        el = driver_test.wait_for_element_condition('/my_xpath/expression', None, None, None)
        assert el is mock_el
        assert mock_WebDriverWait.called_with(driver_test, driver_test.default_wait)
        assert mock_web_driver_wait.until.called
        assert mock_element_is_present.called_with((By.XPATH, '/my_xpath/expression'), False)


def test_wait_for_element_condition_with_css_selector():
    for DriverTest, mock_el, mock_WebDriverWait, mock_web_driver_wait, mock_element_is_present \
        in _init_wait_for_element_condition_mocks():
        driver_test = DriverTest()
        el = driver_test.wait_for_element_condition('div.specific-class[title="tooltip"]', None, None, None)
        assert el is mock_el
        assert mock_WebDriverWait.called_with(driver_test, driver_test.default_wait)
        assert mock_web_driver_wait.until.called
        assert mock_element_is_present.called_with((By.CSS_SELECTOR, '/my_xpath/expression'), False)
