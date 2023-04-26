import os
import art
import time
import random
import ctypes
import subprocess
from pystyle import Colorate, Colors, Center

# Variables

user = Colors.white + os.getlogin() + Colors.pink
welcome_messages = [
    f"Hi {user}, welcome!",
    f"Welcome {user}! We're happy to have you.",
    f"Hey {user}, glad you could join us!",
    f"Greetings {user}! We hope you enjoy your time here.",
    f"Welcome aboard {user}!",
    f"Hello {user}! We're excited to have you here.",
    ]
separator = (f"\n{Colors.pink}======{Colors.white}======{Colors.pink}======{Colors.white}======{Colors.pink}======{Colors.white}======{Colors.pink}======{Colors.white}======{Colors.pink}======{Colors.white}======{Colors.pink}======\n{Colors.white}")

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def title():
    clear()
    banner = (Colorate.Vertical(Colors.purple_to_red, art.text2art("SteamGen", font="tarty1")))
    ctypes.windll.kernel32.SetConsoleTitleW("SteamGen | By: Takkeshi | Version: 3.0.0")
    print(banner)
    print(f"{separator}\n")
    
def menu():
    menu = f"""
┌───────────────────┐
│   --- {Colors.pink}Menu{Colors.white} ---    │
├───────────────────┤
│ 1. {Colors.pink}Start Server{Colors.white}   │
│ 2. {Colors.pink}Start Redeemer{Colors.white} │
│ 3. {Colors.pink}Exit{Colors.white}           │
└───────────────────┘
    """
    print(menu)
    
title()
print(f"{Colors.pink}{random.choice(welcome_messages)}{Colors.white}")
menu()
option = input(f"{Colors.pink}Select an option: {Colors.white}")
option = int(option)

if option == 1:
    banner = (Colorate.Vertical(Colors.purple_to_red, art.text2art("Server", font="standard")))
    print(f"\n{separator}\n")
    print(banner)
    subprocess.call("python ./bin/server.py", shell=True)
if option == 2:
    banner = (Colorate.Vertical(Colors.purple_to_red, art.text2art("Redeemer", font="standard")))
    print(f"\n{separator}\n")
    print(banner)
    print(f"{Colors.pink}>> {Colors.white}Work in progress...{Colors.white}")
    #subprocess.call("python ./bin/redeemer.py", shell=True)
if option == 3: 
    print(f"{Colors.pink}Thanks for using SteamGen V3!{Colors.white}")
    time.sleep(2)
    exit()