from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains
import time


class element_is_enabled(object):
    def __init__(self, element):
        self.element = element

    def __call__(self, driver):
        element = self.element
        if element.is_enabled():
            return element
        else:
            return False

class element_exists(object):
    def __init__(self, locator):
        self.locator = locator

    def __call__(self, driver):
        try:
            element = driver.find_element(*self.locator)
        except NoSuchElementException:
            return False
        if element:
            return element

class BehaveDriver(object):
    def __init__(self, driver):
        self.driver = driver

    def __getattr__(self, item):
        if hasattr(self.driver, item):
            return getattr(self.driver, item)
        else:
            raise AttributeError('{} has no attribute {}'.format(self, item))

    @classmethod
    def chrome(cls, *args, **kwargs):
        driver = webdriver.Chrome(*args, **kwargs)
        return cls(driver=driver)

    @classmethod
    def headless_chrome(cls, *args, **kwargs):
        chrome_options = kwargs.pop('chrome_options', None)
        if chrome_options is None:
            chrome_options = ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        driver = webdriver.Chrome(*args, chrome_options=chrome_options, **kwargs)
        return cls(driver=driver)

    @property
    def alert(self):
        return Alert(self.driver)
    @property
    def screen_size(self):
        size = self.driver.get_window_size()
        x = size['width']
        y = size['height']
        return (x, y)

    @screen_size.setter
    def screen_size(self, size):
        x, y = size
        if x is None:
            x = self.screen_size[0]
        if y is None:
            y = self.screen_size[1]
        self.driver.set_window_size(x, y)


    @property
    def cookies(self):
        return self.driver.get_cookies()

    @property
    def has_alert(self):
        e = EC.alert_is_present()
        return e(self.driver)

    def get_cookie(self, cookie_name):
        return self.driver.get_cookie(cookie_name)

    def get_element(self, selector, by=None):
        """
        :param selector: An xpath or CSS selector
        :return:
        """
        if by:
            return self.driver.find_element(by, selector)
        if selector.startswith('//'):
            return self.driver.find_element_by_xpath(selector)
        else:
            return self.driver.find_element_by_css_selector(selector)

    def get_element_text(self, element):
        elem = self.get_element(element)
        return elem.text

    def get_element_attribute(self, element, attr, css=False):
        elem = self.get_element(element)
        if css:
            value = elem.value_of_css_property(attr)
        else:
            value = elem.get_attribute(attr)
        return value

    def get_element_size(self, element):
        elem = self.get_element(element)
        return elem.size

    def get_element_location(self, element):
        elem = self.get_element(element)
        return elem.location

    def open_url(self, url):
        return self.driver.get(url)

    def element_exists(self, element):
        try:
            elem = self.get_element(element)
            return True
        except NoSuchElementException:
            return False

    def element_visible(self, element):
        elem = self.get_element(element)
        return elem.is_displayed()

    def element_enabled(self, element):
        elem = self.get_element(element)
        return elem.is_enabled()

    def element_selected(self, element):
        elem = self.get_element(element)
        return elem.is_selected()


    def element_contains(self, element, value):
        elem = self.get_element(element)
        element_value = elem.get_property('value')
        if element_value is None:
            element_value = elem.text
        return value in element_value

    def click_element(self, element, n=1, delay=0.1):
        if n < 1:
            return
        elem = self.get_element(element)
        elem.click()
        for _ in range(n-1):
            time.sleep(delay)
            elem.click()

    def doubleclick_element(self, element):
        elem = self.get_element(element)
        actions = ActionChains(self.driver)
        actions.double_click(elem)
        actions.perform()

    def click_link_text(self, text, partial=False):
        if partial:
            self.driver.find_element_by_partial_link_text(text).click()
        else:
            self.driver.find_element_by_link_text(text).click()

    def drag_element(self, element, to_element):
        source_elem = self.get_element(element)
        to_elem = self.get_element(to_element)
        actions = ActionChains(self.driver)
        actions.drag_and_drop(source_elem, to_elem)
        actions.perform()

    def submit(self, element):
        elem = self.get_element(element)
        elem.submit()

    def send_keys(self, keys):
        actions = ActionChains(self.driver)
        actions.send_keys(keys)
        actions.perform()

    def scroll_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def scroll_to_element(self, element):
        location = self.get_element_location(element)
        x = location['x']
        y = location['y']
        self.scroll_to(x, y)

    def scroll_to(self, x, y):
        # prevent script injection
        x = int(x)
        y = int(y)
        self.driver.execute_script('window.scrollTo({}, {});'.format(x, y))

    def pause(self, milliseconds):
        # TODO: use webdriver pause functionality?
        # actions = ActionChains(self.driver)
        seconds = round(milliseconds / 1000, 3)
        # actions.pause(seconds)
        #actions.perform()
        time.sleep(seconds)

    def wait_for_element_condition(self, element, ms, condition):
        conditions = {
            'be checked': EC.element_to_be_selected,
            'be enabled': element_is_enabled,
            'be selected': EC.element_to_be_selected,
            'be visible': EC.visibility_of_element_located,
            'contain a text': EC.text_to_be_present_in_element,
            'contain a value': EC.text_to_be_present_in_element_value,
            'exist': element_exists,
        }

        if not condition or condition in ['exist', 'be visible']:
            if element.startswith('//'):
                elem = (By.XPATH, element)
            else:
                elem = (By.CSS_SELECTOR, element)
        else:
            elem = self.get_element(element)
        seconds = round(ms / 1000, 3)
        wait = WebDriverWait(self.driver, seconds)
        if condition:
            expected = conditions[condition]
        else:
            expected = element_exists

        try:
            result = wait.until(expected(elem))
        except TimeoutException:
            result = None

        return result






