#!/bin/sh


#Check if running with privileges
if [ "$(id -u)" -ne 0 ]; then
    echo "This script must be run as root. Cancelling..." >&2
    exit 1
fi

#Check if driver already installed
if [ -e "/usr/local/bin/geckodriver" ]; then
    echo "Driver already installed"
else
    #Unzip firefox driver
    tar -xvzf geckodriver-v0.31.0-linux64.tar.gz > /dev/null

    #Move driver to bin folder
    sudo mv geckodriver /usr/local/bin

    echo "Driver installed succesfuly"
fi

#Check if program already installed
if [ -e "/usr/local/bin/autologin" ]; then
    echo "Script already installed. If you want to update run update.sh"
else
    sudo mv autologin.py /usr/local/bin/autologin
    echo "Autologin installed succesfuly"
fi

