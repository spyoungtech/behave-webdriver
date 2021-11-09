  # minimal-project/features/myFeature.feature
  Feature: Sample Snippets test
  As a developer
  I should be able to use given text snippets

  Scenario: open URL
      Given the page url is not "http://webdriverjs.christian-bromann.com/"
      And   I open the url "http://webdriverjs.christian-bromann.com/"
      Then  I expect that the url is "http://webdriverjs.christian-bromann.com/"
      And   I expect that the url is not "http://google.com"


  Scenario: click on link
      Given the title is not "two"
      And   I open the url "http://webdriverjs.christian-bromann.com/"
      When  I click on the link "two"
      Then  I expect that the title is "two"
