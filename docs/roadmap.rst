Roadmap
=======

Loosely organized collection of goals/milestones and ideas. Nothing here is necessarily concrete, but should give you an
idea of where our heads are at for the development of behave-webdriver.

You can help steer our roadmap in the right direction with suggestions, feedback, and other contributions. Please don't
hesitate to `raise an issue`_ on Github.


Immediate and Short Term
------------------------

Immediate and short term goals are some milestones that we are actively working on or in our immediate forefront for development.
Ideally, these things have clearly defined requirements and some work in progress.



Documentation; recipes & tutorials
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

While documentation is something we'll be working on perpetually through development,
we are particularly motivated on immediately providing at least some brief tutorials and recipes.



Medium Term
-----------

Medium term goals are things we are committed to working on and implementing in the not-so-distant future.
Ideally, this means we're working on these things passively and have at least a basic plan for the implementation.


Device emulation
^^^^^^^^^^^^^^^^

We want to provide support for steps that use device emulation features of drivers that support this. E.g. steps like
``Given I am using an iPhone 6``, ``Given I am using a Pixel 2``,  etc.



More step definitions
^^^^^^^^^^^^^^^^^^^^^

We plan to implement additional step definitions to perform more actions with selenium and provide more robust
interfaces for testing and automation. This will include things like taking & saving screenshots, retrieving/saving page source, and more.

If you have ideas for step definitions you'd like to see implemented, `raise an issue`_ on Github. These contributions
are welcomed and very much appreciated.

Browser support (others)
^^^^^^^^^^^^^^^^^^^^^^^^

Chrome and Firefox are in our forefront for browser support. We do however plan to test and provide best-effort
support for all the webdrivers supported by selenium.

We hope to get all browsers tested (but not necessarily passing) and attempt to make note of compatibility, behavior differences, and other browser-specific quirks.

Would be nice to have more browsers tested in the CI builds as well.

See :doc:`browsers` for more information.



Long Term, ongoing, and Ideas
-----------------------------

These are some loose long-term milestones or ideas (which may or may not materialize) we have for the future.
These are things that we would probably like to do, but have probably not put much effort into implementation or detailed plans.
Anything we are remotely considering, but have not committed to, will be here, too.

Assertion matcher
^^^^^^^^^^^^^^^^^

Currently, standard python assertions are used. In the future, we may opt to use an assertion matching library such as
pyhamcrest. Some time and effort will need to be put in to research a good choice in this area.


Parallel support
^^^^^^^^^^^^^^^^

While behave itself is planning to add parallel runner support in the future, its unlikely this will work well for
browser testing. As such, we have this parallel support in the back of our minds, but it will probably be some time before
it is introduced in a stable release.


Use of other selenium libraries
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

It may be possible for us to take advantage of previous work in this area, for example requestium, to enhance behave-webdriver.
We want to explore these possibilities.


Survey & reflection - path to a stable release
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

While a stable (LTS) release itself is more of a long-term goal, we are constantly surveying the behave landscape and reviewing our API.
We've made (what we feel are good) decisions in the design of behave-webdriver, but there's always room for improvement.
Now particularly is a good time for us to ensure we are laying down a solid foundation to build upon for the future.

Your feedback is immensely valuable in this regard and is sincerely appreciated.
The best way to make suggestions or general comments is to `raise an issue`_ on Github.




Better tests (ongoing)
^^^^^^^^^^^^^^^^^^^^^^

Our github README boasts its coverage with a shiny badge from coveralls. The truth is that coverage isn't everything. There's undoubtedly cases
where functionality is broken or doesn't work quite as expected. We want to find those to build better test cases, and
improve the functionality of the library as a whole.




Completed
---------

Browser support (Firefox)
^^^^^^^^^^^^^^^^^^^^^^^^^

Firefox is officially supported as of v0.1.1

v0.1.0
^^^^^^

Complete™ support with Google Chrome. We use the feature files (with modifications or additons in some cases) from
cucumber-boilerplate as acceptance tests. While this is bound to be imperfect, it's a great start for v0.1


Deferred
--------

Deferred items are things we previously comitted to but, for some reason or another, have placed on the backburner or
suspended entirely.

PhantomJS support
^^^^^^^^^^^^^^^^^

While we will continue to provide best-effort support for all browsers, including PhantomJS, because PhantomJS has been
deprecated for selenium and `phantomJS development has been suspended`_, PhantomJS is now a low priority.

.. _raise an issue: https://github.com/spyoungtech/behave-webdriver/issues/new


.. _phantomJS development has been suspended: https://github.com/ariya/phantomjs/issues/15344
