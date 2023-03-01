import os
import time
import random
import ctypes
import pyautogui
import subprocess
from colorama import Fore, Back, Style
from selenium.webdriver.common.by import By
from pystyle import Colorate, Colors, Center

# Selenium

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Vars

hits = 0
miss = 0
amount = 0
emailchoice = 0


# Functions

def title():
    banner = Center.XCenter(Colorate.Vertical(Colors.red_to_purple, """
                        ███████╗████████╗███████╗ █████╗ ███╗   ███╗ ██████╗ ███████╗███╗   ██╗
                        ██╔════╝╚══██╔══╝██╔════╝██╔══██╗████╗ ████║██╔════╝ ██╔════╝████╗  ██║
                        ███████╗   ██║   █████╗  ███████║██╔████╔██║██║  ███╗█████╗  ██╔██╗ ██║
                        ╚════██║   ██║   ██╔══╝  ██╔══██║██║╚██╔╝██║██║   ██║██╔══╝  ██║╚██╗██║
                        ███████║   ██║   ███████╗██║  ██║██║ ╚═╝ ██║╚██████╔╝███████╗██║ ╚████║
                        ╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═══╝
                
========================================================================================================================                                                                       
    """))
    try:
        os.system("cls")
    except:
        os.system("clear")
    print(banner)
    print(Center.XCenter(f"{Fore.RED}>> {Fore.LIGHTMAGENTA_EX}Welcome to SteamGen!\n{Fore.RESET}"))
    print(Center.XCenter(f"{Fore.RED}>> {Fore.LIGHTMAGENTA_EX}Made By: @LUXTACO\n{Fore.RESET}"))
    print(Center.XCenter(f"{Fore.RED}>> {Fore.LIGHTMAGENTA_EX}Version: 1.5\n{Fore.RESET}"))
    

def pass_gen():
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+"
    password = ""
    for c in range(16):
        password += random.choice(chars)
    return password

def user_gen():
    suffix = ['Best', 'Ratchet', 'Baller', 'Big', 'Money']
    name_list = ['Lil', 'Big', 'Young', 'Old', 'Dope', 'Savage', 'Crazy', 'Swag', 'Dank', 'Lit', 'Savage', 'Crazy']
    prefix = ['Swag', 'Dank', 'Lit', 'Savage', 'Crazy']
    
    name = random.choice(suffix) + random.choice(name_list) + random.choice(suffix)
    
    return name

def get_email():
    global emailchoice
    
    with open("email.txt", "r") as f:
        emails = f.readlines()
        tempmail = emails[emailchoice].strip()
        f.close()
    return tempmail

# Bools

fail = False

# User Agent

ua = 'Mozilla/5.0 (Windows NT 4.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36'

# Main

title()
ctypes.windll.kernel32.SetConsoleTitleW(f"SteamGen V1.5 | Hits: {hits} | Miss: {miss} | Made By: @LUXTACO")

visual = input(Center.XCenter(f"{Fore.RED}>> {Fore.LIGHTMAGENTA_EX}Do you want to use visual feedback? (y/n): {Fore.RESET}"))

if visual == "y" or visual == "Y":
    print(Center.XCenter(f"{Fore.RED}>> {Fore.LIGHTMAGENTA_EX}Visual feedback enabled!{Fore.RESET}"))
    options = Options()
    options.add_argument(f'--user-agent={ua}')
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-infobars")
    options.add_argument("--mute-audio")
    options.add_argument('--no-sandbox')
    options.add_argument("log-level=3")
    options.add_argument('--no-sandbox')
    options.add_extension("./solver/solver.crx")
    driver = webdriver.Chrome(options=options)
    wait = WebDriverWait(driver, 20)
else:
    print(Center.XCenter(f"{Fore.RED}>> {Fore.LIGHTMAGENTA_EX}Visual feedback disabled!{Fore.RESET}"))
    options = Options()
    options.add_argument(f'--user-agent={ua}')
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-infobars")
    options.add_argument("--mute-audio")
    options.add_argument('--no-sandbox')
    options.add_argument("log-level=3")
    options.add_argument("--headless")
    options.add_argument('--no-sandbox')
    options.add_extension("./solver/solver.crx")
    driver = webdriver.Chrome(options=options)
    wait = WebDriverWait(driver, 20)
    
amount = int(input(Center.XCenter(f"{Fore.RED}\n>> {Fore.LIGHTMAGENTA_EX}How many accounts do you want to generate?: {Fore.RESET}")))
    
while amount != 0:
    
    fail = False
    
    username = user_gen()
    password = pass_gen()
    email = get_email()
    
    print(Center.XCenter(f"{Fore.RED}>> {Fore.LIGHTMAGENTA_EX}Username: {username} | Password: {password} | Email: {email} {Fore.RESET}"))
    
    amount = str(amount)
    print(Center.XCenter(f"{Fore.RED}>> {Fore.LIGHTMAGENTA_EX}Amount: {emailchoice} | Hits: {hits} | Misses: {miss} {Fore.RESET}"))
    ctypes.windll.kernel32.SetConsoleTitleW(f"SteamGen V1.5 | Hits: {hits} | Miss: {miss} | Made By: @LUXTACO")
    amount = int(amount)
    
    try: 
        driver.get("https://store.steampowered.com/join/")
        print(f"{Fore.LIGHTMAGENTA_EX}Opened Steam!{Fore.RESET}")
        print(f"{Fore.LIGHTMAGENTA_EX}Waiting for page load!{Fore.RESET}")
        wait.until(EC.presence_of_element_located((By.XPATH, '/html/body')))
        print(f"{Fore.LIGHTMAGENTA_EX}Page loaded!{Fore.RESET}")
    except:
        print(f"{Fore.LIGHTMAGENTA_EX}Not able to reach the page!{Fore.RESET}")
        print(f"{Fore.LIGHTMAGENTA_EX}Retrying...{Fore.RESET}")
        miss += 1
        fail = True
        pass
    
    if fail == False:
        try:
            driver.find_element(By.XPATH, '//*[@id="email"]' ).send_keys(email)
            driver.find_element(By.XPATH, '//*[@id="reenter_email"]' ).send_keys(email)
        except:
            print(f"{Fore.LIGHTMAGENTA_EX}Unable to enter email!{Fore.RESET}")
            miss += 1
            fail = True
            pass
        
        if fail == False:
            
            try: 
                print(f"{Fore.LIGHTMAGENTA_EX}Solving Captcha!{Fore.RESET}")
                time.sleep(15)
                if visual == "y" or visual == "Y":
                    if pyautogui.pixel(115, 686)[1] == 158:
                        print(f"{Fore.LIGHTMAGENTA_EX}Captcha Solved!{Fore.RESET}")
                    else:
                        print(f"{Fore.LIGHTMAGENTA_EX}Cannot recognise if captcha is solved!{Fore.RESET}")
                        input(f"{Fore.LIGHTMAGENTA_EX}Please solve it, once solved press ENTER!{Fore.RESET}")
                else:
                    time.sleep(15)
                    print(f"{Fore.LIGHTMAGENTA_EX}Cant verify if captcha is solved please choose visual feedback next time!{Fore.RESET}")
                    print(f"{Fore.LIGHTMAGENTA_EX}Captcha solved I guess... {Fore.RESET}")
            except:
                print(f"{Fore.LIGHTMAGENTA_EX}Captcha not solved!{Fore.RESET}")
                input(f"{Fore.LIGHTMAGENTA_EX}Please solve it, once solved press ENTER!{Fore.RESET}")
            
            if fail == False:
                try:
                    driver.find_element(By.XPATH, '//*[@id="i_agree_check"]' ).click()
                    driver.find_element(By.XPATH, '//*[@id="createAccountButton"]').click()
                    print(f"{Fore.LIGHTMAGENTA_EX}Please verify email!{Fore.RESET}")
                    input(f"{Fore.LIGHTMAGENTA_EX}Once verified press ENTER!{Fore.RESET}")
                except:
                    print(f"{Fore.LIGHTMAGENTA_EX}Unable to create account!{Fore.RESET}")
                    miss += 1
                    fail = True
                    pass
                
                if fail == False:
                    try:
                        print(f"{Fore.LIGHTMAGENTA_EX}Waiting for page load!{Fore.RESET}")
                        wait.until(EC.presence_of_element_located((By.XPATH, '/html/body')))
                        print(f"{Fore.LIGHTMAGENTA_EX}Page loaded!{Fore.RESET}")
                        time.sleep(1)
                        print(f"{Fore.LIGHTMAGENTA_EX}Entering username!{Fore.RESET}")
                        driver.find_element(By.XPATH, '//*[@id="accountname"]' ).send_keys(username)
                        time.sleep(1)
                        print(f"{Fore.LIGHTMAGENTA_EX}Entering password!{Fore.RESET}")
                        driver.find_element(By.XPATH, '//*[@id="password"]' ).send_keys(password)
                        driver.find_element(By.XPATH, '//*[@id="reenter_password"]' ).send_keys(password)
                        time.sleep(1)
                        print(f"{Fore.LIGHTMAGENTA_EX}Creating Account!{Fore.RESET}")
                        driver.find_element(By.XPATH, '//*[@id="createAccountButton"]')
                        time.sleep(1)
                        print(f"{Fore.LIGHTMAGENTA_EX}Account created!{Fore.RESET}")
                        print(f"{Fore.LIGHTMAGENTA_EX}Saving Credentials!{Fore.RESET}")
                    except:
                        print(f"{Fore.LIGHTMAGENTA_EX}Unable to enter username!{Fore.RESET}")
                        miss += 1
                        fail = True
                        pass
            
    elif fail == True:
        driver.quit()
        pass
    
    if fail == False:
        s = "----- Steam Account -----"
        u = "Username: " + username
        p = "Password: " + password
        e = "Email: " + email
        d = "-------------------------"
        with open("accounts.txt", "a") as f:
            f.write(s)
            f.write("\n")
            f.write(u)
            f.write("\n")
            f.write(p)
            f.write("\n")
            f.write(e)
            f.write("\n")
            f.write(d)
            f.write("\n")
            f.flush()
            f.close()
        amount -= 1
        emailchoice += 1