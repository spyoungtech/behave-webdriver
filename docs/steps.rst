========================
List of predefined steps
========================



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
