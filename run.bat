REM @echo off

REM Create a new virtual environment
python -m venv venv

REM Activate the virtual environment
venv\Scripts\activate.bat

REM Install required packages
pip install -r requirements.txt

REM Run the Python application
python myapps.py

REM Deactivate the virtual environment
REM deactivate