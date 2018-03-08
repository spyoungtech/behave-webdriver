Advanced usage; extending behave-webdriver
==========================================

behave-webdriver is designed with **you** in-mind. You are free to extend the behavior of our webdriver classes to suit your
unique needs. You can subclass our webdriver classes, use a custom selenium webdriver, write your own mixin, or use
a mixin somebody else provides for selenium.


Example: selenium-requests
--------------------------

`selenium-requests`_ is a preexisting project that adds functionality of the popular ``requests`` library to selenium.
It is simple to use ``selenium-requests`` with behave-webdriver.
The following, and other examples, are available in the repo ``examples`` directory and in the full documentation.

.. code-block:: python

   # examples/selenium-requests/features/environment.py
   from selenium import webdriver # or any custom webdriver
   from behave_webdriver.driver import BehaveDriverMixin
   from seleniumrequests import RequestMixin # or your own mixin

   class BehaveRequestDriver(BehaveDriverMixin, RequestMixin, webdriver.Chrome):
       pass

   def before_all(context):
       context.behave_driver = BehaveRequestDriver()
.. code-block:: python

   # examples/selenium-requests/features/steps/selenium_steps.py
   from behave import *
   from behave_webdriver.steps import *
   from urllib.parse import urljoin

   @given('I send a {method} request to the page "{page}"')
   def send_request_page(context, method, page):
       url = urljoin(context.base_url, page)
       context.response = context.behave_driver.request(method, url)

   @then('I expect the response text contains "{text}"')
   def check_response_text_contains(context, text):
       assert text in context.response.text
.. code-block:: gherkin

   # examples/selenium-requests/features/selenium-requests.feature
   Feature: Using selenium-requests
     As a developer
     I should be able to extend behave-webdriver with selenium-requests

     Scenario: use selenium-requests with behave-webdriver
       # use a behave-webdriver step
       Given the base url is "http://127.0.0.1:8000"
       # use your own steps using selenium-requests features
       Given I send a GET request to the page "/"
       Then I expect the response text contains "<h1>DEMO APP</h1>"

Assuming you're in the repository root (and have the demo app running) just run like any other project with ``behave``

Results ✨
^^^^^^^^^^

.. code-block:: guess

   (behave-webdriver) $ behave examples/selenium-requests/features

   DevTools listening on ws://127.0.0.1:12646/devtools/browser/1fe75b44-1c74-49fa-8e77-36c54d50cd24
   Feature: Using selenium-requests # examples/selenium-requests/features/requests.feature:1
     As a developer
     I should be able to extend behave-webdriver with selenium-requests
     Scenario: use selenium-requests with behave-webdriver          # examples/selenium-requests/features/requests.feature:6
       Given the base url is "http://127.0.0.1:8000"                # behave_webdriver/steps/actions.py:162
       Given I send a GET request to the page "/"                   # examples/selenium-requests/features/steps/selenium_steps.py:11
       Then I expect the response text contains "<h1>DEMO APP</h1>" # examples/selenium-requests/features/steps/selenium_steps.py:17

   1 feature passed, 0 failed, 0 skipped
   1 scenario passed, 0 failed, 0 skipped
   3 steps passed, 0 failed, 0 skipped, 0 undefined
   Took 0m1.385s

.. _selenium-requests: https://github.com/cryzed/Selenium-Requests
