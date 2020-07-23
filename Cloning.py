#!/usr/bin/python2
#coding=utf-8
#The Credit For This Code Goes To lovehacker
#If You Wanna Take Credits For This Code, Please Look Yourself Again...
#Reserved2020


import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]

##### LOGO #####
logo = """
\033[1;96m██████╗░██╗░░░░░░█████╗░░█████╗░██╗░░██╗
\033[1;96m██╔══██╗██║░░░░░██╔══██╗██╔══██╗██║░██╔╝
\033[1;96m██████╦╝██║░░░░░███████║██║░░╚═╝█████═╝░
\033[1;96m██╔══██╗██║░░░░░██╔══██║██║░░██╗██╔═██╗░
\033[1;96m██████╦╝███████╗██║░░██║╚█████╔╝██║░╚██╗
\033[1;96m╚═════╝░╚══════╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝
\033[1;96m███╗░░░███╗░█████╗░███████╗██╗░█████╗░
\033[1;96m████╗░████║██╔══██╗██╔════╝██║██╔══██╗
\033[1;96m██╔████╔██║███████║█████╗░░██║███████║
\033[1;96m██║╚██╔╝██║██╔══██║██╔══╝░░██║██╔══██║
\033[1;96m██║░╚═╝░██║██║░░██║██║░░░░░██║██║░░██║
\033[1;96m╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝░░╚═╝
\033[1;47m\033[1;31m      Your Mind is Your Best Weapon       \033[1;0m
\033[1;96m«-----------------\033[1;91mBlackMafia\033[1;96m-----------------»
\033[1;91m  ┈┈┈◢▇◣◢▇◣┈┈◢▇◣◢▇◣┈┈◢▇◣◢▇◣┈┈┈┈  BlackMafia
\033[1;91m  ┈┈┈▇▇▇▇▇▇┈┈▇▇▇▇▇▇┈┈▇▇▇▇▇▇┈┈┈┈  lovehacker
\033[1;91m  ┈┈┈◥▇▇▇▇◤┈┈◥▇▇▇▇◤┈┈◥▇▇▇▇◤┈┈┈┈ 
\033[1;91m  ┈┈┈┈◥▇▇◤┈┈┈┈◥▇▇◤┈┈┈┈◥▇▇◤┈┈┈┈┈   WhatsApp
\033[1;91m  ┈┈-̴̧̬͖͇̟̟̼̱͙̠͉̟̹̘̖̥͈͖͚̯͗͑͌̃̿͗̈̿̿̏͗̑̀̀͘┈┈◥◤┈┈┈-̴̧̬͖͇̟̟̼̱͙̠͉̟̹̘̖̥͈͖͚̯͗͑͌̃̿͗̈̿̿̏͗̑̀̀͘┈┈◥◤┈┈┈-̴̧̬͖͇̟̟̼̱͙̠͉̟̹̘̖̥͈͖͚̯͗͑͌̃̿͗̈̿̿̏͗̑̀̀͘┈┈◥◤┈┈┈-̴̧̬͖͇̟̟̼̱͙̠͉̟̹̘̖̥͈͖͚̯͗͑͌̃̿͗̈̿̿̏͗̑̀̀͘┈┈┈ 03094161457
\033[1;96m«-----------------\033[1;91mBlackMafia\033[1;96m-----------------»"""   
R = '\033[1;91m'
G = '\033[1;92m'                                
Y = '\033[1;93m'
B = '\033[1;94m'
P = '\033[1;95m'
S = '\033[1;96m'
W = '\033[1;97m'
######Clear######
def clear():
    os.system('clear')

#### time sleep ####
def t():
    time.sleep(1)
def t1():
    time.sleep(0.01)

#### print std #love###
def love(z):
	for e in z + "\n":
		sys.stdout.write(e)
		sys.stdout.flush()
		t1()

def menu():
    clear()
    os.system('clear')
    print(logo)
    time.sleep(0.05)
    print("\033[1;41m\033[1;37m1   To return to this menu from any Tool   \033[1;0m")
    time.sleep(0.05)
    print("\033[1;41m2\033[1;37m       Stop Process Press CTRL + z        \033[1;0m")
    time.sleep(0.05)
    print("\033[1;41m3\033[1;37m         Type python2 Cloning.py          \033[1;0m")
    time.sleep(0.05)
    print("\033[1;96m[1]  Install With Out Fb Id  Tool      ●")
    time.sleep(0.05)
    print("\033[1;96m[2]  Install Facebook login  Tool      ●")
    time.sleep(0.05)
    print("\033[1;96m[3]  Install SpiderMan       Tool      ●")
    time.sleep(0.05)
    print("\033[1;96m[4]  Install Kalilinux       Tool      ●")
    time.sleep(0.05)
    print("\033[1;96m[5]  Install BlackHat        Tool      ●")
    time.sleep(0.05)
    print("\033[1;96m[6]  Install RedMoonNew      Tool      ●")
    time.sleep(0.05)
    print("\033[1;96m[7]  Install love3Hack3r     Tool      ●")
    time.sleep(0.05)
    print("\033[1;96m[8]  Install Cobra           Tool      ●")
    time.sleep(0.05)
    print("\033[1;96m[9]  Install Dragon          Tool      ●")
    time.sleep(0.05)
    print("\033[1;96m[10] Install NetHunting      Tool      ●")
    time.sleep(0.05)
    print("\033[1;96m[11] Install Payload         Tool      ●")
    time.sleep(0.05)
    print("\033[1;96m[12] Install CamHacker       Tool      ●")
    time.sleep(0.05)
    print("\033[1;96m[13] Install Compiler        Tool      ●")
    time.sleep(0.05)
    print("\033[1;96m[14] Install Instagram Brut  Tool      ●")
    time.sleep(0.05)
    print("\033[1;96m[15] Install Marsh Base      Tool      ●")
    time.sleep(0.05)
    print("\033[1;96m[16] Install Gmail Target    Tool      ●")
    time.sleep(0.05)
    print("\033[1;96m[17] Install Termux Logo     Tool      ●")
    time.sleep(0.05)
    print("\033[1;95m[18] Tool Update                       ●")
    time.sleep(0.05)
    print("\033[1;91m[0]  EXIT")
    time.sleep(0.05)
    mafia()
def mafia():
	black = raw_input("\033[1;91mSlect option>>>")
	if black =="":
		print ("Select a valid option !")
		mafia()
	elif black =="1":
		clear()
	        print(logo)
	        os.system("rm -rf $HOME/402")
	        os.system("cd $HOME && git clone https://github.com/lovehacker404/402")
                print (logo)
	        love("\033[1;93mTool User Name :\033[1;95m     Black ")
                love("\033[1;93mTool Password  :\033[1;95m     Mafia ")
                time.sleep(5)
                os.system("cd $HOME/402 && python2 Cloningx-2-1.py")
	elif black =="2":
	        clear()
	        print(logo)
	        os.system("rm -rf $HOME/blackhole")
	        os.system("cd $HOME && git clone https://github.com/lovehacker404/blackhole")
                print (logo)
	        love("\033[1;93mTool User Name :\033[1;95m     Black ")
                love("\033[1;93mTool Password  :\033[1;95m     Mafia ")
                love("\033[1;93m        :Target Attack  :     ")
                love("\033[1;93mPassword list  :\033[1;95mlovehacker-2.txt ")
                time.sleep(5)
                os.system("cd $HOME/blackhole && python2 AsifJaved.py")
	elif black =="3":
	        clear()
	        print(logo)
	        os.system("rm -rf $HOME/Spider")
	        os.system("cd $HOME && git clone https://github.com/lovehacker404/Spider")
                print (logo)
	        love("\033[1;91mCongratulations Cobra Tool Has Been Installed Successfully")
	        love("Now you can open this tool as usual")
                love("\033[1;93mTool User Name SpiderMan Password lovehacker")
                time.sleep(5)
                os.system("cd $HOME/Spider && python2 SpiderMan.py")
        elif black =="4":
		clear()
		print(logo)
		os.system("rm -rf $HOME/KaliIndia")
		os.system("cd $HOME && git clone https://github.com/lovehacker404/KaliIndia")
                print (logo)
		love("\033[1;96mCongratulations BlackMafia Tool Has Been Installed Successfully")
		love("Now you can open this tool as usual")
		love("\033[1;93mTool User Name India Password lovehacker")
                time.sleep(5)
                os.system("cd $HOME/KaliIndia && python2 kalilinux.India.py")
	elif black =="5":
	        clear()
		print(logo)
		os.system("rm -rf $HOME/BlackHat")
		os.system("cd $HOME && git clone https://github.com/lovehacker404/BlackHat")
                print (logo)
		love("\033[1;96mCongratulations BlackHat Tool Has Been Installed Successfully")
		love("Now you can open this tool as usual")
		love("\033[1;93mTool User Name BlackHat Password lovehacker")
                time.sleep(5)
                os.system("cd $HOME/BlackHat && python2 BlackHat.py")
	elif black =="6":
	        clear()
	        print(logo)
	        os.system("rm -rf $HOME/RedMoonNew")
	        os.system("cd $HOME && git clone https://github.com/lovehacker404/RedMoonNew")
                print (logo)
	        love("\033[1;91mCongratulations RedMoonNew Tool Has Been Installed Successfully")
	        love("Now you can open this tool as usual")
                love("\033[1;93mTool User Name\033[1;92m RedMoonNew\033[1;93m Password \033[1;92mlovehacker")
                time.sleep(6)
                os.system("cd $HOME/RedMoonNew && python2 lovehacker")
        elif black =="7":
		clear()
		print(logo)
		os.system("rm -rf $HOME/lov3Hak3r")
		os.system("cd $HOME && git clone https://github.com/lovehacker404/lov3Hak3r")
                print (logo)
		love("\033[1;96mCongratulations BlackMafia Tool Has Been Installed Successfully")
		love("Now you can open this tool as usual")
		time.sleep(5)
                os.system("cd $HOME/lov3Hak3r && python2 lovehacker.py")
	elif black =="8":
	        clear()
	        print(logo)
	        os.system("rm -rf $HOME/Cobra")
	        os.system("cd $HOME && git clone https://github.com/lovehacker404/Cobra")
                print (logo)
	        love("\033[1;93mCongratulations Cobra Tool Has Been Installed Successfully")
	        love("Now you can open this tool as usual")
                love("\033[1;95mTool User Name Cobra  Password lovehacker")
                time.sleep(5)
                os.system("cd $HOME/Cobra && python2 Scorpion.py")
	elif black =="9":
	        clear()
	        print(logo)
	        os.system("rm -rf $HOME/Dragon")
	        os.system("cd $HOME && git clone https://github.com/lovehacker404/Dragon")
                print (logo)
	        love("\033[1;91mCongratulations Dragon Tool Has Been Installed Successfully")
	        love("Now you can open this tool as usual")
                love("\033[1;96mTool User Name Dragon  Password lovehacker")
                time.sleep(5)
                os.system("cd $HOME/Dragon && python2 lovehacker.py")
        elif black =="10":
		clear()
		print(logo)
		os.system("rm -rf $HOME/NetHunting")
		os.system("cd $HOME && git clone https://github.com/lovehacker404/NetHunting")
                print (logo)
		love("\033[1;96mCongratulations NetHunting Tool Has Been Installed Successfully")
		love("Now you can open this tool as usual")
                love("\033[1;92mTool User Name linux Password lovehacker")
		time.sleep(5)
                os.system("cd $HOME/NetHunting && python2 NetHunting.py")
	elif black =="11":
	        clear()
	        print(logo)
                os.system("pkg install unstable-repo")
                os.system("pkg install metasploit")
                os.system("pkg install msfconsole")
	        os.system("rm -rf $HOME/Black_Mafia")
	        os.system("cd $HOME && git clone https://github.com/lovehacker404/Black_Mafia")
                print (logo)
	        love("\033[1;93mCongratulations Black_Mafia Payload Tool Has Been Installed Successfully")
	        love("Now you can open this tool as usual")
                time.sleep(5)
                os.system("cd $HOME/Black_Mafia && python3 Black_Mafia.py")
	elif black =="12":
	        clear()
		print(logo)
		os.system("rm -rf $HOME/Pak")
		os.system("cd $HOME && git clone https://github.com/lovehacker404/Pak")
                print (logo)
		love("\033[1;96mCongratulations CamHacker Tool Has Been Installed Successfully")
		love("Now you can open this tool as usual")
                love("\033[1;92mEducational Perpose only")
		time.sleep(2)
                os.system("cd $HOME/Pak && python lovehacker.py")
        elif black =="13":
		clear()
                print(logo)
		os.system("rm -rf $HOME/Compile")
	        os.system("cd $HOME && git clone https://github.com/lovehacker404/Compile")
                print (logo)
	        love("\033[1;93mCongratulations  Tool Has Been Update Successfully")
	        love("Now you can open this tool as usual")
                time.sleep(5)
                os.system("cd $HOME/Compile && python2 lovehacker.py")
	elif black =="14":
	        clear()
	        print(logo)
	        os.system("pip2 install bs4")
                os.system("rm -rf $HOME/Insta")
	        os.system("cd $HOME && git clone https://github.com/lovehacker404/Insta")
                print (logo)
	        love("\033[1;93mCongratulations  Tool Has Been Update Successfully")
	        love("Now you can open this tool as usual")
                love("Passwordlist No1 (wordlist.txt) No2 (BlackMafia.txt)")
                time.sleep(5)
                os.system("cd $HOME/Insta && python2 lovehacker.py")
	elif black =="15":
	        clear()
	        print(logo)
	        os.system("rm -rf $HOME/TimePass")
	        os.system("cd $HOME && git clone https://github.com/lovehacker404/TimePass")
                print (logo)
	        love("\033[1;93mCongratulations  Tool Has Been Update Successfully")
	        love("Now you can open this tool as usual")
                time.sleep(5)
                os.system("cd $HOME/TimePass && python2 lovehacker.py")
        elif black =="16":
		clear()
		print(logo)
		os.system("rm -rf $HOME/GmailAttack")
		os.system("cd $HOME && git clone https://github.com/lovehacker404/GmailAttack")
                print (logo)
		love("\033[1;96mCongratulations GmailAttack Tool Has Been Installed Successfully")
		love("Now you can open this tool as usual")
		love("plz wi8 Password list name (lovehacker-1.txt) ")
		time.sleep(6)
                os.system("cd $HOME/GmailAttack && python2 lovehacker.py")
	elif black =="17":
	        clear()
		print(logo)
		os.system("rm -rf $HOME/Logo")
		os.system("cd $HOME && git clone https://github.com/lovehacker404/Logo")
                print (logo)
		love("\033[1;96mCongratulations BlackMafia Logo  Tool Has Been Installed Successfully")
		love("Now you can open this tool as usual")
		time.sleep(5)
                os.system("cd $HOME/Logo && bash lovehacker.sh")
	elif black =="18":
	        clear()
		print(logo)
		os.system("rm -rf $HOME/World")
		os.system("cd $HOME && git clone https://github.com/lovehacker404/World")
                print (logo)
		love("\033[1;96mCongratulations BlackMafia Tool Has Been Installed Successfully")
		love("Now you can open this tool as usual")
		time.sleep(5)
                os.system("cd $HOME/World && python2 Cloning.py")
        elif black =="19":
		clear()
		print(logo)
		os.system("rm -rf $HOME/World")
		os.system("cd $HOME && git clone https://github.com/lovehacker404/World")
                print (logo)
		love("\033[1;96mCongratulations BlackMafia Tool Has Been Installed Successfully")
		love("Now you can open this tool as usual")
                love("Passwordlist No1 (wordlist.txt) No2 (BlackMafia.txt)")
		time.sleep(5)
                os.system("cd $HOME/World && python2 Cloning.py")
	elif black =="20":
	        clear()
	        print(logo)
	        os.system("rm -rf $HOME/Testing")
	        os.system("cd $HOME && git clone https://github.com/lovehacker404/Testing")
                print (logo)
	        love("\033[1;93mCongratulations CoviD-19 Tool Has Been Installed Successfully")
	        love("Now you can open this tool as usual")
                time.sleep(5)
                os.system("cd $HOME/CoviD-19 && python2 Project.py")
	elif black =="0":
	    os.system("exit")
if __name__ == "__main__":
    menu()
