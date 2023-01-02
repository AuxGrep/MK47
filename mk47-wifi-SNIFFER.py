#!/usr/bin/env python3
# Author: AuxGrep
# Only for educational purposes !!! Don't misuase

import os
import time
import urllib.request
import subprocess
import sys

colorcode = {

	'RED':'\033[0;31m',
	'RESET':'\033[0m',
	'YELLOW':'\033[1;33m',
	'ITALIC':'\033[3m',
	'BLINK':'\033[5m'
}

if not os.geteuid() == 0:
    sys.exit("\n{0}{2}PLease run this script as root{1}\n".format(colorcode['RED'], \
		colorcode['RESET'], colorcode['ITALIC']))

wifimonitor = str(sys.argv[1])

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
	print('{1}{0}Run Again this script{2}'.format(colorcode['ITALIC'], colorcode['YELLOW'], \
		colorcode['RESET']))
	sys.exit()
else:

# Then let's start sniffing for Wireless Network based on your card if it is 2.4ghz or both 2.4ghz and 5ghz 
	print('{0}{2}Starting hcxdumptool process{1}'.format(colorcode['YELLOW'], colorcode['RESET'], \
		colorcode['ITALIC']))

def hcxdump():
	hcxdump_file = 'recon_dumped.pcapng'
	stx = 15
	subprocess.call(f'sudo hcxdumptool -i {wifimonitor} -o {hcxdump_file} --active_beacon --enable_status={stx}', shell=True)
	subprocess.run("clear")
	print(f'All wifi data saved as {hcxdump_file}, Highly recommend to use GPU to crack captured Networks')
	print("Now run {1}{2}{4}sudo python3 hcx.py{3} to convert dumped data from {1}{2}{0}{3}".format(hcxdump_file, \
		colorcode['RED'], colorcode['ITALIC'], \
			colorcode['RESET'], colorcode['BLINK']))

hcxdump();












