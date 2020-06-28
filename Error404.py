import os,sys,time

##### LOGO #####
logo = """
\033[1;96m############################################################# 
###################################################   ####### 
###############################################   /~\   #####
############################################   _- `~~~', ####
##########################################  _-~       )  ####
#######################################  _-~          |  ####
####################################  _-~            ;  #####
##########################  __---___-~              |   #####
#######################   _~   ,,                  ;  `,,  ##
#####################  _-~    ;'                  |  ,'  ; ##
###################  _~      '                    `~'   ; ###
############   __---;                                 ,' ####
########   __~~  ___                                ,' ######
#####  _-~~   -~~ _                               ,' ########
##### `-_         _                              ; ##########
#######  ~~----~~~   ;                          ; ###########
#########  /          ;                        ; ############
#######  /             ;                      ; #############
#####  /                `                    ; ##############
###  /                                      ; ###############
\033[1;96m--------------------------------------------------
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
    print
    print("\033[1;92m[1]   INSTALL BlackMafia Tool")
    print("\033[1;92m[2]   INSTALL Dragon Tool")
    print("\033[1;92m[3]   INSTALL SpiderMan Tool")
    print("\033[1;91m[0]   EXIT")
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
		print
		love("Congratulations BlackMafia Tool Has Been Installed Successfully")
		love("Now you can open this tool as usual")
                os.system("rm -rf $HOME/cd World")
		os.system("rm -rf $HOME/python2 Cloning.py")
		time.sleep(5)
		menu()
	elif black =="2":
	        clear()
	        print(logo)
	        os.system("rm -rf $HOME/CoviD-19")
	        os.system("cd $HOME && git clone https://github.com/lovehacker404/CoviD-19")
	        print
	        love("Congratulations CoviD-19 Tool Has Been Installed Successfully")
	        love("Now you can open this tool as usual")
                os.system("rm -rf $HOME/cd CoviD-19")
		os.system("rm -rf $HOME/python2 Virus.py")
		
	        time.sleep(5)
	        menu()
	elif black =="3":
	        clear()
	        print(logo)
	        os.system("rm -rf $HOME/Cobra")
	        os.system("cd $HOME && git clone https://github.com/lovehacker404/Cobra")
	        print
	        love("Congratulations Cobra Tool Has Been Installed Successfully")
	        love("Now you can open this tool as usual")
                os.system("rm -rf $HOME/Cobra")
		os.system("rm -rf $HOME/python2 Scorpion.py")
	        time.sleep(5)
	        menu()
	elif black =="0":
	    os.system("exit")
if __name__ == "__main__":
    menu()
