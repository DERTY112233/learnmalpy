#!/bin/python3

import nmap
import pyfiglet
import socket


looker = nmap.PortScanner()

text = pyfiglet.figlet_format("NMAPY", font = "5lineoblique")
eye = pyfiglet.figlet_format("<<(x)>>", font = "alphabet" )
print(text)
print(eye)
print("by derty")
print("<---------------------------------------------------->")

mycomp = socket.gethostname()
myip = socket.gethostbyname(mycomp)
servport = 1-1501
ipaddr = input("enter the IP address you want to scan: ")
print("The IP you entered is: ", ipaddr)
type(ipaddr)


def server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((ipaddr, servport))
        s.listen(3)
        conn, ipaddr = s.accept()
        with conn:
            while True:
                conn.send(b"Hello world")
                break

def client():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((myip, servport))
        data = s.recv(1-1500)
        print(data)

    input()


resp = input("""what scan would you like to do? \n
        1) SYN scan \n
        2) UDP scan \n
        3) comprehensive scan \n
        response ->: """)
print("You have chosen: ", resp)

respopt = {'1':['-v -sS', 'tcp'], '2':['-v -sU','udp'], '3':['-v -sS -sV -sC -A -O','tcp']}
if resp not in respopt.keys():
    print("Choose an actual option please")
else:
    print("your nmap version is: ", looker.nmap_version())
    looker.scan(ipaddr,"1-1501",respopt[resp][0])
    print(looker.scaninfo())
    if looker.scaninfo() == 'up':
        print("port thing status: ", looker[ipaddr].state())
        print(looker[ipaddr].all_protocols)
        print("DA OPEN PORTS ARE: ", looker[ipaddr][respopt[resp][1]].keys())
        try:
            for port in range(1,1501):
                if looker[ipaddr].scaninfo() == "up" and looker[ipaddr].state == True:
                    nmap.connect()
                    print("open, up and connecting...")
        except:
            print("[]<-CLOSED->[]")



