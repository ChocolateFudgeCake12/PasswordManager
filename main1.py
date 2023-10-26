import random
from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from time import sleep
import sys 

sys.setrecursionlimit(10000000) 

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)


currentautofillwebsite = ''

def newautofill():
    website = input("What is the url of the website login page? Please include the https:// ")
    username = input("What is your username/email for this website? ")
    password = input("What is you password for this site? ")
    idusername = input("What is the id for the username inputfield ")
    idpassword = input("What is the id for the password field ")
    print("Saving to Autofill Data...")
    with open(r'.\AutofillUsernameID.txt', 'r+') as f:
        lines = f.readlines()
        lines.insert(0, idusername + website + '\n')
        f.seek(0)
        f.writelines(lines)
    with open(r'.\AutofillPasswordID.txt', 'r+') as f:
        lines = f.readlines()
        lines.insert(0, idpassword + website + '\n')
        f.seek(0)
        f.writelines(lines)
    with open(r'.\AutofillUsername.txt', 'r+') as f:
        lines = f.readlines()
        lines.insert(0, username + website + '\n')
        f.seek(0)
        f.writelines(lines)
    with open(r'.\AutofillPassword.txt', 'r+') as f:
        lines = f.readlines()
        lines.insert(0, password + website + '\n')
        f.seek(0)
        f.writelines(lines)
    with open(r'.\AutofillWebsites.txt', 'r+') as f:
        lines = f.readlines()
        lines.insert(0, website + '\n')
        f.seek(0)
        f.writelines(lines)
    driver = webdriver.Chrome(options=options)
    driver.get(website) 
    usernameElement = element = driver.find_element(By.ID, idusername)
    passowrdElement = element = driver.find_element(By.ID, idpassword)
    usernameElement.send_keys(username)
    passowrdElement.send_keys(password)
 

def autofillbrowser():
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.google.com/")
    
    def autofillbrowsercheck():
        oldurl = driver.current_url
        driver.implicitly_wait(0.1)
        if oldurl == driver.current_url:
            autofillbrowsercheck()
        else:
            autofillconfirmed()
    def autofillconfirmed():
        currenturl = driver.current_url
        with open(r'.\AutofillWebsites.txt', 'r') as fp:
            # read all lines in a list
            lines = fp.readlines()
        for line in lines:
            # check if string present on a current line
            if line.find(currenturl) != -1:
                currentautofillwebsite = line
                print("Autofilling for " + currentautofillwebsite)
                # open autfoillpassword.txt and assign the variable currentautofillpassword the value of the autofill password
                with open(r'.\autofillPassword.txt', 'r') as Ap:
                    lines = Ap.readlines()
                for line in lines:
                    if line.find(currentautofillwebsite):
                        currentautofillpassword = line
                        currentautofillpassword = currentautofillpassword.replace(currentautofillwebsite, '')
                        # open autofillpassword.txt and assign the variable current autofillpassword the value of the autofill password
                with open(r'.\autofillUsername.txt', 'r') as Au:
                    lines = Au.readlines()
                for line in lines:
                    if line.find(currentautofillwebsite):
                        currentautofillusername = line
                        currentautofillusername = currentautofillusername.replace(currentautofillwebsite, '')
                with open(r'.\autofillusername.txt', 'r') as AUI:
                    lines = AUI.readlines()
                for line in lines:
                    if line.find(currentautofillwebsite):
                        currentautofillUsernameID = line
                        currentautofillUsernameID = currentautofillUsernameID.replace(currentautofillwebsite, '')
                with open(r'.\autofillPasswordID.txt', 'r') as API:
                    lines = API.readlines()
                for line in lines:
                    if line.find(currentautofillwebsite):
                        currentautofillPasswordID = line
                        currentautofillPasswordID = currentautofillPasswordID.replace(currentautofillwebsite, '')
                usernameElement = element = driver.find_element(By.ID, currentautofillUsernameID)
                passwordElement = element = driver.find_element(By.ID, currentautofillPasswordID)
                usernameElement.send_keys(currentautofillusername)
                passwordElement.send_keys(currentautofillpassword)
                autofillbrowsercheck()
                
    autofillbrowsercheck()
                

def startmenu():
    print("Hi, what would you like to do today? ")
    startmenuoptions= input("1 - new password 2 - find password 3 - New autofill password 4 - New autofill browser ")
    if startmenuoptions == "1":
        newpassword()
    if startmenuoptions == "2":
        findpassword()
    if startmenuoptions == "3":
        newautofill()
    if startmenuoptions == "4":
        autofillbrowser()
    else:
        print("Not a valid answer")
        startmenu()
        



def findpassword():
    word = input("what is the name of the application you want to find your password for? ")
    with open(r"C:\Users\cmlle\Dropbox\PasswordManager\masterpassword.txt", 'r') as fp:
        # read all lines in a list
        lines = fp.readlines()
        for line in lines:
            # check if string present on a current line
            if line.find(word) != -1:
                print(word, 'string exists in file')
                print('Line Number:', lines.index(line))
                print('Line:', line)
                startmenu()
            else:
                print("We couldn't find a passowrd with that application name. ")
                startmenu()
                return
                

def newpassword():
    def generate_random_string(length):
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789,.:"!@#$%^&*()'
        return ''.join(random.sample(alphabet, k=length))

    ApplicationName = input("What application would you like to generate a password for? ")

    print("generating a password for " + ApplicationName)

    password = generate_random_string(10)

    print("Your password is: " + password)

    Savetofile = input("Would you like to save this password to a file? Y/N" )

    if Savetofile == "Y":
        print("Saving to file masterpassword.txt")
    with open('masterpassword.txt', 'r+') as f:
        file = f.readlines()
        file.insert(0, ApplicationName + ': ' + password + '\n')
        f.seek(0)
        f.writelines(file)
    if Savetofile == "Y":
        startmenu()
        return

    if Savetofile == "N":
        print("We will not save you password on a file. Thank you for using our service")
        startmenu()
        return

    if Savetofile != "Y" or "N":
        print("Not a valid answer")
        startmenu()
        return


startmenu()





