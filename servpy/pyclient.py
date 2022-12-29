#!/bin/python3

import socket

servip = ""
servport = 

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((servip, servport))
    data = s.recv(1024)
    print(data)


input()
