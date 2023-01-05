#!/bin/python3

import requests
import os

myurl = input("Please enter url for html extraction: ")

def gethtml(myurl):
    html = requests.get(myurl)
    print("\n")
    f = open("gethtml.txt", "a")
    f.write(html)
    f.close()
    print("You will find the html in the gethtml.txt, have fun")

gethtml(myurl)

