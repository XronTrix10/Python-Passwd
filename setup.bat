@echo off

:: This script copies the programs to C:\Program Files directory, appends the location to PATH variable for current user and creates some hidden folders in APPDATA folder to save encrypted passwords

Title Setup

:::           
:::                   .--------.
:::                  / .------. \
:::                 / /        \ \
:::                 | |        | |
:::                _| |________| |_
:::              .' |_|        |_| '.
:::              '._____ ____ _____.'
:::              |     .'____'.     |
:::              '.__.'.'    '.'.__.'
:::              '.__  | PSWD |  __.'
:::              |   '.'.____.'.'   |
:::              '.____'.____.'____.'
:::              '.________________.'
:::           
:::
:::
:::__ __  __   __ _____  ___  __    __    _____ _____ 
:::|| ||\\||  ((   ||   ||=|| ||    ||    ||==  ||_// 
:::|| || \|| \_))  ||   || || ||__| ||__| ||___ || \\ 
        

for /f "delims=: tokens=*" %%A in ('findstr /b ::: "%~f0"') do @echo(%%A

echo. & echo ========================================================

goto check_Permissions

:check_Permissions
    
    net session >nul 2>&1

    if %errorLevel% == 0 (

        echo. & echo Installing for you :^)
        
        :: copying all code files
        xcopy "%~dp0scripts" "C:\Program Files\Python-Passwd\" /s /e /y >nul 2>&1
        :: Creating directory for saving credentials
        cd %APPDATA%
        mkdir Python-Passwd-Data >nul 2>&1
        cd Python-Passwd-Data   
        mkdir apps emails others social websites >nul 2>&1
        :: hiding the directory
        attrib +h %APPDATA%\Python-Passwd-Data /s /d

        :: appending the location of code files to PATH
        :: setx path "%path%;C:\Program Files\Python-Passwd\" >nul 2>&1

        echo. & echo Success: Installation Complete

        :: echo. & echo Now Just ^1 step left:
        :: echo. & echo Copy the below line and add into the PATH variable from your system environment variables settings
        :: echo. & echo C:\Program Files\Python-Passwd
        :: echo. & echo NOTE: If you don't do this, you won't be able to run it from anywhere from your pc. Ignore if alredy done
        :: echo. & echo Now open any terminal and type 'pswd' to use the Program
        
    ) else (

        echo. & echo Failure: administrator rights failed !
        echo Please right click on the script and click on "Run as administrator"

    )

    echo. & echo ========================================================

    echo. & echo Press ENTER to quit....
    
    pause >nul
