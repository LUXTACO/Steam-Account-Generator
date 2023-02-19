import os
import time
import random
import sys
import requests
import ctypes
from selenium import webdriver
from colorama import Fore
from pynput.keyboard import Controller
from selenium.webdriver.common.by import By
from pystyle import Colorate, Colors, Center

def title():
	os.system("cls")
	banner = (Colorate.Vertical(Colors.red_to_purple, """
	\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t███████╗████████╗███████╗ █████╗ ███╗   ███╗ ██████╗ ███████╗███╗   ██╗
	\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t██╔════╝╚══██╔══╝██╔════╝██╔══██╗████╗ ████║██╔════╝ ██╔════╝████╗  ██║
	\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t███████╗   ██║   █████╗  ███████║██╔████╔██║██║  ███╗█████╗  ██╔██╗ ██║
	\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t╚════██║   ██║   ██╔══╝  ██╔══██║██║╚██╔╝██║██║   ██║██╔══╝  ██║╚██╗██║
	\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t███████║   ██║   ███████╗██║  ██║██║ ╚═╝ ██║╚██████╔╝███████╗██║ ╚████║
	\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═══╝
 
========================================================================================================================                                                                             
	"""))
	print(banner)
	print (Center.XCenter(f"""{Fore.LIGHTMAGENTA_EX}
	>> {Fore.LIGHTRED_EX}Made By Taquito{Fore.LIGHTMAGENTA_EX}
	>> {Fore.LIGHTRED_EX}Version 1.0 {Fore.LIGHTMAGENTA_EX}
 """))

def gname():
	name = ['anita', 'robert', 'jones', 'laver', 'gratsher', 'killoms', 'ramez', 'sarah', 'michael', 'david', 'jennifer', 'chris', 'emily', 'john', 'jessica', 'matthew', 'ashley', 'mike', 'amanda']
	suffix = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
	
	csuffix = random.choice(suffix)
	rname = random.choice(name)

	rngsuffix = random.choice(suffix)
	i = 0
	while i < 4:
		rngsuffix += random.choice(suffix)
		i += 1

	final_name = rname + rngsuffix
	return final_name

def gpass():
	numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
	alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	
	i = 0
	password = random.choice(numbers) + random.choice(alphabet)
	while i < 4:
		password += random.choice(numbers) + random.choice(alphabet)
		i += 1

	return password

def gmail():
    # open the source file
    with open('./emails.txt', 'r') as data:
        first_line = data.readline().strip()
        email_lines = [line.strip() for line in data]

    # Filter out the used lines
    with open('./used_lines_file.txt', 'r') as used_data:
        used_lines = [line.strip() for line in used_data]
    filtered_lines = [line for line in email_lines if line not in used_lines]

    # write the used lines to another file
    with open('./used_emails.txt', 'w') as used_file:
        for line in email_lines:
            if line in used_lines:
                used_file.write(line + '\n')

    # write the remaining lines back to the original file
    with open('./emails.txt', 'w') as data:
        for line in filtered_lines:
            data.write(line + '\n')

    return first_line

amount = "unknown"
ctypes.windll.kernel32.SetConsoleTitleW("SteamGen | Accounts to generate: " + amount + " | ")
title()

url = 'https://store.steampowered.com/join?l=english'
amount = input(Center.XCenter(f">> {Fore.LIGHTRED_EX}Accounts to generate: {Fore.LIGHTMAGENTA_EX}"))
ctypes.windll.kernel32.SetConsoleTitleW("SteamGen | Accounts to generate: " + amount + " | ")

amount = int(amount)
prox = input(Center.XCenter(f">> {Fore.LIGHTRED_EX}Use proxies? (Y/N): {Fore.LIGHTMAGENTA_EX}"))
print(f" {Fore.LIGHTRED_EX}")

while amount != 0:
	email = gmail()
	passw = gpass()
	user = gname()
	amount = str(amount)
	ctypes.windll.kernel32.SetConsoleTitleW("SteamGen | Accounts to generate: " + amount + " | ")
	
	r = 0
	if prox == 'y' or prox == 'Y':
			with open('./proxies.txt', 'r') as data:
				proxy_lines = [line.strip() for line in data]
			proxy_from_file = "false"
			while (proxy_from_file == "false"):
				r += 1
				print(proxy_lines[r])
				try:
					proxies_file = {'http':'http://:@{}/'.format(proxy_lines[r])}
					requests.get("http://store.steampowered.com/", proxies=proxies_file, timeout=1.5)
				except OSError:
					print ("Proxy Connection error!")
					proxy_from_file = "false"
					sys.stdout.write("\033[F")
					sys.stdout.write("\033[K") 
					sys.stdout.write("\033[F")
					sys.stdout.write("\033[K") 
				else:
					print ("Proxy is working...")
					r += 1
					options = webdriver.ChromeOptions()
					options.add_argument('--proxy-server=%s'.format(proxy_lines[r]))
					proxy_from_file = "true"
					driver = webdriver.Chrome(options=options)
	else:
			driver = webdriver.Chrome()
			pass

	keyboard = Controller()

	driver.get(url)

	driver.find_element(By.ID, "email").send_keys(email)
 
	driver.find_element(By.ID, "reenter_email").send_keys(email)
 
	time.sleep(3)
 
	driver.find_element(By.ID, "i_agree_check").click()
	
	print("\n")
	print(Center.XCenter(f"{Fore.LIGHTMAGENTA_EX}>> {Fore.LIGHTRED_EX}Please solve the captcha! {Fore.LIGHTRED_EX}"))
	wait = input(Center.XCenter(f"{Fore.LIGHTMAGENTA_EX}>> {Fore.LIGHTRED_EX}Press ENTER to continue...\n{Fore.LIGHTRED_EX}"))
 
	driver.find_element(By.XPATH, '//*[@id="createAccountButton"]').click()
 
	print(Center.XCenter(f"{Fore.LIGHTMAGENTA_EX}>> {Fore.LIGHTRED_EX}Please verify the email: {Fore.LIGHTRED_EX}" + email + "!"))
	wait = input(Center.XCenter(f"{Fore.LIGHTMAGENTA_EX}>> {Fore.LIGHTRED_EX}Press ENTER to continue...\n{Fore.LIGHTRED_EX}"))
 
	driver.find_element(By.ID, "accountname").send_keys(user)
 
	driver.find_element(By.ID, "password").send_keys(passw)
 
	driver.find_element(By.ID, "reenter_password").send_keys(passw)
	
	driver.find_element(By.XPATH, '//*[@id="createAccountButton"]').click()
 
	amount = int(amount)
	amount -= 1
 
	account = user + ":" + passw
	with open("accounts.txt", "w") as f:
		f.write(account)
		f.write("\n")