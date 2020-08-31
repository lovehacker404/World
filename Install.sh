#!/bin/bash
clear

BLACK='\e[30m'
RED='\e[31m'
GREEN='\e[32m'
YELLOW='\e[33m'
BLUE='\e[34m'
PURPLE='\e[35m'
CYAN='\e[36m'
WHITE='\e[37m'
NC='\e[0m'
echo""
echo -e "${RED}  _     _         ______ _    _ _______ ______   "
echo " | |   | |  /\   / _____) |  / |_______|_____ \  "
echo " | |__ | | /  \ | /     | | / / _       _____) ) "
echo " |  __)| |/ /\ \| |     | |< < | |     (_____ (| "
echo " | |   | | |__| | \_____| | \ \| |_____      | | "
echo " |_|   |_|______|\______)_|  \_)\______)     |_| "
echo -e "${RED}                                                      ~ Tools for Hacking by Mr. BlackMafia ${NC}"
echo ""
echo -e "${YELLOW} Twitter.com/lovehacker | Instagram.com/lovehacker | Github.com/lovehacker404 ${NC} "
echo ""
echo "---------------------------------------------------------------------------------------"
echo ""
echo -e "${RED}[!] This Tool Must Run As ROOT [!]${NC}"
echo ""
echo -e "${CYAN}[>] Press ENTER to Install World, CTRL+C to Abort.${NC}"
read INPUT
echo ""

if [ "$PREFIX" = "/data/data/com.termux/files/usr" ]; then
    INSTALL_DIR="$PREFIX/usr/share/doc/World"
    BIN_DIR="$PREFIX/usr/bin/"
    pkg install -y git python2
else
    INSTALL_DIR="/usr/share/doc/World"
    BIN_DIR="/usr/bin/"
fi

echo "[✔] Checking directories...";
if [ -d "$INSTALL_DIR" ]; then
    echo "[!] A Directory World Was Found.. Do You Want To Replace It ? [y/n]:" ;
    read mama
    if [ "$mama" = "y" ]; then
        rm -R "$INSTALL_DIR"
    else
        exit
    fi
fi

echo "[✔] Installing ...";
echo "";
git clone https://github.com/lovehacker404/World "$INSTALL_DIR";
echo "#!/bin/bash
python $INSTALL_DIR/Cloning.py" '${1+"$@"}' > World;
chmod +x World;
sudo cp World /usr/bin/;
rm World;


if [ -d "$INSTALL_DIR" ] ;
then
    echo "";
    echo "[✔] Successfuly Installed BlackMafia!!! [✔]";
    echo "";
    echo "[✔]========================================================================[✔]";
    echo "[✔] ✔✔✔ All Is Done!! you can execute tool by typing World !! ✔✔✔ [✔]";
    echo "[✔]========================================================================[✔]";
    echo "";
else
    echo "[✘] Installation Failed !!! [✘]";
    exit
fi
