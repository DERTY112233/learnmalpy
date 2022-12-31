#!/bin/python3

import socket

mycomp = socket.gethostname()
myip = socket.gethotbyname(mycomp)
servip = socket.gethostbyname(mycomp)
servport = 1-1501

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((servip, servport))
    data = s.recv(1024)
    print(data)


input()

