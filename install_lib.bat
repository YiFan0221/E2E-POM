@echo off
REM Create virtual environment
python -m venv tutorial-env

REM Activate virtual environment
.\tutorial-env\Scripts\activate.bat

REM Install dependencies from requirements.txt
pip install -r requirements.txt
