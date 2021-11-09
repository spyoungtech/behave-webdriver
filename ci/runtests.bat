call venv\Scripts\activate.bat

powershell -Command "Import-Module WebAdministration;New-WebSite -Name demoapp -Port 8000 -PhysicalPath C:\projects\behave-webdriver\tests\demo-app"

coverage run -m behave tests\features --format=progress2 --junit

coverage run -a -m pytest tests\unittests --junitxml=reports\pytestresults.xml

call deactivate
