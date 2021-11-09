Feature: Base URL configuration supports parameter transformation
  As a developer
  I should be able to change the base URL for opening pages
  And I should be able to replace hardcoded values with parameters.

  # {BASE_URL} / {ALT_BASE_URL} are transformed by transformer provided in environment.py
  # As long the URLs are valid, this test should still work even if the test url is not available at those urls.
  Scenario: Default base is http://localhost:8000/
    When I open the site "/"
    Then I expect that the url is "{BASE_URL}/"

  Scenario: Change the base url to http://127.0.0.1:8000/
    Given the base url is "{ALT_BASE_URL}/"
    When I open the site "/page.html"
    Then I expect that the url is "{ALT_BASE_URL}/page.html"
    And I expect that the url is not "{BASE_URL}/page.html"
