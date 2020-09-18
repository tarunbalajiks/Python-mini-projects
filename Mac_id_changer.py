# ======= LINUX =======#
# !/usr/bin/env python

import subprocess
import re
import optparse
import random


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface",
                      help="Interface to change its MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC Address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify an interface, --help for more info.")
    return options


# Create function to change MAC address provided by user.


def change_mac(interface, new_mac):
    print("[+] Changing MAC address for " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


# Create a function to retrieve the current MAC.


def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    mac_address_search_result = re.search(
        r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)

    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("[-] Could not read MAC address")


# function for get the arguments
options = get_arguments()

current_mac = get_current_mac(options.interface)
print("Current MAC = " + str(current_mac))
backup_cmd = "echo '" + current_mac + "' > backup_mac.txt"
subprocess.check_output(backup_cmd, shell=True)

if str(options.new_mac) != "None":
    # Execute the change_mac function.
    change_mac(options.interface, options.new_mac)
    # Get the new MAC address in use and print the message.
    current_mac = get_current_mac(options.interface)
    print(current_mac)
    if current_mac == options.new_mac:
        print("[+] MAC address changed successfully to " + current_mac)
    else:
        print("[-] Could not change MAC address")
else:
    # IF something goes wrong.
    print("Error changing MAC")
