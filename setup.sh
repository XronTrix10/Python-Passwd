#!/bin/bash

# Variables
SOURCE_DIR="$(pwd)/scripts"
DEST_DIR="/etc/app"
PYTHON_FILE="/home/ben/fileName.py"

# Copy the whole folder
cp -r $SOURCE_DIR $DEST_DIR

# Make the destination folder hidden
chmod -R 700 $DEST_DIR

# Create a permanent alias to run the python file
echo "alias pythonfile='python3 $PYTHON_FILE'" >> ~/.bashrc
