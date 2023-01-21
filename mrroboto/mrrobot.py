#!/bin/python3

import pyfiglet
import hashlib
from hashlib import sha256
import bcrypt


title = pyfiglet.figlet_format("Mr ROBOTO")
eyes = pyfiglet.figlet_format("<()> <()>")
mouth = pyfiglet.figlet_format("[====]")
print(title)
print(eyes)
print(mouth)

print("""[1] encrypt a password
[2] create encrypted file(tar,zip,gzip) 
[3] create and store encrypted passwords""")

resp = input(": ")

def encpass(passwd):
    passwd = b'{passwd}'
    passen = bcrypt.hashpw(passwd, bcrypt.gensalt())
    passen = passen.pop(0,1,-1)
    print(passen)

if resp == "1":
    passwd = input("Please provide a password for encrytion: ")
    encpass(passwd)
