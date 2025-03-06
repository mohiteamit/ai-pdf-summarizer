@echo off
echo Loading environment variables...
for /f "tokens=1,2 delims==" %%a in ('type .env') do (
    set %%a=%%b
)

echo Activating virtual environment...
call %VENV_PATH%

set PYTHONPATH=%CD%
streamlit run app/main.py
