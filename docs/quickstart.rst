Quickstart
==========

Ready to get started testing? This page will give you a quick introduction to behave-webdriver and how to use it. This
assumes you have installed behave-webdriver and a webdriver on PATH. We also assume you got at least some familiarity
with BDD/behave. If you're brand new to BDD in Python, you may want to check out the `behave docs`_  first.

.. _behave docs: http://behave.readthedocs.io/en/latest/

Basic usage of this library with behave requires the following steps:

1. import the step implementations
2. set the ``behave_driver`` attribute on the behave ``context`` in your ``environment.py`` file.
3. write your feature file
4. run ``behave``

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

In the future, behave-webdriver will provide `fixtures`_ for the setup and teardown of webdrivers.
See the behave tutorial for more information about `environment controls`_ .

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

Congratulations, you've just implemented a behavior-driven test without having to write a single step implementation!

.. _environment controls: http://behave.readthedocs.io/en/latest/tutorial.html#environmental-controls

.. _fixtures: http://behave.readthedocs.io/en/latest/fixtures.html

.. _step implementations: http://behave.readthedocs.io/en/latest/tutorial.html#python-step-implementations
