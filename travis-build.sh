#!/bin/bash

set -ev

if [ "${BEHAVE_WEBDRIVER}" = "chrome" ] || [ "${BEHAVE_WEBDRIVER}" = "headless_chrome"]; then
    wget -N http://chromedriver.storage.googleapis.com/2.33/chromedriver_linux64.zip -P ~/
    unzip ~/chromedriver_linux64.zip -d ~/
    rm ~/chromedriver_linux64.zip
    sudo mv -f ~/chromedriver /usr/local/share/
    sudo chmod +x /usr/local/share/chromedriver
    sudo ln -s /usr/local/share/chromedriver /usr/local/bin/chromedriver

elif [ "${BEHAVE_WEBDRIVER}" = "firefox"]; then
    wget https://github.com/mozilla/geckodriver/releases/download/v0.11.1/geckodriver-v0.11.1-linux64.tar.gz
    tar -xvzf ./geckodriver-v0.11.1-linux64.tar.gz
    rm ./geckodriver-v0.11.1-linux64.tar.gz
    sudo mv -f ./geckodriver /usr/local/share/
    sudo chmod +x /usr/local/share/geckodriver
    sudo ln -s /usr/local/share/geckodriver /usr/local/bin/geckodriver


fi

