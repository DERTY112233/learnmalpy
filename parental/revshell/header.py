#!/bin/python3

import pyfiglet

def title(title, font):
    link = "https://github.com/DERTY112233"
    header = pyfiglet.figlet_format(f"{title}", font=f"{font}")
    print(f"{header}\n by DERTY {link}")
    print("<~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>")