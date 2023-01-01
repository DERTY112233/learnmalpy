#!/bin/python3

import pyfiglet
import socket

sniffban = pyfiglet.figlet_format("!!!SNIFF!!!")
print(sniffban)
print("by DERTY")
print("<-------------------------------------------->")

sockboy = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ipaddr = input("ENTER THE IP YOU WANT TO SCAN PORTS OF: ")

with sockboy as s:
    for port in range(1,1501):
        try:
            s.connect((ipaddr, port))
            print(f"port {port} is open and listening...")
        except:
            print(f"port {port} is closed, shame")
