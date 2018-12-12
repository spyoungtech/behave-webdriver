FROM python:3.7

COPY . .
RUN pip install --no-cache-dir -r ./requirements.txt
RUN pip install --no-cache-dir pytest mock

ENV BEHAVE_WEBDRIVER=Remote
ENV HUB_URL=http://localhost:4444/wd/hub
ENV DEMO_URL=http://demo-site
ENV ENV_BASE_URL=http://demo-site

ENV CAPS="Chrome"

CMD behave tests/features
