.. _api:

==============================
behave-webdriver API Reference
==============================

This reference is meant for those who want to develop upon, extend, or alter the behavior of behave-webdriver. This
will contain information regarding the implementation of various methods. Many aspects of the BehaveDriver class deal
closely with selenium webdriver instances, but this document will refrain from duplicating information that should be
contained in the selenium documentation.

behave-webdriver is designed with **you** in-mind. You are free to extend the behavior of our webdriver classes to suit your
unique needs. You can subclass our webdriver classes, use a custom selenium webdriver, write your own mixin, or use
a mixin somebody else provides for selenium.

.. warning::

    While every effort is made to not make breaking changes, until a stable release, expect some things here to change, including breaking changes.



The webdriver classes
---------------------

behave-webdriver provides each of the same webdriver classes provided in ``selenium.webdriver``. Each class inherits from the :py:class:`~behave_webdriver.driver.BehaveDriverMixin`
mixin as well as the respective ``selenium`` counterpart class.

.. autoclass:: behave_webdriver.Chrome
   :members:

.. autoclass:: behave_webdriver.Firefox
   :members:

.. autoclass:: behave_webdriver.Ie
   :members:

.. autoclass:: behave_webdriver.Safari
   :members:

.. autoclass:: behave_webdriver.PhantomJS
   :members:

.. autoclass:: behave_webdriver.Edge
   :members:

.. autoclass:: behave_webdriver.Opera
   :members:

.. autoclass:: behave_webdriver.BlackBerry
   :members:

.. autoclass:: behave_webdriver.Android
   :members:

.. autoclass:: behave_webdriver.Remote
   :members:


The BehaveDriverMixin
---------------------

The mixin class implements all of the general logic. If you want to alter how behave-webdriver behaves, this is probably the place to do it.


.. autoclass:: behave_webdriver.driver.BehaveDriverMixin
   :members:
