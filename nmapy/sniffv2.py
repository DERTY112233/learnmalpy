#!/bin/python3

import pyfiglet
import socket
import threading
import queue

title = pyfiglet.figlet_format("!!!sniff!!!")
v2 = pyfiglet.figlet_format("v2")
print(title)
print(v2)
print("by DERTY")
print("<----------------------------------------->")

ipaddr = input("Enter the IP address you'd like to scan the ports of: ")
qboi = queue.Queue()
sockboi = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

for i in range(1, 1501):
    qboi.put(i)

def sniff():
    while not qboi.empty():
        port = qboi.get()
    with sockboi as s:
        try:
            s.connect((ipaddr, port))
            print(f"port {port} is open and listening")
        except:
            pass
        qboi.task_done()


for i in range(20):
    t = threading.Thread(target=sniff, daemon=True)
    t.start()

qboi.join()

print("finished")
