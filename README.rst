behave-webdriver
================

behave-webdriver is a step library intended to allow users to easily write `selenium`_ webdriver tests with the
behave BDD testing framework.
Inspired by the `webdriverio/cucumber-boilerplate`_ project.

|docs| |status| |version| |pyversions| |coverage|

For more details, see the `behave-webdriver documentation`_

.. image:: https://raw.githubusercontent.com/spyoungtech/behave-webdriver/master/docs/_static/behave-webdriver.gif




Installation
============

Installation is easy via pip. The install will require ``behave`` and ``selenium``.::

    pip install behave-webdriver

Using webdrivers
----------------

Selenium requires that you provide executables for the webdriver you want to use. Further, unless you specify the path to
the binary explicitly, selenium expects that this executable is in PATH. See these
`driver installation notes`_ for more details.


Usage
=====

Basic usage of this library with behave requires the following steps:

1. write your feature file
2. import the step implementations
3. set the ``behave_driver`` attribute on the behave ``context`` in your ``environment.py`` file.
4. run ``behave``


Writing the feature file
------------------------

.. code-block:: gherkin

    # my-minimal-project/features/myFeature.feature
    Feature: Sample Snippets test
    As a developer
    I should be able to use given text snippets

    Scenario: open URL
        Given the page url is not "http://webdriverjs.christian-bromann.com/"
        And   I open the url "http://webdriverjs.christian-bromann.com/"
        Then  I expect that the url is "http://webdriverjs.christian-bromann.com/"
        And   I expect that the url is not "http://google.com"


    Scenario: click on link
        Given the title is not "two"
        And   I open the url "http://webdriverjs.christian-bromann.com/"
        When  I click on the link "two"
        Then  I expect that the title is "two"


Importing the step implementations
----------------------------------

In order for your feature file steps to match our step implementations, behave needs to find them in your project.
This is as simple as importing our step definitions into your own step implementation file.

.. code-block:: python

   # features/steps/webdriver_example.py
   from behave_webdriver.steps import *


For more information about `step implementations`_, see the behave tutorial.


Set behave_driver in the environment
------------------------------------

Our step implementations specifically look at the behave context for a ``behave_driver`` attribute to use to run your tests.
In order for that to work, you'll have to provide this attribute in your ``environment.py`` file.

.. code-block:: python

   # features/environment.py
   import behave_webdriver

   def before_all(context):
       context.behave_driver = behave_webdriver.Chrome()

   def after_all(context):
       # cleanup after tests run
       context.behave_driver.quit()


The webdriver classes provided by behave-webdriver inherit from selenium's webdriver classes, so they will accept all
same positional and keyword arguments that selenium accepts.

Some webdrivers, such as Chrome, provide special classmethods like ``Chrome.headless`` which instantiates ``Chrome`` with
options to run headless. This is useful, for example in headless testing environments.

.. code-block:: python

   def before_all(context):
       context.behave_driver = behave_webdriver.Chrome.headless()


Using a fixture
^^^^^^^^^^^^^^^

*New in 0.1.1*

You may also find it convenient to use a fixture to setup your driver as well. For example, to use our fixture with Firefox

.. code-block:: python

    from behave_webdriver.fixtures import fixture_browser
    def before_all(context):
        use_fixture(fixture_browser, context, webdriver='Firefox')

This will also ensure that the browser is torn down at the corresponding `cleanup point`_.

.. _cleanup point: http://behave.readthedocs.io/en/stable/fixtures.html#fixture-cleanup-points


Run behave
----------

Then run the tests, just like any other behave test

.. code-block:: bash

    behave

You should then see an output as follows::

    Feature: Sample Snippets test # features/myFeature.feature:2
      As a developer
      I should be able to use given text snippets
      Scenario: open URL                                                          # features/myFeature.feature:6
        Given the page url is not "http://webdriverjs.christian-bromann.com/"     # ../../behave_webdriver/steps/given.py:136 0.012s
        And I open the url "http://webdriverjs.christian-bromann.com/"            # ../../behave_webdriver/steps/given.py:10 1.414s
        Then I expect that the url is "http://webdriverjs.christian-bromann.com/" # ../../behave_webdriver/steps/then.py:102 0.007s
        And I expect that the url is not "http://google.com"                      # ../../behave_webdriver/steps/then.py:102 0.007s

      Scenario: click on link                                          # features/myFeature.feature:13
        Given the title is not "two"                                   # ../../behave_webdriver/steps/given.py:81 0.006s
        And I open the url "http://webdriverjs.christian-bromann.com/" # ../../behave_webdriver/steps/given.py:10 0.224s
        When I click on the link "two"                                 # ../../behave_webdriver/steps/when.py:21 0.622s
        Then I expect that the title is "two"                          # ../../behave_webdriver/steps/then.py:10 0.006s

    1 feature passed, 0 failed, 0 skipped
    2 scenarios passed, 0 failed, 0 skipped
    8 steps passed, 0 failed, 0 skipped, 0 undefined
    Took 0m2.298s

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

.. code-block:: 

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


Getting help ⛑
--------------

If you have any unanswered questions or encounter any issues, please feel welcome to raise an issue. We recognize that
testers come in all different shapes, sizes, and backgrounds. We welcome any and all questions that may arise from using
this library.

Contributing
------------

Contributions are very much welcomed! If you have ideas or suggestions, please raise an issue or submit a PR.

List of step definitions 📝
===========================

We support all the steps supported by webdriverio/cucumber-boilerplate.
We also support some additional niceties and plan to add more step definitions.


Given Steps 👷
--------------

- ``I open the site "([^"]*)?"``
- ``I open the url "([^"]*)?"``
- ``I have a screen that is ([\d]+) by ([\d]+) pixels``
- ``I have a screen that is ([\d]+) pixels (broad|tall)``
- ``I have closed all but the first (window|tab)``
- ``I pause for (\d+)*ms``
- ``a (alertbox|confirmbox|prompt) is( not)* opened``
- ``the base url is "([^"]*)?"``
- ``the checkbox "([^"]*)?" is( not)* checked``
- ``the cookie "([^"]*)?" contains( not)* the value "([^"]*)?"``
- ``the cookie "([^"]*)?" does( not)* exist``
- ``the element "([^"]*)?" contains( not)* the same text as element "([^"]*)?"``
- ``the element "([^"]*)?" is( not)* ([\d]+)px (broad|tall)``
- ``the element "([^"]*)?" is( not)* empty``
- ``the element "([^"]*)?" is( not)* enabled``
- ``the element "([^"]*)?" is( not)* positioned at ([\d]+)px on the (x|y) axis``
- ``the element "([^"]*)?" is( not)* selected``
- ``the element "([^"]*)?" is( not)* visible``
- ``the element "([^"]*)?"( not)* contains any text``
- ``the element "([^"]*)?"( not)* contains the text "([^"]*)?"``
- ``the element "([^"]*)?"( not)* matches the text "([^"]*)?"``
- ``the page url is( not)* "([^"]*)?"``
- ``the title is( not)* "([^"]*)?"``
- ``the( css)* attribute "([^"]*)?" from element "([^"]*)?" is( not)* "([^"]*)?"``
- ``there is (an|no) element "([^"]*)?" on the page``



When Steps ▶️
-------------

- ``I open the site "([^"]*)?"``
- ``I open the url "([^"]*)?"``
- ``I accept the (alertbox|confirmbox|prompt)``
- ``I add "{value}" to the inputfield "{element}"``
- ``I clear the inputfield "{element}"``
- ``I click on the button "{element}"``
- ``I click on the element "{element}"``
- ``I click on the link "{link_text}"``
- ``I close the last opened (tab|window)``
- ``I delete the cookie "{cookie_key}"``
- ``I dismiss the (alertbox|confirmbox|prompt)``
- ``I doubleclick on the element "{element}"``
- ``I drag element "{from_element}" to element "{to_element}"``
- ``I enter "([^"]*)?" into the (alertbox|confirmbox|prompt)``
- ``I focus the last opened (tab|window)``
- ``I move to element "{element}" with an offset of {x_offset:d},{y_offset:d}``
- ``I move to element "{element}"``
- ``I pause for {milliseconds:d}ms``
- ``I press "{key}"``
- ``I scroll to element "{element}"``
- ``I select the option with the (text|value|name) "([^"]*)?" for element "([^"]*)?"``
- ``I select the {nth} option for element "{element}"``
- ``I set "{value}" to the inputfield "{element}"``
- ``I set a cookie "{cookie_key}" with the content "{value}"``
- ``I submit the form "{element}"``

Then Steps ✔️
-------------

- ``I expect the screen is ([\d]+) by ([\d]+) pixels``
- ``I expect a new (window|tab) has( not)* been opened``
- ``I expect that a (alertbox|confirmbox|prompt) is( not)* opened``
- ``I expect that a (alertbox|confirmbox|prompt)( not)* contains the text "([^"]*)?"``
- ``I expect that checkbox "([^"]*)?" is( not)* checked``
- ``I expect that cookie "([^"]*)?"( not)* contains "([^"]*)?"``
- ``I expect that cookie "([^"]*)?"( not)* exists``
- ``I expect that element "([^"]*)?" (has|does not have) the class "([^"]*)?"``
- ``I expect that element "([^"]*)?" becomes( not)* visible``
- ``I expect that element "([^"]*)?" does( not)* exist``
- ``I expect that element "([^"]*)?" is( not)* ([\d]+)px (broad|tall)``
- ``I expect that element "([^"]*)?" is( not)* empty``
- ``I expect that element "([^"]*)?" is( not)* enabled``
- ``I expect that element "([^"]*)?" is( not)* focused``
- ``I expect that element "([^"]*)?" is( not)* positioned at ([\d]+)px on the (x|y) axis``
- ``I expect that element "([^"]*)?" is( not)* selected``
- ``I expect that element "([^"]*)?" is( not)* visible``
- ``I expect that element "([^"]*)?" is( not)* within the viewport``
- ``I expect that element "([^"]*)?"( not)* contains any text``
- ``I expect that element "([^"]*)?"( not)* contains the same text as element "([^"]*)?"``
- ``I expect that element "([^"]*)?"( not)* contains the text "([^"]*)?"``
- ``I expect that element "([^"]*)?"( not)* matches the text "([^"]*)?"``
- ``I expect that the path is( not)* "([^"]*)?"``
- ``I expect that the title is( not)* "([^"]*)?"``
- ``I expect that the url is( not)* "([^"]*)?"``
- ``I expect that the( css)* attribute "([^"]*)?" from element "([^"]*)?" is( not)* "([^"]*)?"``
- ``I expect the url "([^"]*)?" is opened in a new (tab|window)``
- ``I expect the url to( not)* contain "([^"]*)?"``
- ``I wait on element "([^"]*)?"(?: for (\d+)ms)*(?: to( not)* (be checked|be enabled|be selected|be visible|contain a text|contain a value|exist))*``


Acknowledgements ❤️
===================

Special thanks to the authors and contributors of the `webdriverio/cucumber-boilerplate`_ project

Special thanks to the authors and contributors of `behave`_




.. _selenium-requests: https://github.com/cryzed/Selenium-Requests

.. _environment controls: http://behave.readthedocs.io/en/stable/tutorial.html#environmental-controls

.. _fixtures: http://behave.readthedocs.io/en/stable/fixtures.html

.. _step implementations: http://behave.readthedocs.io/en/stable/tutorial.html#python-step-implementations

.. _driver installation notes: http://selenium-python.readthedocs.io/installation.html#drivers

.. _behave-webdriver documentation: http://behave-webdriver.readthedocs.io/en/stable/

.. _selenium: https://github.com/SeleniumHQ/selenium

.. _behave: https://github.com/behave/behave

.. _webdriverio/cucumber-boilerplate: https://github.com/webdriverio/cucumber-boilerplate



.. |docs| image:: https://readthedocs.org/projects/behave-webdriver/badge/?version=stable
    :target: http://behave-webdriver.readthedocs.io/en/stable/

.. |status| image:: https://travis-ci.org/spyoungtech/behave-webdriver.svg?branch=master
    :target: https://travis-ci.org/spyoungtech/behave-webdriver

.. |version| image:: https://img.shields.io/pypi/v/behave-webdriver.svg?colorB=blue
    :target: https://pypi.org/project/behave-webdriver/

.. |pyversions| image:: https://img.shields.io/pypi/pyversions/behave-webdriver.svg?
    :target: https://pypi.org/project/behave-webdriver/

.. |coverage| image:: https://coveralls.io/repos/github/spyoungtech/behave-webdriver/badge.svg
    :target: https://coveralls.io/github/spyoungtech/behave-webdriver

