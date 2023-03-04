#!/bin/bash

# Variables
SOURCE_DIR="$(pwd)/scripts"
DEST_DIR="/usr/share"
PYTHON_FILE="$DEST_DIR/Python-Passwd/main.py"

# Create a permanent alias to run the python file
echo "alias pswd='python3 $PYTHON_FILE'" >> ~/.bashrc

if [ -f "${HOME}/.zshrc" ]; then
    echo "alias pswd='python3 $PYTHON_FILE'" >> ~/.zshrc
fi


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
                   
        
        
        __ __  __   __ _____  ___  __    __    _____ _____ 
        || ||\ ||  ((   ||   ||=|| ||    ||    ||==  ||_// 
        || || \|| \_))  ||   || || ||__| ||__| ||___ || \\ 


"

echo "========================================================"

if [ $(id -u) != 0 ]; then
echo "
Please Grant sudo permissions !

"
fi

    
    # Copy the whole folder
    sudo cp -r $SOURCE_DIR $DEST_DIR

    # Rename and hide the folder
    sudo mv $DEST_DIR/scripts $DEST_DIR/Python-Passwd &>/dev/null

    # Create folder for credential Files
    sudo mkdir ~/.Python-Passwd-Data &>/dev/null

    # Create category folders
    cd ~/.Python-Passwd-Data
    sudo mkdir apps emails others social websites &>/dev/null


    echo "========================================================"

    echo " 
                Installation Complete !
    "
