import marshal, os, time

banner=("""\033[1;36m
                      
     _  _
   _| || |_          \033[1;31mCOMPILER PYTHON\033[1;36m
  |_  ..  _|
  |_      _|         \033[1;31mContact=>03094161457\033[1;36m
    |_||_|           \033[1;31mBlackMafia 
""")
def py():
	try:
		os.system('clear')
		print(banner)
		a=input("\033[1;37m File name => \033[1;32m")
		x=open(a).read()
		b=compile(x,'','exec')
		c=marshal.dumps(b)
		d=open("Hasil_"+a,'w')
		d.write('import marshal\n')
		d.write('exec(marshal.loads('+repr(c)+'))')
		d.close()
		time.sleep(1.5)
		print("\033[1;32mFile Mukamal ho gai: \033[1;36mHasil_"+a)
		print()
	except KeyboardInterrupt:
		print("\n\033[1;31m[!] ERROR: ap jin files ko mukamal karna chahty in ko yaqeeni bnain ")
		exit()
	
def py2():
	try:
		os.system('clear')
		print(banner)
		a=raw_input("\033[1;37m Nama File => \033[1;32m")
		x=open(a).read()
		b=compile(x,'','exec')
		c=marshal.dumps(b)
		d=open("Hasil_"+a,'w')
		d.write('import marshal\n')
		d.write('exec(marshal.loads('+repr(c)+'))')
		d.close()
		time.sleep(1.5)
		print("\033[1;32mFile Ok ho gai ha: \033[1;36mHasil_"+a)
		print
	except KeyboardInterrupt:
		print("\n\033[1;31m[!] ERROR: ap files ko yaqeeni bnain jo ap compiled main chahty hain  ")
		exit()

os.system('clear')
print(banner)
print("\033[1;32m[1] Python3")
print("[2] Python2")
ask=input("\033[1;37m[?] Slect   => \033[1;32m")
if ask == '1':
	py()
elif ask == 2:
	py2()
else:
	print("\n\033[1;31m[!] Invalid")
