#!/bin/python3

import socket

ipaddr = '192.168.8.2'
port = 22

sockboi = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
with sockboi as sockboi:
    sockboi.bind((ipaddr, port))
    sockboi.connect()
    sockboi.send(2048)
    sockboi.send(b'Hello, world')
    sockboi.close()
