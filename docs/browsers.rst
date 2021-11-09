Browser Support
===============

behave-webdriver is designed so that you *can* use any of the webdriver classes you would normally use with Selenium,
e.g. ``Chrome``, ``Firefox``, ``Remote``, etc... However, not all browsers were made equal and attempting to get identical
behavior across browsers is... complicated, if not impossible.

This document will aim to describe the status of support with the various webdrivers supported by Selenium. Where there
are known issues or quirks related to this step library, there will be an effort to document them here, too. Be sure to also checkout the
github issues and projects. browser-specific issues should be tagged accordingly.

More specifics may be revealed in the :doc:`api` and in the source. The ecosystem around selenium/webdrivers is huge.
This is not a repository or body of knowledge for all driver-related issues; just the ones that most directly affect this library.

Unless otherwise noted, we are referring to the latest stable release of Selenium and each respective browser and driver.
Keep in mind, this documentation may not necessarily be up-to-date with very recent releases.


Chrome (recommended)
--------------------

Currently, Chrome is essentially the reference implementation. We primarily discuss issues with other webdrivers with
respect to how Chrome behaves. In our experience so far, Chrome is the fastest and most well-behaving driver.

We recommend Chrome and fully support the use of the Chrome webdriver with the latest versions of selenium and chrome/chromedriver.
At the time of this writing (March 2018) that's selenium 3.10, Chrome 65, and chromedriver 2.36
While earlier versions should work fine and we are willing to support them, they are not tested.




Firefox (beta)
--------------

Firefox is officially supported as of v0.1.1




Known issues
^^^^^^^^^^^^

- ``submit`` on form elements is implemented by a (Selenium) JS shim and will not block for page load. Clicking the form button should block properly, however.
- support for window handles is somewhat problematic
- clicking elements requires they are in the viewport (we compensate for this by scrolling to an element before any click)
- moving to an element *with an offset* that is bigger than the viewport is not (yet) supported
- slower than Chrome

Workarounds/Shims
^^^^^^^^^^^^^^^^^

Shims and other workarounds for some known issues are implemented in the Firefox class.

See :doc:`api` for more details.


Ie
--

We have some preliminary support for Internet Explorer. It is tested in our `appveyor CI build`_.

.. _appveyor CI build: https://ci.appveyor.com/project/spyoungtech/behave-webdriver


Safari
------

We have some preliminary support for Safari on OSX/Mac OS. It is tested as part of our `Travis CI build`_ (failures currently allowed).

.. _Travis CI build: https://travis-ci.org/spyoungtech/behave-webdriver/



PhantomJS
---------


.. danger::
   Selenium support for PhantomJS has been deprecated and the `PhantomJS development has been suspended`_. As such,
   users are recommended to NOT use PhantomJS to begin with.

PhantomJS is a low priority (see above). Users should expect issues with PhantomJS when using modern versions of selenium,
and


Known issues
^^^^^^^^^^^^

- No support for alerts/modals
- Cookies are problematic (cookies must have domain (and expiry?); setting cookies for localdomain not supported)
- Memory-hungry
- Unsupported (see above)


.. _phantomJS development has been suspended: https://github.com/ariya/phantomjs/issues/15344


Remote
------

Remote is untested at this time.



Edge
----

Edge is untested at this time.

Opera
-----

Opera is untested at this time.


BlackBerry
----------

BlackBerry is untested at this time.

Android
-------

Android is untested at this time.
