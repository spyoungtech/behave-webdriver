Feature: Screen Size
  As a developer
  I want to be able to check and modify the screen size

  Background:
    Given I have a screen that is 600 by 500 pixels

  Scenario: change the screen size
    Given I have a screen that is 500 by 420 pixels
    Then I expect the screen is 500 by 420 pixels

  Scenario: Change just Y dimension
    Given I have a screen that is 700 pixels tall
    Then I expect the screen is 600 by 700 pixels

  Scenario: Change just X dimension
    Given I have a screen that is 700 pixels broad
    Then I expect the screen is 700 by 500 pixels
