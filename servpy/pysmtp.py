#!/bin/python3

import smtplib
from email import encoders
from enail.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart


server = smtplib.SMTP('smtp.gmail.com', 25)

server.ehlo()


with open('password.txt', 'r') as f:
    password = f.read()

server.login('joelpaiva112233@gmail.com', password)

msg = MIMEMultipart()
msg['from '] = 'DERTYBOI'
msg['to'] = '' # receiver
msg['subject'] = 'test'

with open('testmessage.txt', 'r') as f:
    message = f.read()

msg.attach(MIMEText(message, 'plain'))

filename = 'derty.PNG'
attachment = open(filename, 'rb') 

pay = MIMEBase('application', 'octet-stream')
pay.set_payload(attachment.read())

encoders.encode_base64(pay)
pay.add_header('Content-Disposition', f'attachment; filename {filename}')
msg.attach(pay)

text = msg.as_string()

server.sendmail('','', text) #sender, receiver
