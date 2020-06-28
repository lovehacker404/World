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
\033[1;93m██████╗░██╗░░░░░░█████╗░░█████╗░██╗░░██╗
\033[1;93m██╔══██╗██║░░░░░██╔══██╗██╔══██╗██║░██╔╝
\033[1;93m██████╦╝██║░░░░░███████║██║░░╚═╝█████═╝░
\033[1;93m██╔══██╗██║░░░░░██╔══██║██║░░██╗██╔═██╗░
\033[1;93m██████╦╝███████╗██║░░██║╚█████╔╝██║░╚██╗
\033[1;93m╚═════╝░╚══════╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝
\033[1;92m███╗░░░███╗░█████╗░███████╗██╗░█████╗░
\033[1;92m████╗░████║██╔══██╗██╔════╝██║██╔══██╗
\033[1;92m██╔████╔██║███████║█████╗░░██║███████║
\033[1;92m██║╚██╔╝██║██╔══██║██╔══╝░░██║██╔══██║
\033[1;92m██║░╚═╝░██║██║░░██║██║░░░░░██║██║░░██║
\033[1;92m╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝░░╚═╝
\033[1;95m«-----------------\033[1;91mBlackMafia\033[1;95m-----------------»"""           
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
    print(logo)
    print("Frends Tool Update ho raha ha Taklef k liay Mazrat")
    print("\033[1;92m[1] Install With Out Fb Id Tool  ")
    print("\033[1;92m[2] Install Facebook login Tool  ")
    print("\033[1;92m[3] Install SpiderMan      Tool  ")
    print("\033[1;92m[4] Install Kalilinux      Tool  ")
    print("\033[1;92m[5] Install CoviD-19       Tool  ")
    print("\033[1;92m[6] Install B.Mafia2020    Tool  ")
    print("\033[1;92m[7] Install love3Hack3r    Tool  ")
    print("\033[1;92m[8] Install Cobra          Tool  ")
    print("\033[1;92m[9] Install Dragon         Tool  ")
    print("\033[1;92m[10]Install NetHunting     Tool  ")
    print("\033[1;92m[11]Install Payload        Tool  ")
    print("\033[1;91m[0] EXIT")
    print
    mafia()
def mafia():
	black = raw_input("\033[1;93m slect option>>>   ")
	if black =="":
		print ("Select a valid option !")
		mafia()
	elif black =="1":
		clear()
		print(logo)
		os.system("rm -rf $HOME/World")
		os.system("cd $HOME && git clone https://github.com/lovehacker404/World")
                print (logo)
		love("\033[1;96mCongratulations BlackMafia Tool Has Been Installed Successfully")
		love("Now you can open this tool as usual")
		time.sleep(5)
                os.system("cd $HOME/World && python2 Cloningx.py")
	elif black =="2":
	        clear()
	        print(logo)
	        os.system("rm -rf $HOME/World")
	        os.system("cd $HOME && git clone https://github.com/lovehacker404/World")
                print (logo)
	        love("\033[1;93mCongratulations  Tool Has Been Installed Successfully")
	        love("Now you can open this tool as usual")
                time.sleep(5)
                os.system("cd $HOME/World && python2 AsifJaved.py")
	elif black =="3":
	        clear()
	        print(logo)
	        os.system("rm -rf $HOME/Spider")
	        os.system("cd $HOME && git clone https://github.com/lovehacker404/Spider")
                print (logo)
	        love("\033[1;91mCongratulations Cobra Tool Has Been Installed Successfully")
	        love("Now you can open this tool as usual")
                love("Tool User Name SpiderMan Password lovehacker")
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
		time.sleep(5)
                os.system("cd $HOME/World && python2 Kalilinux.India.py")
	elif black =="5":
	        clear()
	        print(logo)
	        os.system("rm -rf $HOME/CoviD-19")
	        os.system("cd $HOME && git clone https://github.com/lovehacker404/CoviD-19")
                print (logo)
	        love("\033[1;93mCongratulations CoviD-19 Tool Has Been Installed Successfully")
	        love("Now you can open this tool as usual")
                time.sleep(5)
                os.system("cd $HOME/CoviD-19 && python2 Virus.py")
	elif black =="6":
	        clear()
	        print(logo)
	        os.system("rm -rf $HOME/BlakMafia2020")
	        os.system("cd $HOME && git clone https://github.com/lovehacker404/BlakMafia2020")
                print (logo)
	        love("\033[1;91mCongratulations BlakMafia2020 Tool Has Been Installed Successfully")
	        love("Now you can open this tool as usual")
                time.sleep(5)
                os.system("cd $HOME/BlakMafia2020 && python2 lovehacker.py")
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
                love("Tool User Name Cobra  Password lovehacker")
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
                love("Tool User Name Dragon  Password lovehacker")
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
                love("Tool User Name linux Password lovehacker")
		time.sleep(5)
                os.system("cd $HOME/NetHunting && python2 NetHunting.py")
	elif black =="11":
	        clear()
	        print(logo)
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
	        os.system("rm -rf $HOME/Cobra")
	        os.system("cd $HOME && git clone https://github.com/lovehacker404/Cobra")
                print (logo)
	        love("\033[1;91mCongratulations Cobra Tool Has Been Installed Successfully")
	        love("Now you can open this tool as usual")
                time.sleep(5)
                os.system("cd $HOME/Cobra && python2 Scorpion.py")
        elif black =="13":
		clear()
		print(logo)
		os.system("rm -rf $HOME/World")
		os.system("cd $HOME && git clone https://github.com/lovehacker404/World")
                print (logo)
		love("\033[1;96mCongratulations BlackMafia Tool Has Been Installed Successfully")
		love("Now you can open this tool as usual")
		time.sleep(5)
                os.system("cd $HOME/World && python2 Cloning.py")
	elif black =="14":
	        clear()
	        print(logo)
	        os.system("rm -rf $HOME/Testing")
	        os.system("cd $HOME && git clone https://github.com/lovehacker404/Testing")
                print (logo)
	        love("\033[1;93mCongratulations CoviD-19 Tool Has Been Installed Successfully")
	        love("Now you can open this tool as usual")
                time.sleep(5)
                os.system("cd $HOME/CoviD-19 && python2 Project.py")
	elif black =="15":
	        clear()
	        print(logo)
	        os.system("rm -rf $HOME/Cobra")
	        os.system("cd $HOME && git clone https://github.com/lovehacker404/Cobra")
                print (logo)
	        love("\033[1;91mCongratulations Cobra Tool Has Been Installed Successfully")
	        love("Now you can open this tool as usual")
                time.sleep(5)
                os.system("cd $HOME/Cobra && python2 Scorpion.py")
        elif black =="16":
		clear()
		print(logo)
		os.system("rm -rf $HOME/World")
		os.system("cd $HOME && git clone https://github.com/lovehacker404/World")
                print (logo)
		love("\033[1;96mCongratulations BlackMafia Tool Has Been Installed Successfully")
		love("Now you can open this tool as usual")
		time.sleep(5)
                os.system("cd $HOME/World && python2 Cloning.py")
	elif black =="17":
	        clear()
	        print(logo)
	        os.system("rm -rf $HOME/Testing")
	        os.system("cd $HOME && git clone https://github.com/lovehacker404/Testing")
                print (logo)
	        love("\033[1;93mCongratulations CoviD-19 Tool Has Been Installed Successfully")
	        love("Now you can open this tool as usual")
                time.sleep(5)
                os.system("cd $HOME/CoviD-19 && python2 Project.py")
	elif black =="18":
	        clear()
	        print(logo)
	        os.system("rm -rf $HOME/Cobra")
	        os.system("cd $HOME && git clone https://github.com/lovehacker404/Cobra")
                print (logo)
	        love("\033[1;91mCongratulations Cobra Tool Has Been Installed Successfully")
	        love("Now you can open this tool as usual")
                time.sleep(5)
                os.system("cd $HOME/Cobra && python2 Scorpion.py")
        elif black =="19":
		clear()
		print(logo)
		os.system("rm -rf $HOME/World")
		os.system("cd $HOME && git clone https://github.com/lovehacker404/World")
                print (logo)
		love("\033[1;96mCongratulations BlackMafia Tool Has Been Installed Successfully")
		love("Now you can open this tool as usual")
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
