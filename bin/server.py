import time
import random
import requests
import pyautogui
import configparser
from pystyle import Colorate, Colors, Center

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Variables

captcha_loc = [115, 682]
buster_loc = [265, 946]

hits = 0
miss = 0
amount = 0
amount_acc = 0
emailchoice = 0
proxychoice = 0
fail = False

# Functions

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
    
    name = random.choice(suffix) + random.choice(name_list) + random.choice(suffix) + str(random.randint(1111, 9999))
    
    return name

def get_email():
    global emailchoice
    
    with open("email.txt", "r") as f:
        emails = f.readlines()
        tempmail = emails[emailchoice].strip()
        f.close()
    return tempmail

def get_proxy():
    global proxychoice
    with open("proxies.txt", "r") as f:
        proxies = f.readlines()
        f.close()
    
    while True:
        proxy = proxies[proxychoice].strip()
        try:
            requests.get('https://www.google.com/', proxies={'http': proxy, 'https': proxy}, timeout=5)
            return proxy
        except:
            print(f"\r{Colors.pink}>> {Colors.white}Proxy {proxy} is not working. Trying another proxy...                                {Colors.white}", end="")
            proxychoice += 1
            if proxychoice >= len(proxies):
                proxychoice = 0



# Main

ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"

visual = input(f"{Colors.pink}>> {Colors.white}Do you want to have visual feedback? (y/n): {Colors.white}")
solver = input(f"{Colors.pink}>> {Colors.white}Do you want to use the captcha solver? (y/n): {Colors.white}")
if visual.lower() == "y":
    print(f"{Colors.pink}>> {Colors.white}Visual feedback enabled!{Colors.white}")
    options = Options()
    options.add_argument(f'--user-agent={ua}')
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-infobars")
    options.add_argument("--mute-audio")
    options.add_argument('--no-sandbox')
    options.add_argument("log-level=3")
    options.add_argument('--no-sandbox')
    if solver.lower() == "y":
        options.add_extension("./solver/solver.crx")
    else: 
        pass
    driver = webdriver.Chrome(options=options)
    wait = WebDriverWait(driver, 20)
else:
    print(f"{Colors.pink}>> {Colors.white}Visual feedback disabled!{Colors.white}")
    options = Options()
    options.add_argument(f'--user-agent={ua}')
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-infobars")
    options.add_argument("--mute-audio")
    options.add_argument('--no-sandbox')
    options.add_argument("log-level=3")
    options.add_argument("--headless")
    options.add_argument('--no-sandbox')
    if solver.lower() == "y":
        options.add_extension("./solver/solver.crx")
    else: 
        pass
    driver = webdriver.Chrome(options=options)
    wait = WebDriverWait(driver, 250)

amount = input(f"{Colors.pink}\n>> {Colors.white}How many accounts do you want to generate?: {Colors.white}")
amount = int(amount)

prox_use = input(f"{Colors.pink}>> {Colors.white}Do you want to use proxies? (y/n): {Colors.white}")

# Main Loop

while True:
    
    email = get_email()
    username = user_gen()
    password = pass_gen()
    if prox_use.lower() == "y":
        driver.quit()
        proxy = get_proxy()
        options.add_argument(f'--proxy-server={proxy}')
        driver = webdriver.Chrome(options=options)
    else: 
        proxy = "None"
    fail = False
    
    emailchoice += 1
    proxychoice += 1
    
    print(f"{Colors.pink}>> {Colors.white}Username: {username} | Password: {password} | Email: {email} | Proxy: {proxy} |{Colors.white}")
    
    amount = str(amount)
    print(f"{Colors.pink}>> {Colors.white}Amount: {emailchoice} | Hits: {hits} | Misses: {miss} {Colors.white}")
    amount = int(amount)
    
    try:
        driver.get("https://store.steampowered.com/join/")
        print(f"{Colors.pink}>> {Colors.white}Loading page...{Colors.white}")
        wait.until(EC.presence_of_element_located((By.XPATH, '/html/body')))
        print(f"{Colors.pink}>> {Colors.white}Page loaded!{Colors.white}")
    except:
        print(f"{Colors.pink}>> {Colors.white}Failed to load page!{Colors.white}")
        fail = True
        miss += 1
        
    if fail == False:
        try:
            driver.find_element(By.XPATH, '//*[@id="email"]' ).send_keys(email)
            time.sleep(random.uniform(1.8, 2.3))
            driver.find_element(By.XPATH, '//*[@id="reenter_email"]' ).send_keys(email)
            time.sleep(random.uniform(1.8, 2.3))
        except:
            print(f"{Colors.pink}>> {Colors.white}Failed to enter email!{Colors.white}")
            fail = True
            miss += 1

        if fail == False:
            if visual == "y" or visual == "Y":
                try:
                    if solver.lower() == "y":
                        time.sleep(5)
                        pyautogui.moveRel(captcha_loc[0], captcha_loc[1], duration=random.uniform(0.3, 0.5))
                        pyautogui.moveTo(captcha_loc[0], captcha_loc[1], random.uniform(0.3, 0.5))
                        time.sleep(random.uniform(0.3, 0.8))
                        pyautogui.click()
                        print(f"{Colors.pink}>> {Colors.white}Solving captcha...{Colors.white}")
                        pyautogui.moveRel(buster_loc[0], buster_loc[1], duration=random.uniform(0.3, 0.5))
                        pyautogui.moveTo(buster_loc[0], buster_loc[1], duration=random.uniform(0.3, 0.5))
                        time.sleep(random.uniform(0.3, 0.8))
                        pyautogui.click()
                        time.sleep(5)
                        if pyautogui.pixel(115, 686)[1] == 158:
                            print(f"{Colors.pink}>> {Colors.white}Captcha solved!{Colors.white}")
                    else:
                        input(f"{Colors.pink}>> {Colors.white}Please solve the captcha and press {Colors.pink}ENTER{Colors.white}!{Colors.white}")
                        while True:
                            if pyautogui.pixel(115, 686)[1] == 158:
                                print(f"{Colors.pink}>> {Colors.white}Captcha solved!{Colors.white}")
                                break
                except:
                    print(f"{Colors.pink}>> {Colors.white}Failed to solve captcha!{Colors.white}")
                    fail = True
                    miss += 1
            else:
                print(f"{Colors.pink}>> {Colors.white}Enable visual to get captcha solving!{Colors.white}")
                exit()
            if fail == False:
                try:
                    time.sleep(random.uniform(0.3, 0.8))
                    driver.find_element(By.XPATH, '//*[@id="i_agree_check"]' ).click()
                    time.sleep(random.uniform(0.3, 0.8))
                    driver.find_element(By.XPATH, '//*[@id="createAccountButton"]').click()
                    print(f"{Colors.pink}>> {Colors.white}Creating account...{Colors.white}")
                    print(f"{Colors.pink}>> {Colors.white}Please Verify Email...{Colors.white}")
                    #wait.until(EC.invisibility_of_element_located((By.XPATH, "/html/body/div[3]")))
                    input(f"{Colors.pink}>> {Colors.white}Press {Colors.pink}ENTER{Colors.white} when you have verified your email!{Colors.white}")
                    print(f"{Colors.pink}>> {Colors.white}Email Verified!{Colors.white}")
                except:
                    print(f"{Colors.pink}>> {Colors.white}Failed to click create account!{Colors.white}")
                    miss += 1
                    fail = True
                if fail == False:
                    try: 
                        driver.find_element(By.XPATH, '//*[@id="responsive_page_template_content"]/div/div[1]/div[3]/div[5]/button' ).click()
                    except:
                        pass
                    try:
                        print(f"{Colors.pink}>> {Colors.white}Waiting for page load!{Colors.white}")
                        wait.until(EC.presence_of_element_located((By.XPATH, '/html/body')))
                        print(f"{Colors.pink}>> {Colors.white}Page loaded!{Colors.white}")
                        time.sleep(random.uniform(0.3, 0.8))
                        print(f"{Colors.pink}>> {Colors.white}Entering username!{Colors.white}")
                        driver.find_element(By.XPATH, '//*[@id="accountname"]' ).send_keys(username)
                        time.sleep(random.uniform(0.3, 0.8))
                        print(f"{Colors.pink}>> {Colors.white}Entering password!{Colors.white}")
                        driver.find_element(By.XPATH, '//*[@id="password"]' ).send_keys(password)
                        driver.find_element(By.XPATH, '//*[@id="reenter_password"]' ).send_keys(password)
                        time.sleep(random.uniform(0.3, 0.8))
                        print(f"{Colors.pink}>> {Colors.white}Clicking create account!{Colors.white}")
                        driver.find_element(By.XPATH, '//*[@id="createAccountButton"]').click()
                        time.sleep(random.uniform(0.3, 0.8))
                        wait.until(EC.presence_of_element_located((By.XPATH, '/html/body')))
                        print(f"{Colors.pink}>> {Colors.white}Account created!{Colors.white}")
                        print(f"{Colors.pink}>> {Colors.white}Saving account!{Colors.white}")
                        time.sleep(2)
                    except:
                        print(f"{Colors.pink}>> {Colors.white}Failed to create account!{Colors.white}")
                        miss += 1
                        fail = True
                        pass
    elif fail == True:
        driver.quit()
        driver.delete_all_cookies()
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
        hits += 1
        amount_acc += 1
        
        driver.delete_all_cookies()
        
    if amount <= 0:
        print(f"{Colors.pink}>> {Colors.white}Done!{Colors.white}")
        print(f"{Colors.pink}>> {Colors.white}Created {Colors.pink}{amount_acc}{Colors.white} accounts!{Colors.white}")
        print(f"{Colors.pink}>> {Colors.white}Thanks for using SteamGen!{Colors.white}")
        break
