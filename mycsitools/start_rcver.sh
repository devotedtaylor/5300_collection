#!/bin/bash
sudo ifconfig wlan0 down
cd $(sudo find / -path */linux-80211n-csitool-supplementary/injection)
sudo ./setup_monitor_csi.sh 64 HT20 
#sudo ip link set wlan0 down
#sudo ip link set wlan0 type monitor
#sudo ip link set wlan0 up
#sudo iw wlan0 set channel 64 HT20
#sudo ifconfig wlan0 up
cd $(sudo find / -path */mycsitools/Rcver)
sudo python ./CSIdisplayer2.py &
mypath=$(sudo find / -path */linux-80211n-csitool-supplementary/netlink)
sudo $mypath/log_to_file2 ./raw_bin_data.dat
sudo ifconfig wlan0 down
