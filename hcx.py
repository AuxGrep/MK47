#!/usr/bin/env python3

import sys
import time
import subprocess
import os

colorcode = {

	'RED':'\033[0;31m',
	'RESET':'\033[0m',
	'YELLOW':'\033[1;33m',
	'ITALIC':'\033[3m'
}

if not os.geteuid() == 0:
    sys.exit("\n{0}{2}PLease run this script as root{1}\n".format(colorcode['RED'], \
		colorcode['RESET'], colorcode['ITALIC']))

# Config
crack_signal = 22000
hashcat_format_file = f'dumpNetworks.hc{crack_signal}'
file_from_recon = 'recon_dumped.pcapng'
network_list = 'NetworkList'
wordlist = '/usr/share/wordlists/rockyou.txt'

# we need to enable these services
def network_manager():
	subprocess.run('sudo systemctl start NetworkManager.service', shell=True)
	time.sleep(2)
	subprocess.run('sudo systemctl start wpa_supplicant.service', shell=True)
	os.system(f'sudo hcxpcapngtool -o {hashcat_format_file} -E {network_list} {file_from_recon}')
network_manager();

with open(f'{network_list}', mode='r') as outputfile:
	check = outputfile.read()
	print('{1}{3}Discovered Network to Hack from {0}{2} are: '.format(file_from_recon, colorcode['YELLOW'], \
			colorcode['RESET'], colorcode['ITALIC']))
	print("")
	time.sleep(2)
	print(check)
	print('{1}{2}all network saved as {0}{3}'.format(network_list, colorcode['YELLOW'], colorcode['ITALIC'],\
		colorcode['RESET']))
	






	





