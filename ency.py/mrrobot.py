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

passwd = input("provide a password for encryption: ")
passwd = b"{passwd}"

def encpass(passwd):
    passwd = b'{passwd}'
    passen = bcrypt.hashpw(passwd, bcrypt.gensalt())
    passen = sha256(sha256.digest(passen))
    print(passen)

encpass(passwd)
