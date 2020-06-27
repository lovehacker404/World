import marshal, os, time

banner=("""\033[1;36m
                      :::!~!!!!!:.
                  .xUHWH!! !!?M88WHX:.
                .X*#M@$!!  !X!M$$$$$$WWx:.
               :!!!!!!?H! :!$!$$$$$$$$$$8X:
              !!~  ~:~!! :~!$!#$$$$$$$$$$8X:
             :!~::!H!<   ~.U$X!?R$$$$$$$$MM!
             ~!~!!!!~~ .:XW$$$U!!?$$$$$$RMM!
               !:~~~ .:!M"T#$$$$WX??#MRRMMM!
               ~?WuxiW*`   `"#$$$$8!!!!??!!!
             :X- M$$$$ \033[1;91mâœº \033[1;95m`"T#$T~!8$WUXU~
            :%`  ~#$$$m:        ~!~ ?$$$$$$
          :!`.-   ~T$$$$8xx.  .xWW- ~""##*"
.....   -~~:<` !    ~?T#$$@@W@*?$$ \033[1;91âœº \033[1;95m/`
W$@@M!!! .!~~ !!     .:XUW$W!~ `"~:    :
#"~~`.:x%`!!  !H:   !WM$$$$Ti.: .!WUn+!`
:::~:!!`:X~ .: ?H.!u "$$$B$$$!W:U!T$$M~
.~~   :X@!.-~   ?@WTWo("*$$$W$TH$! `
Wi.~!X$?!-~    : ?$$$B$Wu("**$RM!
$R@i.~~ !     :   ~$$$$$B$$en:``     
?MXT@Wx.~    :     ~"##*$$$$M~      
 \033[1;43m   \033[1;35mBlack \033[1;30mâ™¡\033[1;35m|\033[1;34mâ˜†\033[1;35m|\033[1;30mâ™¡ \033[1;35mMafia   \033[1;0m 
     _  _
   _| || |_          \033[1;32mCOMPILER PYTHON\033[1;36m
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
