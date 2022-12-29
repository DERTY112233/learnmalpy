#!/bin/python3

import socket


servip = ''
servport = 

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((servip, servport))
    s.listen(1)
    conn, addr = s.accept()
    with conn:
        while True:
            conn.send(b"hello world")
            break
