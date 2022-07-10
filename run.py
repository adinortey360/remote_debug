#import scanner from services folder
from services.scanner import Scanner as scout
import os
import argparse
import json
#ppadb import
from ppadb.client import Client as AdbClient

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--target', dest='target', help='Target IP Address/Adresses')
    options = parser.parse_args()

    #Check for errors i.e if the user does not specify the target IP Address
    #Quit the program if the argument is missing
    #While quitting also display an error message
    if not options.target:
        #Code to handle if interface is not specified
        parser.error("[-] Please specify an IP Address or Addresses, use --help for more info.")
    return options

options = get_args()
scanned_output = scout.scan(options.target)

for client in scanned_output:
    ip = client['ip']
    print(f"{client['ip']} is at {client['mac']}")
    #get data from env file
    with open('.env') as env_file:
        env_data = env_file.read()
        #for each line in the file
        for line in env_data.splitlines():
            #if line starts with ADB_LOCATION, split by = and get the value
            if line.startswith('ADB_LOCATION'):
                adb_location = line.split('=')[1]
                print(f"ADB location: {adb_location}")
                #execute shell command
                os.system(f"{adb_location} tcpip 5555")
                os.system(f"{adb_location} connect {ip}:5555")


    #print(device)