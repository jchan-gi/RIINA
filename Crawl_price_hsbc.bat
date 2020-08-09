@ECHO OFF

REM ===================================================
REM ===  Regular insertion of Internet-sourced NAV  ===
REM ===             Codename     RIINA              ===
REM ===            Jimmy Chan - jchan-gi            ===
REM ===================================================
REM
REM ==Description
REM   This set of tools support scheduled crawling of funds price from Internet source.

REM ==LICENSE
REM   BSD 3-clause

REM ==Website
REM   https://github.com/jchan-gi/RIINA

REM ==DEFINE PROGRAM WIDE VAR
REM ---Path information---
SET PWD=%~dp0
SET TEMP_DIR=%PWD%\temp
SET LOG_FILE=%PWD%\logfile.log
SET WEBDRIVER=%PWD%\chromedriver.exe
SET CRAWLER_SCRIPT_DIR=%PWD%\crawler_script
SET CRAWLER_HELPER=%CRAWLER_SCRIPT_DIR%\download_webpage.py

REM ---Fund provider-specific information---
SET CURRENT_SCRIPT_NAME=%CRAWLER_SCRIPT_DIR%\downloader_xxxx.py
SET SQLITE_PATH=Z:\GitHub\raw_data\mpf_hsbc.sqlite
SET OPERATOR=hsbc

REM ---Crawling information---
SET DATA_SRC=xxxx
SET DATA_SRC_PATH=xxxx

REM ---Remove all existing files in Temp folder and then recreate a temp folder---
RD /S /Q "%TEMP_DIR%"
mkdir "%TEMP_DIR%"

REM ---Execute the crawler---
python %CURRENT_SCRIPT_NAME%
RD /S /Q "%TEMP_DIR%"