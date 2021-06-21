import time
import requests
import re
import math
import concurrent.futures
import ctypes
from colorama import Fore, Style
from requests import Session
import string
import random
import requests
import time
import os

sent = 0
session = Session()
b = Style.BRIGHT
os = os.system
os('cls')



#Setting the window up
ctypes.windll.kernel32.SetConsoleTitleW(f"[OG USERNAME GENERATOR] | STATUS: WAITING...")

print(f"""

{b + Fore.BLUE}

                         ▒█▀▀▀█ ▒█▀▀█ 　 ▒█▀▀█ ▒█▀▀▀ ▒█▄░▒█ ▒█▀▀▀ ▒█▀▀█ ░█▀▀█ ▀▀█▀▀ ▒█▀▀▀█ ▒█▀▀█ 
                         ▒█░░▒█ ▒█░▄▄ 　 ▒█░▄▄ ▒█▀▀▀ ▒█▒█▒█ ▒█▀▀▀ ▒█▄▄▀ ▒█▄▄█ ░▒█░░ ▒█░░▒█ ▒█▄▄▀ 
                         ▒█▄▄▄█ ▒█▄▄█ 　 ▒█▄▄█ ▒█▄▄▄ ▒█░░▀█ ▒█▄▄▄ ▒█░▒█ ▒█░▒█ ░▒█░░ ▒█▄▄▄█ ▒█░▒█
                                                                                                        
                                          Developed by ItzXitadoo#1188  v1.0


{b + Fore.GREEN} > {Fore.RESET}Options {b + Fore.GREEN}< """)

#Input stuff
StringAmount = input(f"{b + Fore.BLUE} > Enter the number of strings{Fore.RESET}: ")
Wordamount = input(f"{b + Fore.BLUE} > Enter the number of user names{Fore.RESET}: ")

#Variables
generated = []
available_names = []
invalid_names = []

#Nick Generator Tool
def generator(size=int(StringAmount), chars=string.ascii_letters + string.digits): return ''.join(
    random.choice(chars) for _ in range(size))


ctypes.windll.kernel32.SetConsoleTitleW(f"[OG USERNAME GENERATOR] | STATUS: GENERATING...")

#Generating & Saving the usernames
for x in range(0, int(Wordamount)):

    current = generator()
    generated.append(current)

    with open('generated.txt', 'a') as file:
        file.write(f'{generated[x]}\n')


ctypes.windll.kernel32.SetConsoleTitleW(f"[OG USERNAME GENERATOR] | STATUS: CHECKING...")
print(f'{b + Fore.LIGHTMAGENTA_EX} Processing... This might take a few seconds')

#userName checker tool
def check_username(username):
    retry = True
    while retry:
        retry = False
        result = bool(regex.search(username))
        if not (result or (len(username) < 3) or (len(username) > 16)):

            res = requests.get('https://api.mojang.com/users/profiles/minecraft/' + username)

            if res.status_code == 200:
                invalid_names.append(username)

            elif res.status_code == 204:
                available_names.append(username)
            
            elif res.status_code == 429:

                end_time = time.time()
                global start_time
                time_to_wait = math.ceil(600 - (end_time - start_time))
                global rate_limited

                if not rate_limited:

                    rate_limited = True
                    print(f'{b + Fore.YELLOW} Request is being refused due to IP being rate limited. Waiting {time_to_wait} seconds before reattempting...')
                retry = True
                time.sleep(time_to_wait)
                rate_limited = False
                start_time = time.time()

            else:

                res.raise_for_status()
                print(f'{b + Fore.BLUE} Unhandled HTTP status code: {res.status_code}.')

        else:

            print(f'{username} is an invalid username.')
            invalid_names.append(username)

#Getting the generated.txt content and properly setting it up in the code
with open('generated.txt') as name_list:

    username_list = [line.strip() for line in name_list]
    if not username_list:
        print(f'Directory is empty.')


regex = re.compile(r'[^a-zA-Z0-9_.]')
rate_limited = False
start_time = time.time()

#Properly Checking
with concurrent.futures.ThreadPoolExecutor() as executor:
    try:
        executor.map(check_username, username_list)
    except Exception as exc:
        print(f'There is a problem: {exc}.')


#Exposing the results
print()
print(f'{b + Fore.GREEN} [+] Available username(s): {available_names}')
print(f'{b + Fore.RED} [-] Invalid username(s): {invalid_names}')


#Clearing the generated text file
f = open('generated.txt', 'r+')
f.truncate(0)

#Saving the OG names
if available_names:
    for x in range(0, len(available_names)):
        with open('ognames.txt', 'a') as file:
            file.write(f'{available_names[x]}\n')

#Finish alert
print(f'{b + Fore.LIGHTGREEN_EX} All the good usernames were saved on the programs directory on a file called "ognames.txt"')

#Finish Status Update
ctypes.windll.kernel32.SetConsoleTitleW(f"[OG USERNAME GENERATOR] | STATUS: FINISHED | GOOD USERNAMES: {len(available_names)}")

#Telling the app to wait for user input to close
input()