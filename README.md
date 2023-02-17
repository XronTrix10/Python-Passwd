# Python-Passwd

![Image](https://user-images.githubusercontent.com/98148986/219333077-3e88552e-87ee-4360-8874-d60aab16cd37.png)

### This is a simple CLI encryption based local password manager for those who don't want to rely upon third party online password managers

---

## Features

- Has inbuilt strong password generator
- The credentials are saved in a hidden directory inside /opt folder in encrypted format (.pswd)
- uses advanced & modified cipher text algorithm for encryption
- Has Vault Lock Protection
- User can save email, mobile, username, passwords and comments
- User can have multiple accounts in same website or app
- User can delete or modify saved credentials
- Have different categories for credentials

## Requirements

- System must have Python 3.x pre-installed

## This is for Linux only
[![Linux](https://img.shields.io/badge/Linux-FCC624?style=flat&logo=linux&logoColor=black)](https://github.com/XronTrix10/Python-Passwd/tree/linux)

## Checkout Windows
[![Windows](https://img.shields.io/badge/Windows-0078D6?style=flate&logo=windows-11&logoColor=white)](https://github.com/XronTrix10/Python-Passwd/tree/windows)


## Installation for Linux

1. [Download](https://codeload.github.com/XronTrix10/Python-Passwd/zip/refs/heads/windows) the Repo or,

       git clone -b linux https://github.com/XronTrix10/Python-Passwd

2. Run the setup file

       cd Python-Passwd && chmod +x setup.sh && bash setup.sh       
              
3. Grant sudo permission when asked

### __NOTE :__ The setup script by default appends an alias to your .bashrc file. If you have zsh installed, then manually add the alias by running the command below

    echo "alias pswd='python3 /srv/.Python-Passwd/main.py'" >> ~/.zshrc

<br>  

## Usage

- Open any Terminal from anywhere, then
        
      pswd
