#!/usr/bin/python3 env



import os
import random
import time
import pld_types as plds



# Cooded By : lovehacker
# Youtube   : https://youtube.com/c/BlackMafia
# Github    : https://github.com/lovehacker404
# Instagram : BlackMafia



rows, columns = os.popen('stty size', 'r').read().split()
Colms =  int ((int (columns)-37) / 2)-2
c = " " * Colms

colors = ["\033[1;33m","\033[1;37m","\033[1;31m", "\033[1;34m", "\033[1;32m"]
fore = random.choice (colors)
fore1 = "\033[1;36m"
fore2 = "\033[1;35m"
fore3 = "\033[1;31m"
os.system ("clear")



def finaly ():
	print (c+"\033[1;34m __________________________________")
	print (c+"|                                  |")
	print (c+"| \033[1;36mCooded By \033[1;34m :----->>   \033[1;31m lovehacker   \033[1;34m|")
	print (c+"| \033[1;36mYoutube   \033[1;34m :----->>   \033[1;31m BlackMafia \033[1;34m|")
	print (c+"| \033[1;36mInsagram  \033[1;34m :----->>   \033[1;31m BlackMafia \033[1;34m|")
	print (c+"| \033[1;36mGitHub    \033[1;34m :----->>   \033[1;31m lovehacker404 \033[1;34m|")
	print (c+"|__________________________________|")

# colors.
blue = "\033[1;34m"
cyan = "\033[1;36m"
norml = "\033[0m"



def banner ():
	os.system ("clear")
	print (" \n ")
	print (c+fore3+"     o        o       o            o")
	print (c+fore3+"      o      o          o        o")
	print (c+fore3+"       0 ■■ 0             0 ■■ 0")
	print (c+fore3+"       ■■■■■■ BlackMafia  ■■■■■■")
	print (c+fore3+"      ■■"+fore1+"▣"+fore3+"■■"+fore1+"▣"+fore3+"■■           ■■"+fore2+"◉"+fore3+"■■"+fore2+"◉"+fore3+"■■")
	print (c+fore3+"     ■■■■■■■■■■         ■■■■■■■■■■")
	print (c+fore3+"  ■■ ■■■■■■■■■■ ■■   ■■ ■■■■■■■■■■ ■■")
	print (c+fore3+"  ■■ ■■■■■■■■■■  ■■ ■■  ■■■■■■■■■■ ■■")
	print (c+fore3+"  ■■ ■■■■■■■■■■   ■■■   ■■■■■■■■■■ ■■")
	print (c+fore3+"     ■■■■■■■■■■         ■■■■■■■■■■")
	print (c+fore3+"       ■■  ■■ lovehacker  ■■  ■■")
	print (c+fore3+"       ■■  ■■ 03094161457 ■■  ■■")
	print (c+fore3+"        \033[1;47m   \033[1;34mBlack \033[1;30m♡\033[1;35m|\033[1;34m☆\033[1;35m|\033[1;30m♡ \033[1;34mMafia   \033[1;0m     ")
	print (c+fore3+"            ╭━━━━━━━◢◤━━━━╮")
	print (c+fore3+"            ┃┏┓┏━━┳◢◤┳┓╱╱╱┃")
	print (c+fore3+"            ┃┃┣┫╱╱◢◤╱╱┣━━━┃")
	print (c+fore3+"            ┃┗┛┗━◢◤┻┻┻┛╱╱╱┃")
	print (c+fore3+"            ╰━━━◢◤━━━━━━━━╯")
	print (c+fore2+"   This Tool is For Educational Purpose.")





# configure metasploit is installed or not.
def Check_requirments ():
	if os.path.exists ("/sdcard/Black_Mafia") == False :
		os.system ("mkdir /sdcard/Black_Mafia")

	if os.path.exists ('/data/data/com.termux/files/usr/bin/msfconsole') == True :
		print ("")
	else:
		print (blue+"--->>"+cyan+"  Checking Metasploit  ....")
		time.sleep (1)
		print (blue+"--->>"+cyan+"  Ooo No! Msfvenom isn't in your System")
		time.sleep (1)
		print (blue+"--->>"+cyan+"  Install Metasploit Correctly.")
		time.sleep (1)
		print (blue+"--->>"+cyan+"  Then try again.")
		print (" \n ")
		exit (0)


# Available options.
def chose_opt ():
	print ("\033[1;34mBlack \033[1;35m|\033[1;34m••\033[1;35m| \033[1;34mMafia\033[1;31m/~"+cyan+" Choose Your Payload\n")
	time.sleep (0.5)
	pld_list = ["Android" ,"Windows", "Linux", "Mac","Python","Bash", "Perl","Exit"]
	for pld in pld_list:
		time.sleep (0.1)
		print (cyan+"	["+blue,pld_list.index (pld)+1,cyan+"]   "+pld)
	print(" \n ")
	pld_type = int (input ("\033[1;34mBlack \033[1;30m~~\033[1;35m|\033[1;34m●\033[1;35m|\033[1;30m~~ \033[1;34mMafia\033[1;31m/~  \033[1;36m"))
	if pld_type > 8:
		try:
			raise ValueError
		except ValueError:
			print ("\033[1;34mBlack \033[1;30m~~\033[1;35m|\033[1;34m●\033[1;35m|\033[1;30m~~ \033[1;34mMafia\033[1;31m/~"+cyan+"  Plz Retry Enter number from given options."+norml)
			time.sleep(3)
			exit (0)

	else:
		pld_to_gen = ["plds.Android ()", "plds.Windows ()", "plds.Linux()", "plds.Mac ()", "plds.Python ()", "plds.Bash ()", "plds.Perl ()", "exite ()"]
		exec (pld_to_gen[pld_type - 1])



def exite ():
	time.sleep (1.2)
	banner()
	print ("\n\n\033[1;34mBlack \033[1;30m~~\033[1;35m|\033[1;34m●\033[1;35m|\033[1;30m~~ \033[1;34mMafia\033[1;31m/~"+cyan+"  God By BlackMafia Tool.\n\n")
	exit (0)


def main ():
	os.system ("termux-setup-storage")
	banner ()
	Check_requirments ()
	time.sleep (1.5)
	chose_opt ()


if __name__ == "__main__":
	try:
		main ()
	except KeyboardInterrupt:
		exite ()
	except ValueError:
		print ("\033[1;34mBlack \033[1;30m~~\033[1;35m|\033[1;34m●\033[1;35m|\033[1;30m~~ \033[1;34mMafia\033[1;31m/~"+cyan+"  Plz Retry Enter number from given options."+norml)
		time.sleep()
		exit (0)
	except EOFError:
		exite ()
