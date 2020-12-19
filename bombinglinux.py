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
from selenium.webdriver.common.keys import Keys 
import requests
import pyfiglet 
import time
import os
import platform
import webbrowser
###################################################################################################
"""
    DEFINITIONS
"""

options = 0

cr_dict = 0

browser = 0

counter = 0

###################################################################################################
"""
    FUNCTIONS
"""

def twbombinglinux():
    options = Options()
    options.add_argument("--log-level=3")
    cr_dict = os.getcwd() + r'/geckodriver'

    browser = webdriver.Firefox(executable_path=cr_dict, options=options)

    login = input("    |-$ Your Twitter username (without @) > ")
    password = input("    |-$ Your Twitter password > ")

    browser.get("https://twitter.com/messages/compose")

    time.sleep(3)

    browser.find_element_by_name("session[username_or_email]").send_keys(login + Keys.ENTER) #Writing the username.
    browser.find_element_by_name("session[password]").send_keys(password + Keys.ENTER) #Writing the password.
    
    """
        Already Loged in.
    """
    
    time.sleep(3)

    tw_victim = input("    |-$ Your victim's username (with @) > " )

    browser.find_element_by_css_selector('input.r-fdjqy7').send_keys(tw_victim)

    time.sleep(2)

    browser.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[1]/div/div/div/div[3]/div/div').click()

    time.sleep(1)
    browser.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[2]/div/div/div/div/div/form/div[2]/div/div[2]/div/li/div[2]/div[2]/div").click()
    browser.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[1]/div/div/div/div[3]/div/div").click()

    time.sleep(3)

    mode = input('''    |
    |-PRESS------------------|
    | 1] Repetitive Mode     |
    | 2] Script/Lyrical Mode |
    |------------------------|
    |-> ''')

    if mode.lower() == '1' or mode.lower() == 'repetitive mode':
        message = input('    |-$ Word/Sentence that you want to send Multiple Times > ')
        repcount = int(input('    |-$ How many times ? > '))

    elif mode.lower() == '2' or mode.lower() == 'script/lyrical mode':
        lyrics = open("lyrics.txt","r+")
        splitedlyrics = (lyrics.read().split())

    else:
        print('    |-} invalid input !')
        return

    if mode.lower() == '1' or mode.lower() == 'repetitive mode':
        for i in range(repcount):
            global counter
            counter = counter + 1
            print ("    |Se han enviado", counter)
            browser.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/main/div/div/div/section[2]/div[2]/div/div/div/div/aside/div[2]/div[2]/div/div/div/div/div[1]/div/div/div/div[2]/div").send_keys(message + Keys.ENTER)

    elif mode.lower() == '2' or mode.lower() == 'script/lyrical mode':
        for words in splitedlyrics:
            browser.find_elements_by_xpath("//div[@class='_3FRCZ copyable-text selectable-text']")[1].send_keys(words + Keys.ENTER)

    time.sleep(5)
    browser.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/main/div/div/div/section[2]/div[2]/div/div/div/div/aside/div[2]/div[2]/div/div/div/div/div[1]/div/div/div/div[2]/div").send_keys("Developed by TallBlocks, https://TallBlocks.github.io" + Keys.ENTER)
    print(
    '''    |-} Done !
    |-----------------------------------------------------------''')
    browser.quit()

    
