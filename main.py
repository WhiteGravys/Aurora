# Project Swiss (Aurora 2)
# Property of auroratools.shop

# login - line 14

### Imports ###

import os
import json
import time
import requests
import sys
import select

import src.discordrpc as discordrpc
from src.frontend import *
from src.endpoints import auth
from src.roblox import api, botting, tools

### Code ###

VERSION = "2.3.4"
header = f"""


 ▄▄▄       █    ██  ██▀███   ▒█████   ██▀███   ▄▄▄         
▒████▄     ██  ▓██▒▓██ ▒ ██▒▒██▒  ██▒▓██ ▒ ██▒▒████▄       
▒██  ▀█▄  ▓██  ▒██░▓██ ░▄█ ▒▒██░  ██▒▓██ ░▄█ ▒▒██  ▀█▄     
░██▄▄▄▄██ ▓▓█  ░██░▒██▀▀█▄  ▒██   ██░▒██▀▀█▄  ░██▄▄▄▄██    
 ▓█   ▓██▒▒▒█████▓ ░██▓ ▒██▒░ ████▓▒░░██▓ ▒██▒ ▓█   ▓██▒   
 ▒▒   ▓▒█░░▒▓▒ ▒ ▒ ░ ▒▓ ░▒▓░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░ ▒▒   ▓▒█░   
  ▒   ▒▒ ░░░▒░ ░ ░   ░▒ ░ ▒░  ░ ▒ ▒░   ░▒ ░ ▒░  ▒   ▒▒ ░   
  ░   ▒    ░░░ ░ ░   ░░   ░ ░ ░ ░ ▒    ░░   ░   ░   ▒      
      ░  ░   ░        ░         ░ ░     ░           ░  ░  

White Gravy | version {VERSION} | discord.gg/aqUBsTxSjb
"""

menu = """
┌─tools────────────────────────────┐
│  [ 01 ] Ddos (ip), (port), (time)│
│  [ 02 ] Ip Pull (discord,xbox,psn│
│  [ 03 ] Port checker             │
│  [ 04 ] Fry Network (30 mins     │
│  [ 05 ] Spam repot ODP           │
│  [ 06 ] Password finder(not 100%)│
│  [ 07 ] GEOIP Lookup             │
│  [ 08 ] Post On Doxbin           │
└──────────────────────────────────┘
┌─other────────┐     ┌─support─────────┐
│  [ 0 ] Exit  │     │  [ C ] Credits  │
└──────────────┘     └─────────────────┘
"""

clear()
setTitle("Aurora II | Starting")

# check for updates
log("Checking for updates...")
try:
    upd = requests.get("https://api.auroratools.shop/data.json")
    if VERSION != upd.json()["version"]:
        log(f"There is an update available ({VERSION} -> {upd.json()['version']})")
        if yn('Would you like to download update?'):
            os.system(f"start update.exe")
            sys.exit()
except Exception as e:
    warn(f"Could not check for updates ({e})!")
    log("Please join the Discord (discord.gg/auroramultitool) and report this.")
    pause()

# config reading
log("Reading configuration file...")
try:
    CONFIG = json.load(open("config.json", "r"))
except FileNotFoundError:
    fatal("Aurora could not find 'config.json'!")
    close()
ok("Config loaded!")


# MENU 
while True:
    clear()
    setTitle("Aurora II | Main Menu")
    api.setWindowsPolicy()
    
    for line in header.splitlines():
        print(line.center(os.get_terminal_size().columns))

    for line in menu.splitlines():
        print(line.center(os.get_terminal_size().columns))
    
   

    try:
        selection = input("                 " + selector)
    except ValueError:
        continue
    
    if selection.lower() == "c":
        discordrpc.updateStatus("Browsing Credits")
        tools.credits()
