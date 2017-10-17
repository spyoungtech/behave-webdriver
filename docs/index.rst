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

Inspired heavily by, and borrows many ideas from, the webdriverio `cucumber-boilerplate`_ project.

.. _cucumber-boilerplate: https://github.com/webdriverio/cucumber-boilerplate


.. figure:: https://travis-ci.org/spyoungtech/behave-webdriver.svg?branch=master
   :target: https://travis-ci.org/spyoungtech/behave-webdriver


Goals
-----

* Make writing readable browser automation tests as Gherkin features easy.
* Provide an easily extensible interface to the selenium driver (`BehaveDriver`)
* To be (at least mostly) compatible with feature files written for cucumber/webdriverio


Status
------

This project is in early phases of development and wide open to contributions.
If have an idea or would like to see a change, no matter how large or small, please submit an issue on Github.

.. toctree::
   :maxdepth: 2

   installation
   quickstart
   api
   steps



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
