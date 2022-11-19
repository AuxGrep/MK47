#!/usr/bin/env python3

import sys
import time
import subprocess
import os

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
	os.system(f'hcxpcapngtool -o {hashcat_format_file} -E {network_list} {file_from_recon}')
network_manager();

with open(f'{network_list}', mode='r') as outputfile:
	check = outputfile.read()
	print(f'Discovered Network to Hack from {file_from_recon} are: ')
	print("")
	time.sleep(2)
	print(check)
	print('all network saved as {}'.format(network_list))
	





