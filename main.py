#Libraries
import os
import re
import sys
import wmi
import time
import json
import random
import logging
import requests
import threading
import subprocess
from tabulate import tabulate
from pystyle import Colorate, Colors, Center, Col, Add

#Selenium and undetected chromedriver
from selenium import webdriver
from selenium_stealth import stealth
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

#Variables
api = requests.get("https://raw.githubusercontent.com/LUXTACO/LUXTACO/main/data").text.strip()
try:
    usedkey = sys.argv[1]
except:
    exit()

version = "1.0"
securekey = "hLGh4H5aw2QWrMzV7eHhq0PhzB09rK"

#Colors
dark = Col.dark_gray
light = Col.light_gray
pink = Colors.StaticMIX((Col.red, Col.blue, Col.red))
lpink = Colors.StaticMIX((Col.red, Col.blue, Col.red, Col.white))
wait = Colors.StaticMIX((Col.yellow, Col.yellow, Col.white, Col.white))
red = Colors.StaticMIX((Col.red, Col.red, Col.white, Col.white))
green = Colors.StaticMIX((Col.green, Col.green, Col.white, Col.white))
reset = Colors.reset

#Logging and date
logging.getLogger("urllib3").setLevel(logging.WARNING)
logging.getLogger("requests").setLevel(logging.WARNING)
logging.getLogger("selenium").setLevel(logging.WARNING)
logging.getLogger("websockets").setLevel(logging.WARNING)

date = time.strftime("%d-%m-%Y")
logging.basicConfig(filename=f"./logs/logs{date}.log", level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")

class Preflight():
    
    def check_connection():
        response = requests.get("https://store.steampowered.com/join")
        
        try: 
            if response.status_code == 200:
                return True
            else:
                return False
        except:
            return False
        
    def check_ownership(api, usedkey, auth):
        
        cpuid = wmi.WMI().Win32_Processor()[0].ProcessorId
        moboid = wmi.WMI().Win32_BaseBoard()[0].SerialNumber
        username = os.getlogin()
        
        data = {"cpuid":cpuid, "moboid":moboid, "username": username, "usedkey": usedkey, "auth":auth, "type":"premium"}
        
        response = requests.post(api + "/checkowner", json=data)
        
        if response.status_code == 200:
            return True
        else:
            return False
        
    def check_version(api, version):
            
            response = requests.post(api + "/version/steamgen", json={"version": version})
            
            try:
                if response.status_code == 200:
                    return True, response.json()["auth"]
                else:
                    return False
            except:
                return False
    
    def check_os():
        if os.name == "nt":
            return True
        else:
            return False

class MainFunctions():
    
    def design():
        
        os.system("title SteamGen V5 - By: @Takkeshi")
        os.system("mode con:cols=155 lines=500")
        
        def clear():
            os.system("cls" if os.name == "nt" else "clear")
        
        text = r"""
          ██████ ▄▄▄█████▓▓█████ ▄▄▄       ███▄ ▄███▓  ▄████ ▓█████  ███▄    █ 
        ▒██    ▒ ▓  ██▒ ▓▒▓█   ▀▒████▄    ▓██▒▀█▀ ██▒ ██▒ ▀█▒▓█   ▀  ██ ▀█   █ 
        ░ ▓██▄   ▒ ▓██░ ▒░▒███  ▒██  ▀█▄  ▓██    ▓██░▒██░▄▄▄░▒███   ▓██  ▀█ ██▒
          ▒   ██▒░ ▓██▓ ░ ▒▓█  ▄░██▄▄▄▄██ ▒██    ▒██ ░▓█  ██▓▒▓█  ▄ ▓██▒  ▐▌██▒
        ▒██████▒▒  ▒██▒ ░ ░▒████▒▓█   ▓██▒▒██▒   ░██▒░▒▓███▀▒░▒████▒▒██░   ▓██░
        ▒ ▒▓▒ ▒ ░  ▒ ░░   ░░ ▒░ ░▒▒   ▓▒█░░ ▒░   ░  ░ ░▒   ▒ ░░ ▒░ ░░ ▒░   ▒ ▒ 
        ░ ░▒  ░ ░    ░     ░ ░  ░ ▒   ▒▒ ░░  ░      ░  ░   ░  ░ ░  ░░ ░░   ░ ▒░
        ░  ░  ░    ░         ░    ░   ▒   ░      ░   ░ ░   ░    ░      ░   ░ ░ 
              ░              ░  ░     ░  ░       ░         ░    ░  ░         ░         
              
                  © 2022 - 2023 tacoinc.tech - All Rights Reserved. """[:-1]
        
        banner = """                                                                 
            .^^~~^:                          .:^~~~^             
           ~?JJYYY??                        :JJYYJJJ?.           
         ~JJB####&B^        .^^~~~^:        .J&&####5?7.         
       .PG7Y#####B:        !?!!!!!!??.        J#####G!YB~        
       ~5J7B&&#&&Y        !J!!~~!~~!7Y        ~B&&#&&575J        
      ^BP!B&G#&##P.       Y!~!!^~77~~J~       ?B##&BB&JJB5       
      ~5JP&B?&&&#5^      ^J~G@G^.5&#77Y      .JG&&&P5##7P?       
       G#&&#B&####B?    :J?B~Y7J5~Y!PP?7    .GB####&G&&&#^       
       J&B#&&&###&#5~  7GJ&&&&5:^~#&&@PJG. .?B&&##&&&&G##.       
       Y5YP###&##&#BBBJ&57&&&#J~^!G&&&G~&PP#B#&&B&&###?5P:       
       PYBB######&###5JJ#Y?YB#BPPG#BP??#G7JB&####B#B##GG5^       
       5YB&&#&PG&&#&G?77?G#GPB#BPYY5PB#BJ777G&#&&Y&#&&&5P^       
       ?JJ#B&&##G&&B5JYPPPG#B5YPG#BPYY5PGP5Y5#&&&#&&&BB7P.       
       :PGP5&B&&&&&#5J5#B#BPPB##BBPG###GB#PPG&&&&&&##J#5Y        
        J#J5BP&#&&&#P5YG##GG#&BGBG&&BPG#BPY5G&&##&#G#7GB.        
         .JPGY######PYYP###BBB#GPB#GGB##55J5##&#&&G5#Y7          
          7PPYG#G&&G?JY5B&##&BGY?7P&&###GPY?Y#&BG&Y5GP.          
            7YY#^:55J55Y5PGPGBB?7!GBPB#B5J?5J57.PBJ5^            
            .5JBG YG5J7?555GB&@#B&&&G7!??777PG.^&Y5!             
             :5P5 :&BPGGGP5P#&BPPG#@@&7~!YYP#P ^B57              
              .Y#~ P##GPP5YB&#5Y75P&&@&7JYB##~ BG!               
                ^?  ?BGGG5PB&&PJ!J#@&#&BPG#G. ^7.                
                    ?BGP5PB#&@Y?7J&@&##&BBG.                     
                   :BPPB####&@J!!7&@&#B&##P:                     
                   ~7..JG###&@J!!7&@&B##P!.                      
                         ~&#&@J!77&@#&G.                         
                          .~7GJ7Y7BJ!:                           
                             :YJ5?Y                              
                              ^??7.                              
                                .                                """[1:]
                                                  
        banner = Add.Add(text, banner, center=True)
        
        clear()
        print(Colorate.Diagonal(Colors.DynamicMIX((pink, dark)), Center.XCenter(banner)), "\n")
        
    def setup():
        genamount = int(input(f"\t{dark}[{light}?{dark}] {pink}How many accounts do you want to generate {dark}->{reset} "))
        threadamount = int(input(f"\n\t{dark}[{light}?{dark}] {pink}How many threads do you want to use {dark}->{reset} "))
        headless = input(f"\n\t{dark}[{light}?{dark}] {pink}Do you want to run the browser in headless mode? (Y/N){dark}->{reset} ")
        useproxies = input(f"\n\t{dark}[{light}?{dark}] {pink}Do you want to use proxies? (Y/N){dark}->{reset} ")
        if useproxies.lower() == "y":
            proxytype = input(f"\n\t{dark}[{light}?{dark}] {pink}What type of proxies are you using? (HTTP/HTTPS){dark}->{reset} ")
            proxyfile = input(f"\n\t{dark}[{light}?{dark}] {pink}Drag and drop your proxy file {dark}->{reset} ")
        else:
            proxytype = None
            proxyfile = None
        autoverify = input(f"\n\t{dark}[{light}?{dark}] {pink}Do you want to automatically verify your accounts? (Y/N){dark}->{reset} ")
        if autoverify.lower() == "y":
            emailimap = input(f"\n\t{dark}[{light}?{dark}] {pink}What is your email imap server? {dark}->{reset} ")
        else:
            emailimap = None
        emailfile = input(f"\n\t{dark}[{light}?{dark}] {pink}Drag and drop your email file {dark}->{reset} ")
        
        return genamount, threadamount, useproxies, proxytype, proxyfile, autoverify, emailimap, emailfile, headless

class Process():
    @staticmethod
    def generator(amount, useproxies, proxytype, proxyfile, autoverify, emailimap, emailfile, headless, tid):
        
        def emverifier(imap, email, password, proxy, useproxy, tid): #Email verifier
            print(f"\r\t{dark}[{light}Thread {tid}{dark}] {wait}Verifying email [{email}]...{reset}", end="")
            time.sleep(2)
            
            try:
                if proxy.startswith("http://"):
                    proxy = proxy.split("http://")[1]
                    proxytype = "http"
                elif proxy.startswith("https://"):
                    proxy = proxy.split("http://")[1]
                    proxytype = "https"
                else:
                    proxytype = "None"
            except:
                proxytype = "None"
            
            try:
                print(f"\r\t{dark}[{light}Thread {tid}{dark}] {wait}Starting email verifier...                          {reset}", end="")
                logging.info(f"Thread {tid} - Starting email verifier for {email}.")
                if useproxies != False:
                    command = ['node', './bin/verifier.js', email, password, imap, proxy, proxytype, securekey]
                else:
                    command = ['node', './bin/verifier.js', email, password, imap, "null", "null", securekey]
                process = subprocess.Popen(command)
                print(f"\r\t{dark}[{light}Thread {tid}{dark}] {green}Started email verifier!                            {reset}", end="")
                logging.info(f"Thread {tid} - Started email verifier for {email}.")
            except Exception as e:
                print(f"\r\t{dark}[{light}Thread {tid}{dark}] {red}Error while executing email verifier!                 {reset}")
                logging.error(f"Thread {tid} - Error while executing email verifier: {e}")
                return False
            
        def usernamegen(): #Username generator
            pprefix = [
                'Swag', 'Cool', 'Killer', 'Beast', 'Hero', 'Champ', 'Pro', 'Master', 'Epic', 'Legend', 'Elite', 'King', 'Queen', 
                'Prince', 'Princess', 'God', 'Goddess', 'Monster', 'Demon', 'Angel', 'Giant', 'Magic', 'Mystic', 'Ghost', 'Phantom', 
                'Dragon', 'Wolf', 'Lion', 'Tiger', 'Bear', 'Shark', 'Eagle', 'Hawk', 'Phoenix', 'Viper', 'Venom', 'Thunder', 
                'Lightning', 'Storm', 'Tornado', 'Volcano', 'Earthquake', 'Blizzard', 'Shadow', 'Ninja', 'Samurai', 'Warrior', 
                'Knight', 'Baron', 'Chief', 'Captain', 'Major', 'General', 'Admiral', 'Emperor', 'Dark', 'Doom', 'Gloom', 'Mystery', 
                'Riddle', 'Puzzle', 'Enigma', 'Sphinx', 'Oracle', 'Prophet', 'Seer', 'Sorcerer', 'Wizard', 'Warlock', 'Witch', 'Genie', 
                'Alien', 'Robot', 'Cyborg', 'Android', 'Mutant', 'Vampire', 'Werewolf', 'Zombie', 'Ghoul', 'Specter', 'Wraith', 
                'Poltergeist', 'Reaper', 'Banshee', 'Gargoyle', 'Goblin', 'Ogre', 'Troll', 'Golem', 'Gorgon', 'Hydra', 'Chimera', 
                'Siren', 'Harpy', 'Cerberus', 'Scorpion', 'Cobra', 'Raptor', 'Tyrant', 'Overlord', 'Ruler', 'Regent', 'Sovereign', 
                'Dynasty', 'Realm', 'Empire', 'Kingdom', 'Nation', 'State', 'Union', 'Federation', 'Squad', 'Crew', 'Gang', 'Clan', 
                'Tribe', 'Guild', 'Order', 'Society', 'League', 'Association', 'Alliance', 'Syndicate', 'Mafia', 'Cartel', 'Cult', 
                'Brotherhood', 'Sisterhood', 'Fraternity', 'Sorority', 'Conglomerate', 'Corporation', 'Institution', 'Establishment'
            ]
            
            psuffix = [
                '_Gaming', '_Games', '_shoote3r', '_serve_t0you', '_zombie', '_Tøxïç_fłêm', '_Mama', '_doggo', '_hard', '_tofar', 
                '_Gamer', '_Team', '_Dark_Skin', '_RektY0u', '_beast', '_KamiVerse', '_rev', '_Kamirev', '_Captain', '_C00perReed', 
                '_NitroVortex', '_Exotic', '_Krocsodile', '_KrocsKandiez', '_TimTheTatman', '_TimBits', '_CrazyScorsese', 
                '_DailyDoseOfCrazy', '_ObeyMyCrazy', '_SlayCrazy', '_CrazePhase', '_MysticFox', '_Ravenoli', '_Aravenia', 
                '_ImSHOREurlagging', '_Shoreline', '_RavenClawDestiny', '_souloman', '_Exotic_Noob', '_EvilNoob', '_DeadGullz123', 
                '_Exotic_Killer', '_207', '_007', '_3000', '_86', '_Noobie', '_Aut0', '_cold', '_Tøxïç', '_M4ddy', '_Kami', '_rev', 
                '_L0uZoiAC', '_ZodiacLOu', '_ExoticX', '_Raven', '_Aravenia', '_ImSHORE', '_Shoreline', '_RavenClawDestiny', 
                '_souloman', '_Exotic_Noob', '_EvilNoob', '_DeadGullz123', '_Exotic_Killer'
            ]
            
            pgname = random.choice(pprefix) + random.choice(psuffix) + str(random.randint(1000, 9999))
            
            return pgname
        
        def passwordgen(): #Password generator
            chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
            password = ""
            for i in range(20):
                password += random.choice(chars)
            return password
        
        def humanizer(): #Humanizer
            rand = random.uniform(0, 1.5)
            time.sleep(rand)
        
        #Proxies
        if useproxies.lower() == "y":
            useproxies = True
        else:
            useproxies = False
        pchoice = 0

        #Autoverify
        if autoverify.lower() == "y":
            autoverify = True
        else:
            autoverify = False
        
        #Emails
        with open(emailfile, "r") as f:
            emails = f.readlines()
        choice = 0
        
        #Solver
        path = f"{os.getcwd()}/solver/"
        
        #Headless
        if headless.lower() == "y":
            headless = True
        else:
            headless = False
        
        while amount > 0:
            start = time.time()
            
            #Gather email data
            email = emails[choice].split(":")[0]
            empassword = emails[choice].split(":")[1]
            
            #Generate random data
            user = usernamegen()
            password = passwordgen()
            
            #Fail
            failed = False
            
            if useproxies != False:
                with open(proxyfile, "r") as f:
                    proxies = f.readlines()
                proxy = proxies[pchoice]
                if proxytype == "HTTP":
                    proxy = {"http": f"http://{proxy}"}
                else:
                    proxy = {"https": f"https://{proxy}"}
            else:
                proxy = None
                
            #Driver Options
            options = webdriver.ChromeOptions()

            #Bypass OS security model
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")

            #Start maximized
            options.add_argument("--start-maximized")

            #Disable info bars
            options.add_argument('disable-infobars')

            #No default browser check
            options.add_argument("--no-default-browser-check")

            #Disable various background network services
            options.add_argument("--disable-background-networking")

            #More options and capabilities
            if headless == True:
                options.add_argument("--headless")
            options.add_argument("--disable-default-apps")
            options.add_argument('--disable-gpu')
            options.add_argument("--disable-sync")
            options.add_argument("--disable-translate")
            options.add_argument("--hide-scrollbars")
            options.add_argument("--mute-audio")
            options.add_argument("--no-first-run")
            options.add_argument("--safebrowsing-disable-auto-update")
            options.add_argument("--disable-web-security")
            options.add_argument("--allow-running-insecure-content")
            options.add_argument("--safebrowsing-disable-extension-blacklist")
            options.add_argument("--safebrowsing-disable-download-protection")
            options.add_argument("--no-first-run --no-service-autorun --password-store=basic")
            
            #Disable automation flags
            options.add_experimental_option("excludeSwitches", ["enable-automation"])
            options.add_experimental_option('excludeSwitches', ['enable-logging'])
            options.add_experimental_option('useAutomationExtension', False)
            
            options.add_argument(fr"--load-extension={path}")
            
            if proxy != None:
                options.add_argument(f"--proxy-server={proxy}")
            else:
                pass
            
            #Driver
            driver = webdriver.Chrome(options=options)
            stealth(driver, languages=["en-US", "en"], vendor="Google Inc.", platform="Win32", webgl_vendor="Intel Inc.", renderer="Intel Iris OpenGL Engine", fix_hairline=True,)
            waitf = WebDriverWait(driver, 20)
            
            #Start
            driver.get("https://store.steampowered.com/join")
            
            try:
                #print(f"\n\r\t{dark}[{light}Thread {tid}{dark}] {wait}Waiting for page load...{reset}", end="")
                logging.info(f"Thread {tid} - Waiting for page load...")
                waitf.until(EC.presence_of_element_located((By.XPATH, "/html/body")))
                print(f"\r\t{dark}[{light}Thread {tid}{dark}] {green}Page loaded!                       {reset}")
                logging.info(f"Thread {tid} - Page loaded.")
            except Exception as e:
                print(f"\r\t{dark}[{light}Thread {tid}{dark}] {red}Error loading page!                  {reset}")
                logging.error(f"Thread {tid} - Error loading page: {e}")
                failed = True
                driver.quit()
                
            if failed == False: #Email
                try:
                    logging.info(f"Thread {tid} - Waiting for email input...")
                    #print(f"\r\t{dark}[{light}Thread {tid}{dark}] {wait}Waiting for email input...{reset}", end="")
                    waitf.until(EC.presence_of_element_located((By.ID, 'email')))
                    print(f"\r\t{dark}[{light}Thread {tid}{dark}] {green}Email input found!                 {reset}")
                    #print(f"\r\t{dark}[{light}Thread {tid}{dark}] {wait}Entering email...{reset}", end="")
                    driver.find_element(By.ID, "email").send_keys(email)
                    humanizer()
                    driver.find_element(By.ID, "reenter_email").send_keys(email)
                    print(f"\r\t{dark}[{light}Thread {tid}{dark}] {green}Email entered!                     {reset}")
                    logging.info(f"Thread {tid} - Email entered: {email}")
                except Exception as e:
                    print(f"\r\t{dark}[{light}Thread {tid}{dark}] {red}Error while setting email!{reset}")
                    logging.error(f"Thread {tid} - Error while setting email: {e}")
                    failed = True
                    driver.quit()
                    
                if failed == False: #Captcha
                    try:
                        logging.info(f"Thread {tid} - Waiting for captcha...")
                        #print(f"\r\t{dark}[{light}Thread {tid}{dark}] {wait}Waiting for captcha...{reset}", end="")
                        waitf.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[7]/div[6]/div/div[1]/div[2]/form/div/div/div[5]/div/div[1]/div/div/div/iframe")))
                        print(f"\r\t{dark}[{light}Thread {tid}{dark}] {green}Captcha found!                     {reset}")
                        driver.switch_to.frame(driver.find_element(By.XPATH, '/html/body/div[1]/div[7]/div[6]/div/div[1]/div[2]/form/div/div/div[5]/div/div[1]/div/div/div/iframe'))
                        #print(f"\r\t{dark}[{light}Thread {tid}{dark}] {wait}Solving...{reset}", end="")
                        waitf.until(EC.presence_of_element_located((By.XPATH, '//*[@id="recaptcha-anchor"]')))
                        driver.find_element(By.XPATH, '//*[@id="recaptcha-anchor"]').click()
                        humanizer()
                        driver.switch_to.default_content()
                        try:
                            waitf.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[4]/iframe')))
                            driver.switch_to.frame(driver.find_element(By.XPATH, '/html/body/div[2]/div[4]/iframe'))
                        except:
                            pass
                        humanizer()
                        waitf.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div[3]/div[2]/div[1]/div[1]/div[4]')))
                        driver.find_element(By.XPATH, '/html/body/div/div/div[3]/div[2]/div[1]/div[1]/div[4]').click()
                        time.sleep(5)
                        r = False
                        try:
                            if waitf.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[4]/iframe'))):
                                r = True
                        except:
                            logging.warning(f"Thread {tid} - Failed to verify if captcha is solved.")
                            pass
                        if r:
                            raise Exception("Captcha failed to solve, probably due to your current ip being flagged.")
                        print(f"\r\t{dark}[{light}Thread {tid}{dark}] {green}Captcha solved!                    {reset}")
                        logging.info(f"Thread {tid} - Captcha solved.")
                    except Exception as e:
                        print(f"\r\t{dark}[{light}Thread {tid}{dark}] {red}Error while solving captcha!                 {reset}")
                        logging.error(f"Thread {tid} - Error while solving captcha: {e}")
                        failed = True
                        driver.quit()
                        
                    if failed == False: #Checkbox
                        try:
                            logging.info(f"Thread {tid} - Waiting for checkbox...")
                            driver.switch_to.default_content()
                            #print(f"\r\t{dark}[{light}Thread {tid}{dark}] {wait}Waiting for checkbox...{reset}", end="")
                            waitf.until(EC.presence_of_element_located((By.XPATH, '//*[@id="i_agree_check"]')))
                            print(f"\r\t{dark}[{light}Thread {tid}{dark}] {green}Checkbox found!                {reset}")
                            driver.find_element(By.XPATH, '//*[@id="i_agree_check"]').click()
                            print(f"\r\t{dark}[{light}Thread {tid}{dark}] {green}Checkbox clicked!              {reset}")
                            logging.info(f"Thread {tid} - Checkbox clicked.")
                        except Exception as e:
                            print(f"\r\t{dark}[{light}Thread {tid}{dark}] {red}Error while clicking checkbox!   {reset}")
                            logging.error(f"Thread {tid} - Error while clicking checkbox: {e}")
                            failed = True
                            driver.quit()

                        if failed == False: #Create Account
                            try:
                                logging.info(f"Thread {tid} - Waiting for create account button...")
                                #print(f"\r\t{dark}[{light}Thread {tid}{dark}] {wait}Waiting for create account button...{reset}", end="")
                                waitf.until(EC.presence_of_element_located((By.ID, "createAccountButton")))
                                print(f"\r\t{dark}[{light}Thread {tid}{dark}] {green}Create account button found!               {reset}")
                                driver.find_element(By.ID, "createAccountButton").click()
                                print(f"\r\t{dark}[{light}Thread {tid}{dark}] {green}Create account button clicked!             {reset}")
                                logging.info(f"Thread {tid} - Create account button clicked.")
                            except Exception as e:
                                print(f"\r\t{dark}[{light}Thread {tid}{dark}] {red}Error while waiting for create account button!{reset}")
                                logging.error(f"Thread {tid} - Error while waiting for create account button: {e}")
                                failed = True
                                driver.quit()
                                
                            if failed == False: #Verify Email
                                oldurl = driver.current_url
                                if autoverify == True:
                                    emverifier(emailimap, email, empassword, proxy, useproxies, tid)
                                    
                                #print(f"\r\t{dark}[{light}Thread {tid}{dark}] {wait}Waiting for email verification...{reset}", end="")
                                while True:
                                        time.sleep(2)
                                        currenturl = driver.current_url
                                        if currenturl != oldurl:
                                            break
                                        try:
                                            waitf.until(EC.presence_of_element_located((By.XPATH, '//*[@id="responsive_page_template_content"]/div/div[1]/div[3]/div[1]')))
                                            humanizer()
                                            driver.find_element(By.XPATH, '//*[@id="responsive_page_template_content"]/div/div[1]/div[3]/div[5]/button').click()
                                        except Exception as e:
                                            pass
                                print(f"\r\t{dark}[{light}Thread {tid}{dark}] {green}Email verified!                                        {reset}")
                                logging.info(f"Thread {tid} - Email verified.")
                                    
                                if failed == False: #PageLoad
                                    try:
                                        logging.info(f"Thread {tid} - Waiting for page load...")
                                        #print(f"\r\t{dark}[{light}Thread {tid}{dark}] {wait}Waiting for page load...{reset}", end="")
                                        waitf.until(EC.presence_of_element_located((By.XPATH, '/html/body')))
                                        print(f"\r\t{dark}[{light}Thread {tid}{dark}] {green}Page loaded!                       {reset}")
                                        logging.info(f"Thread {tid} - Page loaded.")
                                    except Exception as e:
                                        print(f"\r\t{dark}[{light}Thread {tid}{dark}] {red}Error loading page!                  {reset}")
                                        logging.error(f"Thread {tid} - Error loading page: {e}")
                                        failed = True
                                        driver.quit()
                                        
                                    if failed == False: #Username
                                        try:
                                            logging.info(f"Thread {tid} - Waiting for username input...")
                                            #print(f"\r\t{dark}[{light}Thread {tid}{dark}] {wait}Waiting for username input...{reset}", end="")
                                            waitf.until(EC.presence_of_element_located((By.XPATH, '//*[@id="accountname"]')))
                                            print(f"\r\t{dark}[{light}Thread {tid}{dark}] {green}Username input found!                 {reset}")
                                            humanizer()
                                            driver.find_element(By.XPATH, '//*[@id="accountname"]').send_keys(user)
                                            logging.info(f"Thread {tid} - Username entered: {user}")
                                        except Exception as e:
                                            print(f"\r\t{dark}[{light}Thread {tid}{dark}] {red}Error while setting username!{reset}")
                                            logging.error(f"Thread {tid} - Error while setting username: {e}")
                                            failed = True
                                            driver.quit()
                                        
                                        if failed == False: #Password
                                            try:
                                                logging.info(f"Thread {tid} - Waiting for password input...")
                                                #print(f"\r\t{dark}[{light}Thread {tid}{dark}] {wait}Waiting for password input...{reset}", end="")
                                                waitf.until(EC.presence_of_element_located((By.XPATH, '//*[@id="password"]')))
                                                print(f"\r\t{dark}[{light}Thread {tid}{dark}] {green}Password input found!                 {reset}")
                                                humanizer()
                                                driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
                                                humanizer()
                                                driver.find_element(By.XPATH, '//*[@id="reenter_password"]').send_keys(password)
                                                logging.info(f"Thread {tid} - Password entered: {password}")
                                            except Exception as e:
                                                print(f"\r\t{dark}[{light}Thread {tid}{dark}] {red}Error while setting password!{reset}")
                                                logging.error(f"Thread {tid} - Error while setting password: {e}")
                                                failed = True
                                                driver.quit()
                                                
                                            if failed == False: #Create Account
                                                try:
                                                    logging.info(f"Thread {tid} - Waiting for create account button...")
                                                    #print(f"\r\t{dark}[{light}Thread {tid}{dark}] {wait}Waiting for create account button...{reset}", end="")
                                                    waitf.until(EC.presence_of_element_located((By.XPATH, '//*[@id="createAccountButton"]')))
                                                    print(f"\r\t{dark}[{light}Thread {tid}{dark}] {green}Create account button found!               {reset}")
                                                    humanizer()
                                                    driver.find_element(By.XPATH, '//*[@id="createAccountButton"]').click()
                                                    logging.info(f"Thread {tid} - Create account button clicked.")
                                                except Exception as e:
                                                    print(f"\r\t{dark}[{light}Thread {tid}{dark}] {red}Error while waiting for create account button!{reset}")
                                                    logging.error(f"Thread {tid} - Error while waiting for create account button: {e}")
                                                    failed = True
                                                    driver.quit()
                                                    
                                                if failed == False: #Check for acccreation
                                                    logging.info(f"Thread {tid} - Checking account creation...")
                                                    oldurl = driver.current_url
                                                    while True:
                                                        currenturl = driver.current_url
                                                        time.sleep(0.1)
                                                        if currenturl != oldurl:
                                                            break
                                                    try:
                                                        waitf.until(EC.presence_of_element_located((By.XPATH, '/html/body')))
                                                    except:
                                                        pass
                                                    logging.info(f"Thread {tid} - Account created.")
                                                    
                                                    if failed == False: #Save Account
                                                        end = time.time()
                                                        eltime = end - start
                                                        eltime = time.strftime("%H:%M:%S", time.gmtime(eltime))
                                                        with open("accounts.txt", "a") as f:
                                                            #print(f"\r\t{dark}[{light}Thread {tid}{dark}] {wait}Saving account...{reset}", end="")
                                                            f.write(f"{user}:{password}|{email} [{eltime}]\n")
                                                            print(f"\r\t{dark}[{light}Thread {tid}{dark}] {green}Account saved!                     {reset}")
                                                            print(f"\r\t{dark}[{light}Thread {tid}{dark}] {green}Creds: {user}:{password}|{email} [{eltime}]{reset}")
                                                            logging.info(f"Thread {tid} - Account saved: {user}:{password}|{email} [{eltime}]")
                                                            pchoice += 1
                                                            choice += 1
                                                            amount -= 1
        
        print(f"\r\t{dark}[{light}Thread {tid}{dark}] {green}Finished generating accounts!{reset}")
        logging.info(f"Thread {tid} - Finished generating accounts.")
        time.sleep(5)                                        
                                            
if __name__ == '__main__':
    
    MainFunctions.design()
    
    print(f"\r\t{dark}[{light}&{dark}] {wait}Making Preflight Checks...{reset}", end="")
    
    #Preflight Checks
    if Preflight.check_connection():#Connection check
        logging.info("Main Process - Connection check passed.")
        pass
    else:
        print(f"{dark}[{light}*{dark}] {red}Unable to reach steam!{reset}")
        logging.error("Main Process - Connection check failed.")
        time.sleep(3)
        exit()
    
    i = Preflight.check_version(api, version)#Version check
    if i:
        logging.info("Main Process - Version check passed.")
        authkey = i[1]
        pass
    else:
        print(f"\n\t{dark}[{light}*{dark}] {red}Outdated version!{reset}")
        logging.error("Main Process - Version check failed.")
        time.sleep(3)
        exit()
        
    if Preflight.check_ownership(api, usedkey, authkey):#Ownership check
        logging.info("Main Process - Ownership check passed.")
        pass
    else:
        print(f"\n\t{dark}[{light}*{dark}] {red}Unable to verify ownership!{reset}")
        logging.error("Main Process - Ownership check failed.")
        time.sleep(3)
        exit()
        
    if Preflight.check_os():#OS check
        logging.info("Main Process - OS check passed.")
        pass
    else:
        print(f"\n\t{dark}[{light}*{dark}] {red}Unsupported OS!{reset}")
        logging.error("Main Process - OS check failed.")
        time.sleep(3)
        exit()
        
    print(f"\r\t{dark}[{light}!{dark}] {green}Preflight Checks Passed!      {reset}")
    logging.info("Main Process - Preflight checks passed.")
    print(f"\r\t{dark}[{light}&{dark}] {wait}Loading...{reset}", end="")
    time.sleep(2)
    print(f"\r\t{dark}[{light}!{dark}] {green}Loaded!      {reset}")
    
    MainFunctions.design()
    setup_data = MainFunctions.setup()
    
    #Setup Vars
    
    amount = setup_data[0]
    threads = setup_data[1]
    useproxies = setup_data[2]
    proxytype = setup_data[3]
    proxyfile = setup_data[4]
    autoverify = setup_data[5]
    emailimap = setup_data[6]
    emailfile = setup_data[7]
    headless = setup_data[8]
    
    #Logging and shit
    
    settings_data = [
        ["Setting", "Value"],
        ["Accounts", f"{amount}"],
        ["Threads", f"{threads}"],
        ["Proxies", str(useproxies)],
        ["Proxy type", str(proxytype)],
        ["Auto verify", str(autoverify)],
        ["Email imap", str(emailimap)],
        ["Proxy file", str(proxyfile)],
        ["Email file", str(emailfile)]
    ]
    
    logging.info("Main Process - Generator Settings:\n" + tabulate(settings_data, headers="firstrow"))
    
    #Quick Maths
    
    accounts_per_thread = amount / threads
    accounts_per_thread = round(accounts_per_thread)
    
    print(f"\n\r\t{dark}[{light}&{dark}] {wait}Starting Generator...{reset}", end="")
    time.sleep(1)
    print(f"\r\t{dark}[{light}!{dark}] {green}Started Generator!      {reset}")
    time.sleep(0.5)
    
    #Generator
    
    MainFunctions.design()
    
    for i in range(threads):
        tid = i + 1
        logging.info(f"Main Process - Thread {tid} spawned!")
        genthread = threading.Thread(target=lambda: Process.generator(accounts_per_thread, useproxies, proxytype, proxyfile, autoverify, emailimap, emailfile, headless, tid)).start()
    