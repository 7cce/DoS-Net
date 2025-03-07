#!/usr/bin/env python3
import os
import sys 
import time
import datetime

os.system("clear")

R = "\033[91;1m"  # Red
G = "\033[92;1m"  # Green
B = "\033[94;1m"  # Blue
Y = "\033[93;1m"  # Yellow
C = "\033[96;1m"  # Cyan
M = "\033[95;1m"  # Magenta
W = "\033[97;1m"  # White
D = "\033[90;1m"  # Grey
S = "\033[0m"     # REST

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

now = datetime.datetime.now()
formatted_time = now.strftime("%I:%M %p")
formatted_day = now.strftime("%A")

date_day = "\033[94;1m" + "[" + "\033[92;1m" + "Today" + "\033[94;1m" + "]" + "\033[97;1m" + "(" + "\033[93;1m" + formatted_day + "\033[95;1m" + f" {now:%B %D %Y}" + "\033[97;1m" + ")" + "\033[94;1m" + "[" + "\033[92;1m" + "Time" + "\033[94;1m" + "]" + "\033[93;1m" + "[" + "\033[91;1m" + formatted_time + "\033[93;1m" + "]" + "\033[97;1m"


if os.geteuid() != 0:
    sudo = "\033[1;31m" + "sudo" + "\033[0m"
    root = "\033[93;1m" + "root" + "\033[97;1m"
    print(f"{please} {W}please use {root} Type a command {sudo}")
    sys.exit(1)

print(f'''
                                      {B}.{W}
                                     {B}/ \\{W}
  ____               _               {B}| |{W} 
 / ___|  ___   _ __ | |_ _ __   ___  {B}| |{W}
| |     / {Y}_{W} \ | '_ \| __| '__| / {R}_{W} \ {B}|.|{W}
| |___ | {Y}(0){W} || | | | |_| |   | {R}(0){W} |{B}|.|{W}
 \____| \_{Y}^{W}_/ |_| |_|\__|_|    \_{R}^{W}_/ {B}|:|{W}
                                     {B}|:|{W}
                                  {W}~{Y}\==8==/{W}~
                                      {R}8{W}
                                      {R}0{W}
''')
print(f'''
┏─────────────────────────────────────────────────────┓
│ {R}● {Y}● {G}●{W}                                               │
│ {B}INSTAGRAM {W}| {Y}https://www.instagram.com/3x_n/{W}         │
┗─────────────────────────────────────────────────────┛''')

def stop_network_manager():
    os.system("sudo ifconfig wlan0 down")
    os.system("sudo airmon-ng start wlan0")
    os.system("sudo airmon-ng check kill")
    os.system("sudo systemctl stop NetworkManager")
    os.system("clear")
    print(f"{W}[{G}INFO{W}] {B}Activation wlan0 down {G}ON{W}")
    time.sleep(0.25)
    print(f"{W}[{G}INFO{W}] {B}Activation airmon-ng wlan0 {M}START{W}")
    time.sleep(0.50)
    print(f"{W}[{G}INFO{W}] {B}Activation airmon-ng check kill {G}ON{W}")
    time.sleep(0.75)
    print(f"{W}[{G}INFO{W}] {B}Activation NetworkManager {R}STOP{W}")
    time.sleep(1)
    os.system("clear")
    print(f'''
                                      {B}.{W}
                                     {B}/ \\{W}
  ____               _               {B}| |{W} 
 / ___|  ___   _ __ | |_ _ __   ___  {B}| |{W}
| |     / {Y}_{W} \ | '_ \| __| '__| / {R}_{W} \ {B}|.|{W}
| |___ | {Y}(0){W} || | | | |_| |   | {R}(0){W} |{B}|.|{W}
 \____| \_{Y}^{W}_/ |_| |_|\__|_|    \_{R}^{W}_/ {B}|:|{W}
                                     {B}|:|{W}
                                  {W}~{Y}\==8==/{W}~
                                      {R}8{W}
                                      {R}0{W}

+----+---------------------------------+-------+
| {Y}ID{W} | {G}INFORMATION{W}                     | {M}MOD{W}   |
+----+---------------------------------+-------+
| {Y}1{W}  | {G}Activation wlan0 down{W}           | {B}ON{W}    |
| {Y}2{W}  | {G}Activation airmon-ng wlan0{W}      | {G}START{W} |
| {Y}3{W}  | {G}Activation airmon-ng check kill{W} | {B}ON{W}    |
| {Y}4{W}  | {G}Activation NetworkManager{W}       | {R}STOP{W}  |
+----+---------------------------------+-------+ 
''')    



def start_network_manager():
    os.system("sudo systemctl start NetworkManager")
    time.sleep(0.25)
    print(f"{W}[{G}INFO]{W} {B}start network manager {R}OFF{W}")
    time.sleep(1)
    print(f"{W}[{G}INFO]{W} {B}Activation NetworkManager {G}START{W}")
    time.sleep(1)
    os.system("clear")
    print(f'''
                                      {B}.{W}
                                     {B}/ \\{W}
  ____               _               {B}| |{W} 
 / ___|  ___   _ __ | |_ _ __   ___  {B}| |{W}
| |     / {Y}_{W} \ | '_ \| __| '__| / {R}_{W} \ {B}|.|{W}
| |___ | {Y}(0){W} || | | | |_| |   | {R}(0){W} |{B}|.|{W}
 \____| \_{Y}^{W}_/ |_| |_|\__|_|    \_{R}^{W}_/ {B}|:|{W}
                                     {B}|:|{W}
                                  {W}~{Y}\==8==/{W}~
                                      {R}8{W}
                                      {R}0{W}

+----+---------------------------------+-------+
| {Y}ID{W} | {G}INFORMATION{W}                     | {M}MOD{W}   |
+----+---------------------------------+-------+
| {Y}1{W}  | {G}Activation airmon-ng check kill{W} | {R}OFF{W}   |
| {Y}2{W}  | {G}Activation NetworkManager{W}       | {G}START{W} |
+----+---------------------------------+-------+ 
''')

def main():
    print(f"{W}[{G}*{W}] {B}use option:{W}")
    print(f"{W}[{G}1{W}] {Y}Stop Network Manager{W}")
    print(f"{W}[{G}2{W}] {Y}Start Network Manager{W}")

    choice = input(f"{W}[{G}+{W}] {B}Enter your choice (1 or 2): {Y}")
    print(1*f"{W}\n")
    if choice == "1":
        stop_network_manager()
    elif choice == "2":
        start_network_manager()
    else:
        print(f"{Y}[{R}!{Y}] {R}Invalid choice. Please enter 1 or 2.{W}")

if __name__ == "__main__":
    main()
