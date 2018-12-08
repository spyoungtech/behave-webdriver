Feature: Using a transformation fixture from feature file

  @fixture.transformer.EnvironmentFormatTransformer
  Scenario: transform step from environment variable
    Given the base url is "{ENV_BASE_URL}"
    When I open the site "/page.html"
    Then I expect that the url is "http://127.0.0.1:8000/page.html"