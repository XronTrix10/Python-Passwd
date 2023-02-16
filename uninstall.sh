@echo off

:: This script copies the programs to C:\Program Files directory, appends the location to PATH variable for current user and creates some hidden folders in APPDATA folder to save encrypted passwords

echo "


                              .--------.
                             / .------. \
                            / /        \ \
                            | |        | |
                           _| |________| |_
                         .' |_|        |_| '.
                         '._____ ____ _____.'
                         |     .'____'.     |
                         '.__.'.'    '.'.__.'
                         '.__  | PSWD |  __.'
                         |   '.'.____.'.'   |
                         '.____'.____.'____.'
                         '.________________.'



    __ __ __  __ __ __  __   __ _____  ___  __    __    _____ _____ 
    || || ||\\|| || ||\\||  ((   ||   ||=|| ||    ||    ||==  ||_// 
    \\_// || \|| || || \|| \_))  ||   || || ||__| ||__| ||___ || \\ 

"


echo ========================================================

if [ $(id -u) != 0 ]; then

    echo "Root priviledge not Acquired !"
    
else

    rm -r /srv/.Python-Passwd/ &>/dev/null

    echo "Uninstallation in progress...."

    echo ========================================================

    echo "
                    Uninstallation Complete !
    
    "
fi