# behave-webdriver
behave-webdriver is a step library intended to allow users to easily write [selenium](https://github.com/SeleniumHQ/selenium) 
webdriver tests with the [behave](https://github.com/behave/behave) BDD testing framework.  
Inspired heavily by the webdriverio [cucumber-boilerplate](https://github.com/webdriverio/cucumber-boilerplate) project.

[![Documentation](https://readthedocs.org/projects/behave-webdriver/badge/?version=latest)](http://behave-webdriver.readthedocs.io/en/latest/)
[![Build Status](https://travis-ci.org/spyoungtech/behave-webdriver.svg?branch=master)](https://travis-ci.org/spyoungtech/behave-webdriver)
[![PyPI Version](https://img.shields.io/pypi/v/behave-webdriver.svg?colorB=blue)](https://pypi.org/project/behave-webdriver/)
[![Python Versions](https://img.shields.io/pypi/pyversions/behave-webdriver.svg?)](https://pypi.org/project/behave-webdriver/)
[![Coverage Status](https://coveralls.io/repos/github/spyoungtech/behave-webdriver/badge.svg)](https://coveralls.io/github/spyoungtech/behave-webdriver)

For more details, see the  [behave-webdriver documentation](http://behave-webdriver.readthedocs.io/en/latest/) 

![behave-webdriver](https://raw.githubusercontent.com/spyoungtech/behave-webdriver/master/docs/_static/behave-webdriver.gif)

# Installation

Installation is easy via pip. The install will require `behave` and `selenium`.

```
pip install behave-webdriver
```

## Using webdrivers :traffic_light:

Selenium requires that you provide executables for the webdriver you want to use. Further, unless you specify the path to 
the binary explicitly, selenium expects that this executable is in PATH. See [this article](http://selenium-python.readthedocs.io/installation.html#drivers) for more information.

You can download the latest chromedriver for your 
platform from the [chromium.org downloads page](https://sites.google.com/a/chromium.org/chromedriver/downloads).

# Quick start :running:

Basic usage of this library with behave requires the following steps: 

1. import the step implementations
2. set the `behave_driver` attribute on the behave `context` in your `environment.py` file.


### Importing the step implementations

In order for your feature file steps to match our step implementations, behave needs to find them in your project.  
This is as simple as importing our step definitions into your own step implementation file.

```python
# features/steps/webdriver_example.py
from behave_webdriver.steps import *
```

For more information about step implementations, see the [behave tutorial](http://behave.readthedocs.io/en/latest/tutorial.html#python-step-implementations)


### Setting up the environment :hammer:

Our step implementations specifically look at the behave context for a `behave_driver` attribute to use to run your tests.  
In order for that to work, you'll have to provide this attribute in your `environment.py` file.


```python
# features/environment.py
import behave_webdriver

def before_all(context):
    context.behave_driver = behave_webdriver.Chrome()

def after_all(context):
    # cleanup after tests run
    context.behave_driver.quit()
```

The webdriver classes provided by behave-webdriver inherit from selenium's webdriver classes, so they will accept all 
same positional and keyword arguments that selenium accepts.

Some webdrivers, such as Chrome, provide special classmethods like `Chrome.headless` which instantiates `Chrome` with 
options to run headless. This is useful, for example in headless testing environments.

```python
def before_all(context):
    context.behave_driver = behave_webdriver.Chrome.headless()
```

See the behave tutorial for more information about [environment controls](http://behave.readthedocs.io/en/latest/tutorial.html#environmental-controls)


## Advanced usage; modifying/extending behave-webdriver

behave-webdriver is designed with you in-mind. You are free to extend the behavior of our webdriver classes to suit your 
unique needs. 

## Getting help :children_crossing:

If you have any unanswered questions or encounter any issues, please feel welcome to raise an issue. We recognize that 
testers come in all different shapes, sizes, and backgrounds. We welcome any and all questions that may arise from using 
this library.

## Contributing :busts_in_silhouette: :wrench:

Contributions are very much welcomed! If you have ideas or suggestions, please raise an issue or submit a PR.

# List of step definitions :memo:

We support all the steps supported by webdriverio/cucumber-boilerplate.  
We also support some additional niceties and plan to add more step definitions.

## Given Steps :contruction_worker:


- `I open the url "([^"]*)?"`
- `I open the site "([^"]*)?"`
- `the base url is "([^"]*)?"`
- `the element "([^"]*)?" is( not)* visible`
- `the element "([^"]*)?" is( not)* enabled`
- `the element "([^"]*)?" is( not)* selected`
- `the checkbox "([^"]*)?" is( not)* checked`
- `there is (an|no) element "([^"]*)?" on the page`
- `the title is( not)* "([^"]*)?"`
- `the element "([^"]*)?" contains( not)* the same text as element "([^"]*)?"`
- `the element "([^"]*)?"( not)* matches the text "([^"]*)?"`
- `the element "([^"]*)?"( not)* contains the text "([^"]*)?"`
- `the element "([^"]*)?"( not)* contains any text`
- `the element "([^"]*)?" is( not)* empty`
- `the page url is( not)* "([^"]*)?"`
- `the( css)* attribute "([^"]*)?" from element "([^"]*)?" is( not)* "([^"]*)?"`
- `the cookie "([^"]*)?" contains( not)* the value "([^"]*)?"`
- `the cookie "([^"]*)?" does( not)* exist`
- `the element "([^"]*)?" is( not)* ([\d]+)px (broad|tall)`
- `the element "([^"]*)?" is( not)* positioned at ([\d]+)px on the (x|y) axis`
- `I have a screen that is ([\d]+) by ([\d]+) pixels`
- `a (alertbox|confirmbox|prompt) is( not)* opened`
- `I have closed all but the first (window|tab)`

## When Steps :arrow_forward:


- `I pause for {miliseconds:d}ms`
- `I click on the element "{element}"`
- `I doubleclick on the element "{element}"`
- `I click on the link "{link_text}"`
- `I click on the button "{element}"`
- `I set "{value}" to the inputfield "{element}"`
- `I add "{value}" to the inputfield "{element}"`
- `I clear the inputfield "{element}"`
- `I drag element "{from_element}" to element "{to_element}"`
- `I submit the form "{element}"`
- `I set a cookie "{cookie_key}" with the content "{value}"`
- `I delete the cookie "{cookie_key}"`
- `I press "{key}"`
- `I accept the alert`
- `I dismiss the alert`
- `I enter "{text}" into the prompt`
- `I scroll to element "{element}"`
- `I move to element "{element}" with an offset of {x_offset:d},{y_offset:d}`
- `I move to element "{element}"`
- `I close the last opened tab`
- `I close the last opened window`
- `I select the {nth:d} option for element "{element}"`
- `I select the option with the text "{text}" for element "{element}"`
- `I select the option with the value "{value}" for element "{element}"`



## Then Steps :white_check_mark:


- `I expect that the title is( not)* "([^"]*)?"`
- `I expect that element "([^"]*)?" is( not)* visible`
- `I expect that element "([^"]*)?" becomes( not)* visible`
- `I expect that element "([^"]*)?" is( not)* within the viewport`
- `I expect that element "([^"]*)?" does( not)* exist`
- `I expect that element "([^"]*)?"( not)* contains the same text as element "([^"]*)?"`
- `I expect that element "([^"]*)?"( not)* matches the text "([^"]*)?"`
- `I expect that element "([^"]*)?"( not)* contains the text "([^"]*)?"`
- `I expect that element "([^"]*)?"( not)* contains any text`
- `I expect that element "([^"]*)?" is( not)* empty`
- `I expect that the url is( not)* "([^"]*)?"`
- `I expect that the path is( not)* "([^"]*)?"`
- `I expect the url to( not)* contain "([^"]*)?"`
- `I expect that the( css)* attribute "([^"]*)?" from element "([^"]*)?" is( not)* "([^"]*)?"`
- `I expect that checkbox "([^"]*)?" is( not)* checked`
- `I expect that element "([^"]*)?" is( not)* selected`
- `I expect that element "([^"]*)?" is( not)* enabled`
- `I expect that cookie "([^"]*)?"( not)* contains "([^"]*)?"`
- `I expect that cookie "([^"]*)?"( not)* exists`
- `I expect that element "([^"]*)?" is( not)* ([\d]+)px (broad|tall)`
- `I expect that element "([^"]*)?" is( not)* positioned at ([\d]+)px on the (x|y) axis`
- `I wait on element "([^"]*)?"(?: for (\d+)ms)*(?: to( not)* (be checked|be enabled|be selected|be visible|contain a text|contain a value|exist))*`
- `I expect that a (alertbox|confirmbox|prompt) is( not)* opened`
- `I expect that element "([^"]*)?" (has|does not have) the class "([^"]*)?"`
- `I expect that element "([^"]*)?" is( not)* focused`
- `I expect that a (alertbox|confirmbox|prompt)( not)* contains the text "([^"]*)?"`
- `I expect a new (window|tab) has( not)* been opened`
- `I expect the url "([^"]*)?" is opened in a new (tab|window)`


# Acknowledgements :heart:

Special thanks to the authors of the webdriverio [cucumber-boilerplate](https://github.com/webdriverio/cucumber-boilerplate) project for boilerplate ideas and feature files  
Special thanks to the authors of the [behave](https://github.com/behave/behave) for the BDD testing framework.