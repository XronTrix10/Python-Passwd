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
        goto copy_Program
        goto Add_to_PATH
        pip install cryptography
        echo. & echo Success: Installation Complete & echo. & echo Press ENTER to quit....


    ) else (

        echo. & echo Failure: administrator rights failed !
        echo Please right click on the script and click on "Run as administrator"

    )

    echo. & echo Press ENTER to quit....
    
    pause >nul



:copy_Program

    xcopy %CD%\scripts C:\Program Files\Python-Passwd\ /s /e
    
    cd %APPDATA%
    mkdir Python-Passwd-Data
    cd Python-Passwd-Data
    mkdir apps emails others social websites
    :: hiding the directory
    attrib +h %APPDATA%\Python-Passwd-Data /s /d



:Add_to_PATH

    setx path "%path%;C:\Program Files\Python-Passwd\"