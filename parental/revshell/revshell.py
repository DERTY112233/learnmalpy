#!/bin/python3

import socket
import subprocess

#making socket object with tcp ipv4
sockboi = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ipaddr = input("Enter ip address: ")
port = int(input("Enter the port number: "))



with sockboi as s:
    try:
        s.connect((ipaddr, port))
        com = input("$")
        while com != 'quit' or 'exit':
            s.send(com.encode())
            out = s.recv(2048).decode()
            com = input("$")
            print(out)
        s.close()
    except:
        print("Unable to connect, an error has occured")

