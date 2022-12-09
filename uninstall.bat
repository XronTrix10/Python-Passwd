@echo off

:: This script copies the programs to C:\Program Files directory, appends the location to PATH variable for current user and creates some hidden folders in APPDATA folder to save encrypted passwords

Title Setup

:::           
:::                          .--------.
:::                         / .------. \
:::                        / /        \ \
:::                        | |        | |
:::                       _| |________| |_
:::                     .' |_|        |_| '.
:::                     '._____ ____ _____.'
:::                     |     .'____'.     |
:::                     '.__.'.'    '.'.__.'
:::                     '.__  | PSWD |  __.'
:::                     |   '.'.____.'.'   |
:::                     '.____'.____.'____.'
:::                     '.________________.'
:::           
:::
:::
:::__ __ __  __ __ __  __   __ _____  ___  __    __    _____ _____ 
:::|| || ||\\|| || ||\\||  ((   ||   ||=|| ||    ||    ||==  ||_// 
:::\\_// || \|| || || \|| \_))  ||   || || ||__| ||__| ||___ || \\ 


for /f "delims=: tokens=*" %%A in ('findstr /b ::: "%~f0"') do @echo(%%A

echo. & echo ========================================================

echo. & echo Checking for Administrative priviledges...

goto check_Permissions

:check_Permissions
    
    net session >nul 2>&1

    if %errorLevel% == 0 (

        echo. & echo Success: Administrative permissions confirmed.

        echo. & echo Now Uninstalling for you :^)
        
        :: Deleting Recursively all code files
        rd /s /q "C:\Program Files\Python-Passwd" 
        

        echo. & echo Success: Installation Complete


    ) else (

        echo. & echo Failure: administrator rights failed !
        echo Please right click on the script and click on "Run as administrator"

    )

    echo. & echo ========================================================

    echo. & echo Press ENTER to quit....
    
    pause >nul
