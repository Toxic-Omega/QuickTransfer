clear
echo Installing Update...
echo 
apt update && apt upgrade -y
echo 
echo Installing Rename
echo 
apt install rename -y
echo 
echo Installing Apache2
echo 
apt install apache2 -y
echo 
echo Installing Python3
echo 
apt install python3 -y
echo 
echo Installing Pip
echo 
apt install python3-pip -y
echo 
echo Installing Zip
echo 
apt install zip -y
echo 
echo Installing Pytube
echo 
pip install pytube
echo 
echo Installing Wget
echo 
pip install wget
echo 
echo Installing Click
echo 
pip install click
echo 
echo Done!
echo
