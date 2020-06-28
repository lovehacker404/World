#!/usr/bin/python3
import os
import time
import sys

os.system("clear")

print('''\033[95m

┏━━┓┏┓╋╋╋╋╋╋┏┓╋┏━┓┏━┓╋╋╋┏━┓
┃┏┓┃┃┃╋╋╋╋╋╋┃┃╋┃┃┗┛┃┃╋╋╋┃┏┛
┃┗┛┗┫┃┏━━┳━━┫┃┏┫┏┓┏┓┣━━┳┛┗┳┳━━┓
┃┏━┓┃┃┃┏┓┃┏━┫┗┛┫┃┃┃┃┃┏┓┣┓┏╋┫┏┓┃
┃┗━┛┃┗┫┏┓┃┗━┫┏┓┫┃┃┃┃┃┏┓┃┃┃┃┃┏┓┃
┗━━━┻━┻┛┗┻━━┻┛┗┻┛┗┛┗┻┛┗┛┗┛┗┻┛┗┛
''')
def slowprint(s):
    for c in s + '\n' :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(5. / 100)

print (''' \033[93m
+--------------------------------------+
| This Tool Install All Basic Packages |
+--------------------------------------+
| Coded By lovehackee | version : 2.0  |
+--------------------------------------+''')

slowprint(''' \033[93m
[01] python
[02] python2
[03] python-dev
[04] python3
[05] php
[06] java
[07] git
[08] perl
[09] bash
[10] nano
[11] curl
[12] openssl
[13] openssh
[14] wget
[15] clang
[16] nmap
[17] w3m
[18] hydra
[19] ruby
[20] macchanger
[21] host
[22] dnsutils
[23] coreutils ''')
slowprint('''\033[96m
This Command for access Storage in Termux
[00] termux-setup-storage''')
print ("                                            ")
choice = input("\033[95mDo You Want to Install All Packages [y/n] : ")
if choice == 'n' : sys.exit()
if choice == 'y' : os.system ("apt update")
os.system ("atp upgrade -y")
os.system ("apt install python -y")
os.system ("apt install python2 -y")
os.system ("apt install php -y")
os.system ("apt install python-dev -y")
os.system ("apt install python3 -y")
os.system ("apt install java -y")
os.system ("apt install git -y")
os.system ("apt install perl -y")
os.system ("apt install bash")

print ("wait for second and start install All pkg")

os.system ("apt install nano -y")
os.system ("apt install curl -y")
os.system ("apt install openssl -y")
os.system ("apt install openssh -y")
os.system ("apt install wget -y")
os.system ("apt install clang -y")
os.system ("apt install nmap -y")
os.system ("apt install w3m -y")
os.system ("apt install hydra -y")


print ("""
subscribe lovehacker BlackMafia """)

os.system ("apt install ruby -y")
os.system ("apt install macchanger -y")
os.system ("apt install host -y")
os.system ("apt install dnsutils -y")
os.system ("apt install coreutils -y")

print ("Allow the Button For Access the Storage in Termux")


os.system ("termux-setup-storage")

def slowprint(s):
    for c in s + '\n' :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(8. / 100)
print("\033[95m+-------------------------------------------------+")
slowprint('''\033[95m|             Welcome To BlackMafia              |
|           Subscribe Our YouTube Channel         |
|              WhatsApp Num 03094161457        |''')
print("+-------------------------------------------------+")

input("\n\nPress the enter key to exit : ")
