@echo off
cd %~dp0
echo Installing required dependencies
pip install tweepy
echo Required dependencies successfully installed!
echo @echo off > start.bat
echo title Flunty's Twitter Client - Console >> start.bat
echo echo Logs: >> start.bat
echo python main.py >> start.bat
del "%~f0"