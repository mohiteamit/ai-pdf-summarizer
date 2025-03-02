@echo off

REM This script sets up a virtual environment using a predefined base path.
REM The base path should be provided as a command line argument.
REM Example usage: setup_env.bat C:\Users\windowsusers\venvs

REM Check if base path argument is provided
if "%1"=="" (
    echo Error: No base path provided. Usage: setup_env.bat C:\path\to\venvs
    exit /b 1
)

set BASE_PATH=%1
set VENV_NAME=ai_note_summarizer

REM Step 1: Create a virtual environment in the specified path
if not exist %BASE_PATH%\%VENV_NAME% (
    echo Creating virtual environment at %BASE_PATH%\%VENV_NAME%
    python -m venv %BASE_PATH%\%VENV_NAME%
) else (
    echo Virtual environment already exists at %BASE_PATH%\%VENV_NAME%
)

REM Step 2: Activate the virtual environment
call %BASE_PATH%\%VENV_NAME%\Scripts\activate

REM Step 3: Install dependencies
pip install -r requirements.txt

REM Step 4: Load environment variables
if exist .env (
    echo Loading environment variables from .env file
    setlocal enabledelayedexpansion
    for /f "tokens=* delims=" %%a in ('type .env') do set "%%a"
)

REM Step 5: Verify installation
python --version
pip freeze

echo Environment setup complete!
