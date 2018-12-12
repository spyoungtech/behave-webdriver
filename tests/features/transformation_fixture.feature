Feature: Using a transformation fixture from feature file

  @fixture.transformer.EnvironmentTransformer
  Scenario: transform step from environment variable
    Given the base url is "{ENV_BASE_URL}"
    When I open the site "/page.html"
    Then I expect that the url is "{ENV_BASE_URL}page.html"
