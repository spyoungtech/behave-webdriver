# Created by spenceryoung at 3/2/2018
Feature: Test Multiple Select elements
  As a developer
  I want to be able to test if certain elements in a multiple select field are selected

  Background:
    Given I open the site "/page.html"
    Then I expect that element "#yes" is not selected
    Then I expect that element "#yes2" is not selected
    Then I expect that element "#no" is not selected
    Then I expect that element "#affirmative" is not selected
    Then I expect that element "#negative" is not selected

  Scenario: Test if multiple values are selected by text
    When I select the option with the text "Yes" for element "#selectElementTest"
    Then I expect that element "#yes" is selected
    And I expect that element "#yes2" is selected
    And I expect that element "#no" is not selected
    And I expect that element "#affirmative" is not selected
    And I expect that element "#negative" is not selected

  Scenario: Test is multiple values are selected by value
    When I select the option with the value "1" for element "#selectElementTest"
    Then I expect that element "#yes" is selected
    And I expect that element "#affirmative" is selected
    And I expect that element "#yes2" is not selected
    And I expect that element "#no" is not selected
    And I expect that element "#negative" is not selected

  Scenario: Trying to select non-existant elements raises an error
    Then I expect that executing the step 'When I select the option with the name "x" for element "#selectElementTest"' raises an exception
