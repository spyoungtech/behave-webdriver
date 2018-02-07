import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.color import Color

from .conditions import element_is_present, element_is_selected, element_contains_value, element_is_visible, element_contains_text, element_is_enabled



class BehaveDriver(object):
    """
    Implements most of the logic for step definitions. Should be fully substitutable with any selenium webdriver.
    Attributes of the underlying webdriver can be accessed directly (behave_driver.attr)
    or you can access the driver attribute `behave_driver.driver.attr`
    """
    def __init__(self, driver, default_wait=None):
        self.driver = driver

    def __getattr__(self, item):
        if hasattr(self.driver, item):
            return getattr(self.driver, item)
        else:
            raise AttributeError('{} has no attribute {}'.format(self, item))

    @classmethod
    def chrome(cls, *args, **kwargs):
        """
        Alternative constructor. Creates BehaveDriver instance using standard chromedriver.
        :param args: positional args passed to `webdriver.Chrome`
        :param kwargs: keyword args passed to `webdriver.Chrome`
        :return: a BehaveDriver instance
        """
        driver = webdriver.Chrome(*args, **kwargs)
        return cls(driver=driver)


    @classmethod
    def firefox(cls, *args, **kwargs):
        """
        Alternative constructor. Creates a BehaveDriver instance using standard firefox gecko driver.
        :param args: dirver args
        :param kwargs: driver kwargs
        :return: a BehaveDriver instance
        """
        driver = webdriver.Firefox(*args, **kwargs)
        return cls(driver=driver)

    @classmethod
    def phantom_js(cls, *args, **kwargs):
        """
        Alternative constructor. Creates a BehaveDriver instance using standard phantomJS driver.
        :param args: dirver args
        :param kwargs: driver kwargs
        :return: a BehaveDriver instance
        """
        driver = webdriver.PhantomJS(*args, **kwargs)
        return cls(driver=driver)

    @classmethod
    def safari(cls, *args, **kwargs):
        """
        Alternative constructor. Creates a BehaveDriver instance using standard safari driver.
        :param args: dirver args
        :param kwargs: driver kwargs
        :return: a BehaveDriver instance
        """
        driver = webdriver.Safari(*args, **kwargs)
        return cls(driver=driver)

    @classmethod
    def headless_chrome(cls, *args, **kwargs):
        """
        Alternate constructor. Creates a BehaveDriver instance using a chromrdriver with headless options.
        :param args: positional args passed to `webdriver.Chrome`
        :param kwargs: keyword args passed to `webdriver.Chrome`
        :return: a BehaveDriver instance
        """
        chrome_options = kwargs.pop('chrome_options', None)
        if chrome_options is None:
            chrome_options = ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        driver = webdriver.Chrome(*args, chrome_options=chrome_options, **kwargs)
        return cls(driver=driver)

    @property
    def alert(self):
        """
        Property shortcut for an `Alert` object for the driver
        Note: this will return an Alert instance regardless of whether or not there is actually an alert present.
        Use `has_alert` to check whether or not there is an alert currently present.
        :return: an selenium.webdriver.common.alert.Alert instance
        """
        return Alert(self.driver)

    @property
    def screen_size(self):
        """
        Property for the current screen size
        :return: tuple of the screen dimensions (x, y)
        """
        size = self.driver.get_window_size()
        x = size['width']
        y = size['height']
        return (x, y)

    @screen_size.setter
    def screen_size(self, size):
        """
        :param size: The dimensions to set the screen to in (x, y) format.
        :type size: tuple
        :return:
        >>> behave_driver = BehaveDriver.chrome()
        >>> behave_driver.screen_size = (800, 600) # changes the screen size
        >>> behave_driver.screen_size == behave_driver.get_window_size() == (800, 600)
        True

        """
        x, y = size
        if x is None:
            x = self.screen_size[0]
        if y is None:
            y = self.screen_size[1]
        self.driver.set_window_size(x, y)


    @property
    def cookies(self):
        """
        Shortcut for driver.get_cookies()
        :return:
        """
        return self.driver.get_cookies()

    @property
    def has_alert(self):
        """
        Whether or not there is currently an alert present
        :return: True if there is an alert present, else False
        :rtype: bool
        """
        e = EC.alert_is_present()
        return e(self.driver)

    def get_cookie(self, cookie_name):
        """
        retrieve a cookie with a particular name
        :param cookie_name: the name of the cookie
        :type cookie_name: str
        :return: A dictionary containing the cookie information
        :rtype: dict
        """
        return self.driver.get_cookie(cookie_name)

    def get_element(self, selector, by=None):
        """
        Takes a selector string and uses an appropriate method (XPATH or CSS selector by default) to find a WebElement
        The optional `by` argument can be supplied to specify any locating method explicitly.
        This is used to resolve selectors from step definition strings to actual element objects

        :param selector: The selector to use, an XPATH or CSS selector
        :type selector: str
        :param by: alternate method used to locate element, e.g. (By.id) See selenium.webdriver.common.by.By attributes
        :return: WebElement object
        """
        if by:
            return self.driver.find_element(by, selector)
        if selector.startswith('//'):
            return self.driver.find_element_by_xpath(selector)
        else:
            return self.driver.find_element_by_css_selector(selector)

    def get_element_text(self, element):
        """
        Takes in a selector, finds the element, and extracts the text.
        When present on the WebElement, the element's 'value' property is returned. (For example, this is useful for
        getting the current text of Input elements)
        If the element has no 'value' property, the containing text is returned (elem.text)

        :param element: selector to use to locate the element
        :type element: str
        :return: the text contained within the element.
        :rtype: str
        """
        elem = self.get_element(element)
        value = elem.get_property('value')
        if value is not None:
            return value
        return elem.text

    def get_element_attribute(self, element, attr, css=False, expected_value=None):
        """
        Get the value of an attribute or css attribute from an element.
        :param element: selector used to locate the element.
        :type element: str
        :param attr: The attribute to lookup
        :type attr: str
        :param css: Whether or not this is a CSS atrribute
        :type css: bool
        :return: The value of the attribute
        """
        elem = self.get_element(element)
        if css:
            value = elem.value_of_css_property(attr)
            if self.is_color(value):
                value = Color.from_string(value)
            if expected_value:
                if self.is_color(expected_value):
                    expected_value = Color.from_string(expected_value)
                return value, expected_value
        else:
            value = elem.get_attribute(attr)
        return value

    def get_element_size(self, element):
        """
        Returns a dictionary containing the size information of an element.
        The dictionary has two keys: 'width' and 'height' which represent the size of the element dimensions in px
        :param element: selector used to locate the element
        :type element: str
        :return: A dictionary with size information
        :rtype: dict
        """
        elem = self.get_element(element)
        return elem.size

    def get_element_location(self, element):
        """
        Gets the location of the element in the renderable canvas.
        This is a dict with two keys: 'x' and 'y'
        :param element: selector used to locate the element
        :type element: str
        :return: the element's location
        :rtype: dict
        """
        elem = self.get_element(element)
        return elem.location

    def open_url(self, url):
        """
        Get an absolute URL
        :param url: an absolute URL including the scheme
        :type url: str
        :return:
        """
        return self.driver.get(url)

    def element_exists(self, element):
        """
        Whether or not an element exists. Attempts to locate the element using `get_element` returns True if the element
        was found, False if it couldn't be located.
        :param element: the selector used to locate the element
        :type element: str
        :return: True if the element could be found, False if it couldn't be found
        :rtype: bool
        """
        try:
            self.get_element(element)  # attempt to get the element
            return True  # if it succeeded, return True
        except NoSuchElementException:
            # The element was not able to be located
            return False

    def element_visible(self, element):
        """
        Checks if an element is visible or not.
        :param element: the selector used to locate the element
        :type element: str
        :return: True if the element is visible, else False
        :rtype: bool
        """
        elem = self.get_element(element)
        return elem.is_displayed()

    def element_enabled(self, element):
        """
        Checks if an element is enabled or not.

        :param element: the selector used to locate the element
        :type element: str
        :return: True if the element is enabled, else False
        :rtype: bool
        """
        elem = self.get_element(element)
        return elem.is_enabled()

    def element_selected(self, element):
        """
        Checks if an element is selected or not.

        :param element: the selector used to locate the element
        :type element: str
        :return: True if the element is selected, else False
        :rtype: bool
        """
        elem = self.get_element(element)
        return elem.is_selected()

    def element_contains(self, element, value):
        """
        Checks if an element contains (in value/text) a given string/value

        :param element: the selector used to locate the element
        :type element: str
        :param value: the text/value to check for
        :type value: str
        :return: True or False, whether or not the value was found in the element.
        :rtype: bool
        """
        elem = self.get_element(element)
        element_value = elem.get_property('value')
        if element_value is None:
            element_value = elem.text
        return value in element_value

    def element_has_class(self, element, cls):
        """
        Checks whether or not an element has a particular css class.

        :param element: the selector used to locate the element
        :type element: str
        :param cls: The css class to check for
        :type cls: str
        :return: True if the element has the specified class, else False
        :rtype: bool
        """
        elem = self.get_element(element)
        elem_classes = elem.get_attribute('class')
        return cls in elem_classes

    def click_element(self, element, n=1, delay=0.1):
        """
        Click on an element. Note: this will not trigger some doubleclick events, even when n=2 with any delay.
        Instead, if you want to doubleclick, use `doubleclick_element`

        :param element: the selector used to locate the element
        :type element: str
        :param n: Number of times to click
        :type n: int
        :param delay: Delay (in seconds) between each click.
        :return:
        """
        if n < 1:
            return
        elem = self.get_element(element)
        elem.click()
        for _ in range(n-1):
            time.sleep(delay)
            elem.click()

    def doubleclick_element(self, element):
        """
        Double click an element
        :param element: the selector used to locate the element
        :type element: str
        :return:
        """
        elem = self.get_element(element)
        actions = ActionChains(self.driver)
        actions.double_click(elem)
        actions.perform()

    def click_link_text(self, text, partial=False):
        """
        Click on a link, located by matching the text contained in the link. If `partial` is True,
        the link is located by partial text.
        :param text: The text contained in the link, used to locate the element.
        :type text: str
        :param partial: Whether or not to match link by partial text (as opposed to full match)
        :type partial: bool
        :return:
        """
        if partial:
            self.driver.find_element_by_partial_link_text(text).click()
        else:
            self.driver.find_element_by_link_text(text).click()

    def drag_element(self, element, to_element):
        """
        Drag an element to the location of another element.
        :param element: the selector used to locate the source element
        :type element: str
        :param to_element: the selector used to locate the destination element
        :type to_element: str
        :return:
        """
        source_elem = self.get_element(element)
        to_elem = self.get_element(to_element)
        actions = ActionChains(self.driver)
        actions.drag_and_drop(source_elem, to_elem)
        actions.perform()

    def submit(self, element):
        """
        Shortcut for submitting an element
        :param element: the selector used to locate the element
        :type element: str
        :return:
        """
        elem = self.get_element(element)
        elem.submit()

    def send_keys(self, keys):
        """
        Send arbitrary keys. Note: this is different than sending keys directly to an element.
        :param keys: keys to send
        :return:
        """
        actions = ActionChains(self.driver)
        actions.send_keys(keys)
        actions.perform()

    def press_button(self, button):
        """
        Send a keystroke simulating the press of a given button. You can use keys as strings (e.g. 'a', 'z') or any
        key names (e.g. the 'escape' key). When the length of the button argument is greater than one character,
        names are checked against selenium.webdriver.common.keys.Keys first.

        :param button: A single character or key name
        :type button: str
        :return:
        """
        if len(button) > 1:
            button = getattr(Keys, button.upper(), button)
        self.send_keys(button)

    def scroll_to_bottom(self):
        """
        Scrolls the current window to the bottom of the window (0, document.body.scrollHeight).
        :return:
        """
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def scroll_to_element(self, element):
        """
        Scroll to the location of an element.
        :param element:
        :return:
        """
        location = self.get_element_location(element)
        x = location['x']
        y = location['y']
        self.scroll_to(x, y)

    def scroll_to(self, x, y):
        """
        Scroll to a particular (x, y) coordinate.

        :param x: the x coordinate to scroll to.
        :type x: int
        :param y: the y coordinate to scroll to.
        :type y: int
        :return:
        """
        # prevent script injection
        x = int(x)
        y = int(y)
        self.driver.execute_script('window.scrollTo({}, {});'.format(x, y))

    def move_to_element(self, element, offset=None):
        """
        Moves the mouse to the middle of an element
        :param element: the selector used to locate the element
        :type element: str
        :param offset: optional tuple of x/y offsets to offset mouse from center
        :type offset: tuple
        :return:
        """
        elem = self.get_element(element)
        actions = ActionChains(self.driver)
        if offset:
            actions.move_to_element_with_offset(elem, *offset)
        else:
            actions.move_to_element(elem)
        actions.perform()

    def pause(self, milliseconds):
        """
        sleep for a number of miliseconds. For now, this just uses time.sleep, but will probably change.
        :param milliseconds: number of miliseconds to wait
        :type milliseconds: int
        :return:
        """
        # TODO: use webdriver pause functionality?
        # actions = ActionChains(self.driver)
        seconds = round(milliseconds / 1000, 3)
        # actions.pause(seconds)
        #actions.perform()
        time.sleep(seconds)

    def wait_for_element_condition(self, element, ms, negative, condition):
        """
        Wait on an element until a certain condition is met, up to a maximum amount of time to wait.
        This is currently (pre-0.0.1 release) a major work-in-progress, so expect it to change without warning

        :param element: selector used to locate the element
        :param ms: maximum time (in milliseconds) to wait for the condition to be true
        :param negative: whether or not the check for negation of condition. Will coarse boolean from value
        :param condition: the condition to check for. Defaults to checking for presence of element
        :return: element
        """
        if not ms:
            seconds = 1.5
        else:
            seconds = round(ms / 1000, 3)

        condition_text_map = {
            'be checked': element_is_selected,
            'be enabled': element_is_enabled,
            'be selected': element_is_selected,
            'be visible': element_is_visible,
            'contain a text': element_contains_text,
            'contain a value': element_contains_value,
            'exist': element_is_present,
        }

        if condition:
            expected = condition_text_map[condition]
        else:
            expected = element_is_present

        if element.startswith('//'):
            locator = (By.XPATH, element)
        else:
            locator = (By.CSS_SELECTOR, element)

        wait = WebDriverWait(self.driver, seconds)

        try:
            result = wait.until(expected(locator, negative=bool(negative)))
        except TimeoutException:
            result = None

        return result

    @staticmethod
    def is_color(str_):
        try:
            Color.from_string(str_)
            return True
        except ValueError:
            return False
