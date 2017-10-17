Quickstart
==========

Ready to get started testing? This page will give you a quick introduction to behave-webdriver and how to use it. This
assumes you have installed behave-webdriver and a webdriver on PATH. We also assume you got at least some familiarity
with BDD/behave. If you're brand new to BDD in Python, you may want to check out the `behave docs`_  first.

.. _behave docs: http://behave.readthedocs.io/en/latest/


Application Setup
-----------------

We'll run through setting up the bare necessities for running your first tests with behave-webdriver. For the impatient,
 you can also find this example in the `examples` from the github repository.

environment.py
^^^^^^^^^^^^^^

For behave-webdriver to work, you'll need to add some setup code in your `environment.py` file to set the
`behave_driver` attribute in your context. Typically, this is done in the a `before_all` function. Additionally, we'll
include some teardown logic in an `after_all` function.

.. code-block:: python

    # my-minimal-project/features/environment.py
    from behave_webdriver import BehaveDriver

    def before_all(context):
        context.behave_driver = BehaveDriver.chrome()

    def after_all(context):
        context.behave_driver.quit()

.. hint::
    You can supply any arguments that a given webdriver would normally take to any of the alternative browser constructors
    .. code-block:: python

        context.behave_driver = BehaveDriver.headless_chrome(executable_path='/path/to/chromedriver')

    You don't need to use the builtin browsers, either. You can also supply your own selenium webdriver instance to `BehaveDriver`
    .. code-block:: python

        from selenium import webdriver
        from behave_webdriver import BehaveDriver
        my_driver = webdriver.Firefox()

        def before_all(context):
            context.behave_driver = BehaveDriver(my_driver)

Import the step definitions
^^^^^^^^^^^^^^^^^^^^^^^^^^^
To use behave-webdriver's step definitions, you'll need to import them.

.. code-block:: python

    # my-minimal-project/features/steps/my_steps.py
    from behave_webdriver.steps import *

This is enough to be able to use all the steps provided by behave_webdriver.

Feature file
^^^^^^^^^^^^
The following is a snippet of a feature file that utilizes a few of the step definitions provided by behave-webdriver.

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

Running the tests
-----------------

Recap: we've created a minimal application structure with the content from the previous section. If you're following
the example, you should have a directory tree that looks something like this::

    └── my-minimal-project
        └── features
            ├── myFeature.feature
            └── steps
                └── my_steps.py

With this in place, we can now run the tests, just like any other behave test, from the working directory
`my-minimal-project`

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