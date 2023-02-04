import os

# checks if the user has already entered a password
if os.path.exists('pswd.key'):
    # asks the user to enter the password
    password = input("Enter the password: ")
    # opens the file 'pswd.key' in read mode to compare the password
    with open('pswd.key', 'r') as f:
        # compares the password with the saved string
        if password == str(f.readline()):
            print('Welcome!')
        else:
            print('Authentication failed.')

# will be executed only if the file 'pswd.key' doesn't exist
else:
    # asks the user to enter the password
    password = input("Enter the password: ")
    # opens the file 'pswd.key' in write mode to save the entered password 
    with open('pswd.key', 'w') as f:
        f.write(password)
