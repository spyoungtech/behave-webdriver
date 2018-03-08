"""
Provides additional expected conditions as well as *negatable* versions of selenium's expected conditions.
"""

from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC


class NegationMixin(object):
    """
    Provides the ability to test the negation of any existing expected condition (EC).
    Currently, there is an unsolved problem in certain ECs due to the way exceptions are caught.
    """
    def __init__(self, *args, **kwargs):
        negative = kwargs.pop('negative', False)
        super(NegationMixin, self).__init__(*args, **kwargs)
        self.negative = negative

    def __call__(self, *args, **kwargs):
        try:
            result = super(NegationMixin, self).__call__(*args, **kwargs)
        except StaleElementReferenceException:
            return False  # Stale elements are unreliable, always try to regrab the element
        if self.negative:
            return not result
        return result


class AnyTextMixin(object):
    """
    Provides default for text_ arguments when the EC expects it. An empty value will test true when
    tested against any other string. For example, with selenium's ``text_to_be_present_in_element`` that checks
    >>> if element_text:
    ...     return self.text in element_text
    In effect, to the desired behavior of accepting just any text because ``'' in any_string`` is always ``True``
    >>> if element_text:
    ...    return True

    This behavior only applies if the text_ keyword argument is not provided.
    This may cause problems if you try to provide text_ as a positional argument, so don't do that.
    """
    def __init__(self, *args, **kwargs):
        if 'text_' not in kwargs:
            kwargs['text_'] = ''
        super(AnyTextMixin, self).__init__(*args, **kwargs)


class element_is_selected(NegationMixin, EC.element_located_to_be_selected):
    """
    Like selenium's element_located_to_be_selected but with the :ref:`~behave_webdriver.conditions.NegationMixin`.
    """
    pass


class element_is_visible(NegationMixin, EC.visibility_of_element_located):
    """
    Like selenium's visibility_of_element_located but with the :ref:`~behave_webdriver.conditions.NegationMixin`.
    """
    pass


class element_is_present(NegationMixin, EC.presence_of_element_located):
    """
    Like selenium's presence_of_element_located but with the :ref:`~behave_webdriver.conditions.NegationMixin`.
    """
    def __call__(self, driver):
        """
        extends __call__ to catch NoSuchElementException errors to support negation of element existing.
        """
        try:
            return super(element_is_present, self).__call__(driver)
        except NoSuchElementException:
            result = False
        if self.negative:
            return not result
        return result


class element_is_enabled(object):
    """
    A new EC that checks a webelement's ``is_enabled`` method.
    Negation is supplied manually, rather than the usual mixin.
    """
    def __init__(self, locator, negative=False):
        self.locator = locator
        self.negative = negative

    def __call__(self, driver):
        try:
            element = driver.find_element(*self.locator)
        except StaleElementReferenceException:
            return False
        result = element.is_enabled()
        if self.negative:
            return not result
        return result


class element_contains_text(NegationMixin, AnyTextMixin, EC.text_to_be_present_in_element):
    """
    Like selenium's text_to_be_present_in_element but with the :ref:`~behave_webdriver.conditions.NegationMixin`.
    and :ref:`~behave_webdriver.conditions.AnyTextMixin`.
    """
    def __call__(self, driver):
        """
        Same logic as in EC.text_to_be_present_in_element except StaleElementReferenceException is not caught
        this, for now, is needed to distinguish if a False return value is the result of this exception.
        """
        try:
            element = driver.find_element(*self.locator)
            result = bool(element.text)
        except StaleElementReferenceException:
            return False

        if self.negative:
            return not result
        return result


class element_contains_value(NegationMixin, AnyTextMixin, EC.text_to_be_present_in_element_value):
    """
    Like selenium's text_to_be_present_in_element_value but with the :ref:`~behave_webdriver.conditions.NegationMixin`.
    and :ref:`~behave_webdriver.conditions.AnyTextMixin`.
    """
    pass
