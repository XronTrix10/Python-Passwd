import os

logo = """
__________   _____     _________  _________ __      __  ________   
\______   \ /  _  \   /   _____/ /   _____//  \    /  \ \______ \  
 |     ___//  /_\  \  \_____  \  \_____  \ \   \/\/   /  |    |  \ 
 |    |   /    |    \ /        \ /        \ \        /   |    `   \\
 |____|   \____|__  //_______  //_______  /  \__/\  /   /_______  /
                  \/         \/         \/        \/            \/ 
"""

bye = """

              Good Bye.
            ,'
          ;     
         ["]   
        /[_]\    
         ] [
    
"""

# Text Colors
class clr:

    reset = "\033[0m"
    bold = "\033[01m"
    disable = "\033[02m"
    underline = "\033[04m"
    reverse = "\033[07m"
    strikethrough = "\033[09m"
    invisible = "\033[08m"

    black = "\033[30m"
    red = "\033[31m"
    green = "\033[32m"
    orange = "\033[33m"
    blue = "\033[34m"
    purple = "\033[35m"
    cyan = "\033[36m"
    lightgrey = "\033[37m"
    darkgrey = "\033[90m"
    lightred = "\033[91m"
    lightgreen = "\033[92m"
    yellow = "\033[93m"
    lightblue = "\033[94m"
    pink = "\033[95m"
    lightcyan = "\033[96m"


# Function to clear screen and print logo
def header():
    os.system("cls")
    # print(clr.green,"\n" + "█"*70)
    print(clr.green,clr.bold, logo,clr.reset, end='\n\n')
    # print(clr.reset,clr.green,"\n" + "█"*70,clr.reset, end='\n\n\n')

