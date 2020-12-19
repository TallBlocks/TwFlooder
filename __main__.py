###################################################################################################
"""
    IMPORTS
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
import requests
import pyfiglet 
import time
import os

import platform
import webbrowser
from bombingwindows import *
from bombinglinux import *

from selenium.webdriver.common.keys import Keys 

###################################################################################################
"""
    DEFINITIONS
"""

counter = 0

res = 0

linux = 0

AsciiArt = 0

###################################################################################################
"""
    FUNCTIONS
"""

def checkInternet():
    res = False
    try:
        requests.get('https://www.google.com')
        res = False
    except Exception:
        res = True
    if res:
        print("    |-$ It seems that you are not connected to Internet.")
        print('    |-$ TwFlooder will stop now...')
        exit()

def checkPlataform():
    global linux
    if platform.system() == 'Linux':
        linux = True
        pass
    elif platform.system() == 'Windows':
        linux = False
        pass
    else:
        print('OS not supported !')
        exit()

###################################################################################################
"""
    EOF
"""

checkPlataform()

checkInternet()

AsciiArt = pyfiglet.figlet_format("TallBlocks's TwFlooder")

print (AsciiArt)
print ("")
print ("    |-$ https://TallBlocks.github.io")
print ("    |")

if linux:
    twbombinglinux()
elif linux == False:
    twbombingwin()
time.sleep(2)