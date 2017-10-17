========================
List of predefined steps
========================



.. warning::

    This documentation is a pre-release work-in-progress. Most, but not all, steps here have working/tested
    implementations behind them.


Given
=====

* ``I open the url "([^"]*)?"``
* ``I open the site "([^"]*)?"``
* ``the base url is "([^"]*)?"``
* ``the element "([^"]*)?" is( not)* visible``
* ``the element "([^"]*)?" is( not)* enabled``
* ``the element "([^"]*)?" is( not)* selected``
* ``the checkbox "([^"]*)?" is( not)* checked``
* ``there is (an|no) element "([^"]*)?" on the page``
* ``the title is( not)* "([^"]*)?"``
* ``the element "([^"]*)?" contains( not)* the same text as element "([^"]*)?"``
* ``the element "([^"]*)?"( not)* matches the text "([^"]*)?"``
* ``the element "([^"]*)?"( not)* contains the text "([^"]*)?"``
* ``the element "([^"]*)?"( not)* contains any text``
* ``the element "([^"]*)?" is( not)* empty``
* ``the page url is( not)* "([^"]*)?"``
* ``the( css)* attribute "([^"]*)?" from element "([^"]*)?" is( not)* "([^"]*)?"``
* ``the cookie "([^"]*)?" contains( not)* the value "([^"]*)?"``
* ``the cookie "([^"]*)?" does( not)* exist``
* ``the element "([^"]*)?" is( not)* ([\d]+)px (broad|tall)``
* ``the element "([^"]*)?" is( not)* positioned at ([\d]+)px on the (x|y) axis``
* ``I have a screen that is ([\d]+) by ([\d]+) pixels``

* ``I have closed all but the first (window|tab)``



When
====

* ``I pause for {miliseconds:d}ms``
* ``I click on the element "{element}"``
* ``I doubleclick on the element "{element}"``
* ``I click on the link "{link_text}"``
* ``I click on the button "{element}"``
* ``I set "{value}" to the inputfield "{element}"``
* ``I set {value} to the inputfield "{element}"``
* ``I add "{value}" to the inputfield "{element}"``
* ``I clear the inputfield "{element}"``
* ``I drag element "{from_element}" to element "{to_element}"``
* ``I submit the form "{element}"``
* ``I set a cookie "{cookie_key}" with the content "{value}"``
* ``I delete the cookie "{cookie_key}``
* ``I press "{key}"``
* ``I accept the alert``
* ``I dismiss the alert``
* ``I enter {text} into the prompt``
* ``I scroll to element {element}``
* ``I move to element "{element}" with an offset of {x_offset:d},{y_offset:d}``
* ``I move to element "{element}"``

* ``I close the last opened tab``
* ``I close the last opened window``
* ``I select the {nth:d} option for element "{element}"``
* ``I select the option with the text {text} for element {element}``
* ``I select the option with the value {value} for element {element}``


Then
====

* ``I expect that the title is( not)* "([^"]*)?"``
* ``I expect that element "([^"]*)?" is( not)* visible``
* ``I expect that element "([^"]*)?" becomes( not)* visible``
* ``I expect that element "([^"]*)?" is( not)* within the viewport``
* ``I expect that element "([^"]*)?" does( not)* exist``
* ``I expect that element "([^"]*)?"( not)* contains the same text as element "([^"]*)?"``
* ``I expect that element "([^"]*)?"( not)* matches the text "([^"]*)?"``
* ``I expect that element "([^"]*)?"( not)* contains the text "([^"]*)?"``
* ``I expect that element "([^"]*)?"( not)* contains any text``
* ``I expect that element "([^"]*)?" is( not)* empty``
* ``I expect that the url is( not)* "([^"]*)?"``
* ``I expect that the path is( not)* "([^"]*)?"``
* ``I expect the url to( not)* contain "([^"]*)?"``
* ``I expect that the( css)* attribute "([^"]*)?" from element "([^"]*)?" is( not)* "([^"]*)?"``
* ``I expect that checkbox "([^"]*)?" is( not)* checked``
* ``I expect that element "([^"]*)?" is( not)* selected``
* ``I expect that element "([^"]*)?" is( not)* enabled``
* ``I expect that cookie "([^"]*)?"( not)* contains "([^"]*)?"``
* ``I expect that cookie "([^"]*)?"( not)* exists``
* ``I expect that element "([^"]*)?" is( not)* ([\d]+)px (broad|tall)``
* ``I expect that element "([^"]*)?" is( not)* positioned at ([\d]+)px on the (x|y) axis``
* ``I wait on element "([^"]*)?"(?: for (\d+)ms)*(?: to( not)* (be checked|be enabled|be selected|be visible|contain a text|contain a value|exist))*``
* ``I expect that a (alertbox|confirmbox|prompt) is( not)* opened``
* ``I expect that element "([^"]*)?" (has|does not have) the class "([^"]*)?"``

* ``I expect a new (window|tab) has( not)* been opened``
* ``I expect the url "([^"]*)?" is opened in a new (tab|window)``
* ``I expect that element "([^"]*)?" is( not)* focused``
* ``I expect that a (alertbox|confirmbox|prompt)( not)* contains the text "([^"]*)?"``
