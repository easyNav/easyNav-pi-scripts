#!/bin/bash 

# Start dispatcher first
#killall -9 easyNav-pi-dispatcher
#easyNav-pi-dispatcher &
#sleep 5

# Launch screens
screen -c easyNavScreenRC.conf
