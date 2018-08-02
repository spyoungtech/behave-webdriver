#!/bin/sh

if [ "$TRAVIS_OS_NAME" == "osx" ]
then
    sudo safaridriver --enable
    brew upgrade python
    sudo python3 -m pip install -r ./requirements.txt
    sudo python3 -m pip install coveralls pytest mock
else
    python -m pip install -r ./requirements.txt
    python -m pip install coveralls pytest mock
fi


if [ "${BEHAVE_WEBDRIVER}" = "Firefox" ]
then
    wget https://github.com/mozilla/geckodriver/releases/download/v0.20.0/geckodriver-v0.20.0-linux64.tar.gz
    tar -xvzf ./geckodriver-v0.20.0-linux64.tar.gz
    rm ./geckodriver-v0.20.0-linux64.tar.gz
    chmod +x ./geckodriver
fi


if [ "${BEHAVE_WEBDRIVER}" = "Chrome" ]
then
    wget -N http://chromedriver.storage.googleapis.com/2.37/chromedriver_linux64.zip -P ./
    unzip ./chromedriver_linux64.zip -d ./
    rm ./chromedriver_linux64.zip
    chmod +x ./chromedriver
fi