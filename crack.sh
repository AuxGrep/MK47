#!/usr/bin/bash
# now lets crack 

wordLIST="/usr/share/wordlists/rockyou.txt" # You can use also yours
file="dumpNetworks.hc22000"

if [ -f "dumpNetworks.hc22000" ]
then
clear
hashcat -m 22000 $file $wordLIST -o cracked_Networks.txt

else
   echo "File $file is not found"
   exit 0
fi


 
