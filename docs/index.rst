.. behave-webdriver documentation master file, created by
   sphinx-quickstart on Tue Oct 17 09:40:19 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to behave-webdriver's documentation!
============================================

behave-webdriver
----------------

behave-webdriver is a step library intended to allow users to easily run browser automation tests (via `selenium`_)
with the `behave`_ BDD testing framework.

.. _selenium: https://github.com/SeleniumHQ/selenium
.. _behave: https://github.com/behave/behave

Inspired by, the webdriverio `cucumber-boilerplate`_ project.

.. _cucumber-boilerplate: https://github.com/webdriverio/cucumber-boilerplate

.. toctree::
   :maxdepth: 2

   installation
   quickstart
   api
   steps
   examples
   browsers
   roadmap



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`



Goals
-----

* Make writing readable browser automation tests as Gherkin features easy.
* Provide an easily extensible interface to the selenium driver (``BehaveDriver``)
* To be (at least mostly) compatible with feature files written for `webdriverio/cucumber-boilerplate`_


Status
------

|version| |pyversions| |status|

We currently test against Python2.7 and Python3.5+ using headless chrome. While all selenium's webdrivers are provided,
they are not all supported at this time. We plan to add support for additional browsers in the future.







.. _raise an issue: https://github.com/spyoungtech/behave-webdriver/issues/new


.. _selenium-requests: https://github.com/cryzed/Selenium-Requests

.. _environment controls: http://behave.readthedocs.io/en/latest/tutorial.html#environmental-controls

.. _fixtures: http://behave.readthedocs.io/en/latest/fixtures.html

.. _step implementations: http://behave.readthedocs.io/en/latest/tutorial.html#python-step-implementations

.. _driver installation notes: http://selenium-python.readthedocs.io/installation.html#drivers

.. _behave-webdriver documentation: http://behave-webdriver.readthedocs.io/en/latest/

.. _selenium: https://github.com/SeleniumHQ/selenium

.. _behave: https://github.com/behave/behave

.. _webdriverio/cucumber-boilerplate: https://github.com/webdriverio/cucumber-boilerplate



.. |docs| image:: https://readthedocs.org/projects/behave-webdriver/badge/?version=latest
    :target: http://behave-webdriver.readthedocs.io/en/latest/

.. |status| image:: https://travis-ci.org/spyoungtech/behave-webdriver.svg?branch=master
    :target: https://travis-ci.org/spyoungtech/behave-webdriver

.. |version| image:: https://img.shields.io/pypi/v/behave-webdriver.svg?colorB=blue
    :target: https://pypi.org/project/behave-webdriver/

.. |pyversions| image:: https://img.shields.io/pypi/pyversions/behave-webdriver.svg?
    :target: https://pypi.org/project/behave-webdriver/

.. |coverage| image:: https://coveralls.io/repos/github/spyoungtech/behave-webdriver/badge.svg
    :target: https://coveralls.io/github/spyoungtech/behave-webdriver
