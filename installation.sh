#!/bin/sh
#Install python3
sudo apt-get update -y
sudo apt install -y python3
sudo apt install -y python3-pip
pip3 install --upgrade pip

#Install mysql client package
sudo apt install mysql-client -y

#Check to see if installed
mysql -V

echo ***MESSAGE FOR JAMIUL***MAKE SURE TO CHANGE THE IP ON SECURITY GROUP FOR RDS CONNECTION

pip install -r requirements.txt

