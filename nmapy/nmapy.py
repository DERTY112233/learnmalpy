#!/bin/python3

import nmap
import pyfiglet

looker = nmap.PortScanner()

text = pyfiglet.figlet_format("NMAPY", font = "5lineoblique")
eye = pyfiglet.figlet_format("<<(x)>>", font = "alphabet" )
print(text)
print(eye)
print("by derty")
print("<---------------------------------------------------->")

ipaddr = input("enter the IP address you want to scan: ")
print("The IP you entered is: ", ipaddr)
type(ipaddr)

resp = input("""what scan would you like to do? \n
        1) SYN scan \n
        2) UDP scan \n
        3) comprehensive scan \n
        : """)
print("You have chosen: ", resp)

respopt = {'1':['-v -sS', 'tcp'], '2':['-v -sU','udp'], '3':['-v -sS -sV -sC -A -O','tcp']}
if resp not in respopt.keys():
    print("Choose an actual option please")
else:
    print("your nmap version is: ", looker.nmap_version())
    looker.scan(ipaddr,"1-1500",respopt[resp][0])
    print(looker.scaninfo())
    if looker.scaninfo() == 'up':
        print("port thing status: ", looker[ipaddr].state())
        print(looker[ipaddr].all_protocols)
        print("DA OPEN PORTS ARE: ", looker[ipaddr][respopt[resp][1]].keys())
