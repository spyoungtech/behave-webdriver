Feature: Using selenium-requests
  As a developer
  I should be able to extend behave-webdriver with selenium-requests


  Scenario: use selenium-requests with behave-webdriver
    Given the base url is "http://127.0.0.1:8000"
    Given I send a GET request to the page "/"
    Then I expect the response text contains "<h1>DEMO APP</h1>"
