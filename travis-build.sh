#!/bin/bash

set -ev

if [ "${BEHAVE_WEBDRIVER}" = "chrome" ] || [ "${BEHAVE_WEBDRIVER}" = "headless_chrome" ]; then
    wget -N http://chromedriver.storage.googleapis.com/2.33/chromedriver_linux64.zip -P ./
    unzip ~/chromedriver_linux64.zip -d ./
    rm ./chromedriver_linux64.zip
    chmod +x ./chromedriver

elif [ "${BEHAVE_WEBDRIVER}" = "firefox" ]; then
    wget https://github.com/mozilla/geckodriver/releases/download/v0.11.1/geckodriver-v0.11.1-linux64.tar.gz
    tar -xvzf ./geckodriver-v0.11.1-linux64.tar.gz
    rm ./geckodriver-v0.11.1-linux64.tar.gz
    chmod +x ./geckodriver


fi

