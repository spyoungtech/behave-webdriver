C:\Python36\python.exe -m venv venv

call venv\Scripts\activate.bat

pip install -r .\requirements.txt

pip install pytest mock coverage

call deactivate
