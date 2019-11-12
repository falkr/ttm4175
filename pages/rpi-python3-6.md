# Updating to Python 3.6


## Step 1: 

Install some dependencies for python3.6 :

```bash
sudo apt-get update
sudo apt-get install -y build-essential tk-dev libncurses5-dev libncursesw5-dev libreadline6-dev libdb5.3-dev libgdbm-dev libsqlite3-dev libssl-dev libbz2-dev libexpat1-dev liblzma-dev zlib1g-dev libffi-dev
```
## Step 2: 

Download python 3.6  and install it (this might take some time):

```bash
wget https://www.python.org/ftp/python/3.6.8/Python-3.6.8.tgz
sudo tar zxf Python-3.6.8.tgz
cd Python-3.6.8
sudo ./configure
sudo make -j 4
sudo make altinstall
```
Check that python3.6 is installed:

```bash
python3.6 -V
```

## Step 3: 

Setting python 3.6 as the default :

```bash
sudo echo "alias python3='/usr/local/bin/python3.6' ">>~/.bashrc 
source ~/.bashrc
```
Check python3 version:

```bash
python3  -V
```

## Step 4: 
Using 'pip3.6' to install other  packages with their dependencies in python3.6:

```bash
sudo apt-get install python-dev libsdl-image1.2-dev libsdl-mixer1.2-dev libsdl-ttf2.0-dev   libsdl1.2-dev libsmpeg-dev python-numpy subversion libportmidi-dev libswscale-dev libavformat-dev libavcodec-dev libsdl1.2-dev
sudo pip3.6 install slackclient
sudo pip3.6 install  RPi.GPIO
sudo pip3.6 install pygame
sudo pip3.6 install certifi
```


