from selenium.common.exceptions import NoSuchElementException
class BehaveDriver(object):
    def __init__(self, driver, **options):
        self.driver = driver

    @property
    def title(self):
        return self.driver.title

    @property
    def current_url(self):
        return self.driver.current_url

    @property
    def cookies(self):
        return self.driver.get_cookies()

    def get_cookie(self, cookie_name):
        return self.driver.get_cookie(cookie_name)

    def get_element(self, selector):
        """
        :param selector: An xpath or CSS selector
        :return:
        """
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

