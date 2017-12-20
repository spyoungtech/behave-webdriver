if [ "${BEHAVE_WEBDRIVER}" = "firefox" ]; then
    behave tests/features --tags=-firefox_bug
else
    behave tests/features
fi