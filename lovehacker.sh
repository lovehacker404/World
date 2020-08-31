#!/bin/bash
#BlackMafia 
clear
echo -e "\e[4;31m «-----------------BlackMafia-----------------»\e[0m"
echo -e "\e[1;35m«----- WhatsApp Num:    03094161457-----»\e[0m"
echo -e "\e[1;31m «-----------------BlackMafia-----------------»\e[0m"
echo -e "\e[1;36m «-----------------Disclaimer---------------»
 This Tool is for Educational Purpose
This presentation is for educational
purposes ONLY.How you use this information
is your responsibility.I will not be
held accountable This Tool/Channel Doesn't
Support illegal activities.for any illegal
Activitie This Tool is for Educational Purpose
«-----------------BlackMafia---------------» \e[0m"
echo "Press Enter To Continue"
read a1
if [[ -s update.BlackMafia ]];then
echo "All Requirements Found...."
else
echo 'Installing Requirements....'
echo .
echo .
apt install figlet toilet python curl -y
apt install python3-pip
pip install -r requirements.txt
echo This Script Was Made By BlackMafia >update.BlackMafia
echo Requirements Installed....
echo Press Enter To Continue...
read upd
fi
while :
do
rm *.xxx >/dev/null 2>&1
clear
echo -e "\e[1;31m"
figlet lovehacker
echo -e "\e[1;34m Created By \e[1;32m"
toilet -f mono12 -F border Black
toilet -f mono12 -F border Mafia
read ch
if [ $ch -eq 1 ];then
clear
echo -e "\e[1;32m"
rm *.xxx >/dev/null 2>&1
python2 Cloning.py
rm *.xxx >/dev/null 2>&1
exit 0
elif [ $ch -eq 2 ];then
clear
echo -e "\e[1;32m"
echo " BlackMafia"
python2 Cloning.py 
rm *.xxx >/dev/null 2>&1
exit 0
elif [ $ch -eq 3 ];then
clear
apt install git -y
echo -e "\e[1;34m Downloading Latest Files..."
git clone https://github.com/lovehacker404/World
if [[ -s World/Cloning.py ]];then
cd World
cp -r -f * .. > temp
cd ..
rm -rf  World >> temp
rm update.BlackMafia >> temp
rm temp
chmod +x Cloning.py
fi
read a6
./Cloning.sh
exit
elif [ $ch -eq 4 ];then
clear
echo -e "\e[1;33m"
figlet BlackMafia
echo -e "\e[1;34mCreated By \e[1;34m"
toilet -f mono12 -F border Love
toilet -f mono12 -F border Hacker
echo  " "
echo ""
echo ""
echo -e "\e[1;31m This Script is Only For Educational Purposes or To Prank.\e[0m"
echo -e "\e[1;31m Do not Use This To Harm Others. \e[0m"
echo -e "\e[1;31m I Am Not Responsible For The Misuse Of The Script. \e[0m"
echo -e "\e[1;32m Make Sure To Update it If It Does not Work.\e[0m"
echo  " "
echo "Press Enter To Go Home"
read a3
clear
elif [ $ch -eq 5 ];then
clear
echo -e "\e[1;31m"
figlet Lovehacker
echo -e "\e[1;34m God By \e[1;32m"
toilet -f mono12 -F border By By
echo -e "\e[4;34m This Script Was Created By BlackMafia \e[0m"
echo -e "\e[1;34m For Any Problum Contact Me!!!\e[0m"
echo -e "\e[1;32m          WhatsApp: 03094161457 \e[0m"
echo " "
exit 0
else
echo -e "\e[4;32m Invalid Input !!! \e[0m"
echo "Press Enter To Go Home"
read a3
clear
fi
done
