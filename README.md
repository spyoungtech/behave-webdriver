# behave-webdriver
Boilerplate to easily run [selenium](https://github.com/SeleniumHQ/selenium) webdriver tests with the [behave](https://github.com/behave/behave) BDD testing framework
Inspired by the webdriverio [cucumber-boilerplate](https://github.com/webdriverio/cucumber-boilerplate) project.

# Goal
Make writing readable selenium tests as Gherkin features easy.
Implement features from webdriverio-cucumber-boilerplate project
Provide an easily extensible interface to the selenium driver


# Status

This project is currently in the very early stages of development, but is being worked on regularly. A formal release will be forthcoming.

The current travis tests test a base set of features.

## Installing and running the tests

<aside class="notice">
For now, the tests use headless chrome, so chromedriver 2.3+ must be on PATH.
</aside>

```
# install
git clone https://github.com/spyoungtech/behave-webdriver
cd behave-webdriver
pip install .
# run tests
behave behave_webdriver/features
```

0 features passed, 1 failed, 0 skipped
18 scenarios passed, 8 failed, 0 skipped
108 steps passed, 8 failed, 5 skipped, 0 undefined
```

# TODO
- [ ] Implement the support code from cucumber-boilerplate for behave/selenium
  - [x] given
  - [ ] when
  - [ ] then
- [x] Setup basic travis tests
- [ ] Provide some cool browser options
- [ ] ???
- [ ] Profit

# Acknowledgements

Thanks to the authors of the webdriverio [cucumber-boilerplate](https://github.com/webdriverio/cucumber-boilerplate) project for boilerplate ideas and feature files