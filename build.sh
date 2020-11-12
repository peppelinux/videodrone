#!/bin/bash

VDPATH=$1
CHROME_VER=$(chromium --version | awk -F' ' {'print $2'} | awk -F'.' {'print $1'})
Y4M_URL="https://media.xiph.org/video/derf/y4m/stefan_cif.y4m"

rm -Rf $VDPATH

if [ -z "$CHROME_VER" ]
then
      echo "Please install chromium"
      exit 1
else
      echo $(chromium --version)
fi

if [ -z "$VDPATH" ]
then
      echo "Installing to ./VideoDrone ..."
      VDPATH="VideoDrone"
fi

# virtualenv check
virtualenv -h 2>&1 > /dev/null
if [ $? -eq 1 ]; then 
    echo "Please install python3 virtualenv"
    exit 1
fi

# unzip check
unzip -h 2>&1 > /dev/null
if [ $? -eq 1 ]; then 
    echo "Please install unzip"
    exit 1
fi

# wget check
wget -h 2>&1 > /dev/null
if [ $? -eq 1 ]; then 
    echo "Please install wget"
    exit 1
fi

case $CHROME_VER in
  "86")
    zip_file_url="https://chromedriver.storage.googleapis.com/86.0.4240.22/chromedriver_linux64.zip"
    ;;
  "85")
    zip_file_url="https://chromedriver.storage.googleapis.com/85.0.4183.87/chromedriver_linux64.zip"
    ;;
  "84")
    zip_file_url="https://chromedriver.storage.googleapis.com/84.0.4147.30/chromedriver_linux64.zip"
    ;;
  *)
    zip_file_url="https://chromedriver.storage.googleapis.com/84.0.4147.30/chromedriver_linux64.zip"
    ;;
esac

mkdir $VDPATH && cd $VDPATH
wget $zip_file_url -O chromium.driver.zip && unzip chromium.driver.zip -d drivers/ 

mkdir y4ms
wget $Y4M_URL -O y4ms/example_cif.y4m

virtualenv -ppython3 env && source env/bin/activate
pip install videodrone

# set -x
# videodrone -c "videodrone.drones.jitsi_chrome" -r thatroom -y4m ./y4ms/ -lifetime 18 -n 2
