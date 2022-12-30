#!/bin/python3

import socket

mycomp = socket.gethostname()
myip = socket.gethotbyname(mycomp)
servip = 
servport =

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((servip, servport))
    data = s.recv(1024)
    print(data)


input()

