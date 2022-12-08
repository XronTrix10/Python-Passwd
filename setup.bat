@echo off

:: This script copies the programs to C:\Program Files directory, appends the location to PATH variable for current user and creates some hidden folders in APPDATA folder to save encrypted passwords

Title Setup

:::           
:::                .--------.
:::               / .------. \
:::              / /        \ \
:::              | |        | |
:::             _| |________| |_
:::           .' |_|        |_| '.
:::           '._____ ____ _____.'
:::           |     .'____'.     |
:::           '.__.'.'    '.'.__.'
:::           '.__  | PSWD |  __.'
:::           |   '.'.____.'.'   |
:::           '.____'.____.'____.'
:::           '.________________.'
:::           

for /f "delims=: tokens=*" %%A in ('findstr /b ::: "%~f0"') do @echo(%%A

echo. & echo Running Python Password Manager Installer

echo. & echo ========================================================

echo. & echo Checking for Administrative priviledges...

goto check_Permissions

:check_Permissions
    
    net session >nul 2>&1

    if %errorLevel% == 0 (

        echo. & echo Success: Administrative permissions confirmed.

        echo. & echo "Now Installing for you :)"
        
        :: copying all code files
        xcopy "%~dp0scripts" "C:\Program Files\Python-Passwd\" /s /e >nul 2>&1
        :: Creating directory for saving credentials
        cd %APPDATA%
        mkdir Python-Passwd-Data & cd Python-Passwd-Data
        mkdir apps emails others social websites
        :: hiding the directory
        attrib +h %APPDATA%\Python-Passwd-Data /s /d

        :: appending the location of code files to PATH
        setx path "%path%;C:\Program Files\Python-Passwd\" >nul 2>&1

        :: installing python cryptography module
        pip install cryptography >nul 2>&1

        echo. & echo ========================================================

        echo. & echo Success: Installation Complete


    ) else (

        echo. & echo Failure: administrator rights failed !
        echo Please right click on the script and click on "Run as administrator"

    )

    echo. & echo Press ENTER to quit....
    
    pause >nul
