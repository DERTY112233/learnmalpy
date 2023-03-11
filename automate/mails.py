#!bin/python3

import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart


servobj = smtplib.SMTP("smtp.gmail.com", 25)

servobj.ehlo()

user = input("[+]Username: ")
passwd = input("[+] password: ")

servobj.login(user, passwd)

mess = 
