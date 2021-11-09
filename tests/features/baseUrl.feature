Feature: Base URL configuration
  As a developer
  I should be able to change the base URL for opening pages.

  Scenario: Change the base url to http://127.0.0.1:8000/
    Given the base url is "http://127.0.0.1:8000/"
    When I open the site "/page.html"
    Then I expect that the url is "http://127.0.0.1:8000/page.html"
    And I expect that the url is not "http://localhost:8000/page.html"
