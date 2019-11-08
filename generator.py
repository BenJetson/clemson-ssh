#!/usr/bin/env python3

import os
import random
from typing import List

CONFIG_FILE = os.path.expanduser("~/.ssh/config")
SOC_DOMAIN = "computing.clemson.edu"

def make_suffix_list(min: int, max: int) -> List[str]:
    out = []

    for i in range(min, max+1):
        out.append(str(i))

    return out


def add_config(config_file, username, hostname, alias=""):
    alias = hostname if alias == "" else alias

    config = "Host {}\n".format(alias)
    config += "\tHostName {}.{}\n".format(hostname, SOC_DOMAIN)
    config += "\tUser {}\n\n".format(username)

    config_file.write(config)

    print("Added: {} -> {}@{}.{}" \
        .format(alias, username, hostname, SOC_DOMAIN))


NO_SUFFIX = [""]

SERVERS = {
    "access": NO_SUFFIX + make_suffix_list(1, 2),
    "ada": make_suffix_list(1, 18),
    "babbage": make_suffix_list(1, 35),
    "joey": make_suffix_list(1, 21),
    "cerf": make_suffix_list(1, 30),
    "titan": make_suffix_list(1, 5),
    "newton": NO_SUFFIX,
}

if __name__ == "__main__":
    print("Welcome! This program generates a ~/.ssh/config file that will")
    print("contain entries for the Clemson SoC servers.")
    print()
    print("<i> INFO: This software comes with ABSOLUTELY NO WARRANTY! Use this")
    print("          program at your own risk. See LICENSE for details.")
    print()
    print("<!> WARNING: Proceeding will modify file at: {}".format(CONFIG_FILE))
    print("             This will alter how your SSH client works. Consider")
    print("             making a backup copy in case something goes wrong.")
    print()
    print("Please type \"I AGREE\" to continue.")

    agreement = input(">>> ")

    if agreement != "I AGREE":
        print("\n<!> ERROR: You cannot use this software if you do not accept")
        print("           the license terms. If you change your mind, run the")
        print("           program again.\n")

        exit(1)

    print("\nEnter your Clemson username.")
    username = input(">>> ")
    print()

    write_mode = 'w' if not os.path.exists(CONFIG_FILE) else 'a'
    if write_mode == 'a':
        print("File {} already exists.".format(CONFIG_FILE))
        print("Append (a) or Overwrite (w)?")
        write_mode = input("[a] >>> ")
        print()

        write_mode = 'a' if write_mode not in ['w', 'a'] else write_mode


    with open(CONFIG_FILE, write_mode) as config_file:
        for prefix, suffixes in SERVERS.items():
            # Pick a random suffix from this list for the canonical host.
            if len(suffixes) > 1:
                hostname = prefix + random.choice(suffixes)
                add_config(config_file, username, hostname, prefix)

            for suffix in suffixes:
                hostname = prefix + suffix
                add_config(config_file, username, hostname)
    
    random_hostname = random.choice(list(SERVERS.keys())[1:-1])
    random_suffix = random.choice(SERVERS[random_hostname])

    print()
    print("SUCCESS! Your SSH config now contains aliases for SoC machines.")
    print()
    print("Instead of typing all of this:")
    print("\tssh {}@{}{}.{}".format(username, random_hostname, 
        random_suffix, SOC_DOMAIN))
    print("Try using an alias like so:")
    print("\tssh {}{}".format(random_hostname, random_suffix))
    print()
    print("Furthermore, the script has randomly selected a host from each")
    print("group to connect to. So if you really want to save keystrokes:")
    print("\tssh {}".format(random_hostname))
    print()
